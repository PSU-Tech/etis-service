from bs4 import BeautifulSoup, Tag
import requests


def parse_audience_usage(html: str):
    soup = BeautifulSoup(html, 'html.parser')
    data = soup.find(class_="cgrldatarow")

    all_data_tags: list[Tag] = data.find_all('td')
    if len(all_data_tags) == 3:
        return  # NO DATA

    pairs_tags = all_data_tags[3:]

    days = []
    for pairs_tag in pairs_tags:
        pair_tag_class = pairs_tag.get('class')
        if pair_tag_class:
            pair_tag_class = pair_tag_class[0]
        if pair_tag_class == 'vert':
            days.append([])
            continue

        if pair_tag_class in ['in_use', 'in_use_red']:
            days[-1].append(True)
            continue
        days[-1].append(False)

    week_date_tag: Tag = soup.find('table').find('tr').find_all('td')[-1]
    _, week = week_date_tag.find('a').text.split()
    dates_raw = week_date_tag.contents[1].text.strip()
    date_start, date_end = dates_raw[1:len(dates_raw) - 1].split(' - ')

    return {
        "week": int(week),
        "dates": {
            "start": date_start,
            "end": date_end
        },
        "days": days
    }


def parse_audience_usage_info(html: str):
    soup = BeautifulSoup(html, 'html.parser')

    rows: list[Tag] = soup.find_all(class_="cgrldatarow")

    lesson_type = discipline = teacher = None
    groups = []

    for row in rows:
        num, student_count_plan, student_count_real, period, teach_plan_id, group, _lesson_type, _discipline, _teacher = list(map(lambda tag: tag.text, row.find_all('td')))

        if not lesson_type:
            lesson_type = _lesson_type
            discipline = _discipline
            teacher = _teacher
        groups.append(group)

    return {
        "lesson_type": lesson_type,
        "discipline": discipline,
        "teacher": teacher,
        "groups": groups
    }

aud_usage_req_s = "https://etis.psu.ru/pls/education/rep_chk2.usage_tr?p_ty_id=2024&p_bch_id=&p_sdiv_lsn=&p_cnt_method=3&P_ROO_ID=700&P_SOLE=&P_STEP=2&P_TYPE=1&P_WEEK=9&p_size=&p_pairs=1&p_pair=&p_grp=&p_common=&p_day=2"
usage_info_req_s = "https://etis.psu.ru/pls/education/rep_chk2.usage_tr_info?p_ty_id=2024&p_roo_id=700&p_term=1&p_week=9&p_day={0}&p_pair={1}"

def main():
    audience_usage = parse_audience_usage(requests.get(aud_usage_req_s).text)

    for day_number, day in enumerate(audience_usage["days"]):
        for pair_index in range(8):
            if day[pair_index]:
                res = requests.get(usage_info_req_s.format(day_number, pair_index + 1)).text
                usage_info = parse_audience_usage_info(res)
                print(usage_info)

main()