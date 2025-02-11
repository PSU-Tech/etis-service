import re

from bs4 import BeautifulSoup, Tag

from .schemas import LessonTypes

DATE_REGEX = re.compile(r".*\((\d{2}.\d{2}.\d{2})\)")
lesson_types = {
    "лек": LessonTypes.LECTURE,
    "практ": LessonTypes.PRACTICE,
    "лаб": LessonTypes.LABORATORY,
}


def parse_audience_usage(html: str):
    soup = BeautifulSoup(html, "html.parser")
    data = soup.find(class_="cgrldatarow")

    all_data_tags: list[Tag] = data.find_all("td")
    if len(all_data_tags) == 3:
        return  # NO DATA

    pairs_tags = all_data_tags[3:]

    days = []
    for pairs_tag in pairs_tags:
        pair_tag_class = pairs_tag.get("class")
        if pair_tag_class:
            pair_tag_class = pair_tag_class[0]
        if pair_tag_class == "vert":
            days.append([])
            continue

        if pair_tag_class in ["in_use", "in_use_red"]:
            days[-1].append(True)
            continue
        days[-1].append(False)

    table_trs = soup.find("table").find_all("tr", recursive=False)
    week_date_tag: Tag = table_trs[0].find_all("td")[-1]
    _, week = week_date_tag.find("a").text.split()
    dates_raw = week_date_tag.contents[1].text.strip()
    date_start, date_end = dates_raw[1 : len(dates_raw) - 1].split(" - ")

    days_date = list(
        map(lambda td: DATE_REGEX.findall(td.text.strip())[0], table_trs[1].find_all("td", align="center")[:6])
    )  # Сломанный HTML, в котором не закрыт тег tr

    return {"week": int(week), "dates": {"start": date_start, "end": date_end}, "days": days, "days_date": days_date}


def _get_event_data(soup: BeautifulSoup):
    table = soup.find_all("table")[-1]
    rows = table.find_all("tr")
    if not rows:
        return
    title_row, data_row = rows

    is_event = title_row.find_all("th")[1].text == "Мероприятие"
    if is_event:
        _, event_name, contact_info, department = list(map(lambda tag: tag.text, data_row.find_all("td")))
        return {"type": "EVENT", "name": event_name, "contact_info": contact_info, "department": department}


def parse_audience_usage_info(html: str):
    soup = BeautifulSoup(html, "html.parser")

    rows: list[Tag] = soup.find_all(class_="cgrldatarow")

    if not rows:
        return _get_event_data(soup)

    lesson_type = discipline = teacher = None
    groups = []
    for row in rows:
        row_data = list(map(lambda tag: tag.text, row.find_all("td")))

        (
            num,
            student_count_plan,
            student_count_real,
            period,
            teach_plan_id,
            group,
            _lesson_type,
            _discipline,
            _teacher,
        ) = row_data

        if not lesson_type:
            lesson_type = _lesson_type
            discipline = _discipline
            teacher = _teacher
        groups.append(group)

    return {
        "type": "PAIR",
        "subject": {"discipline": discipline, "type": lesson_types[lesson_type]},
        "teacher": {
            "name": teacher,
        },
        "groups": groups,
    }
