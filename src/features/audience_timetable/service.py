from src.features.audience.schemas import Audience
from src.features.audience_timetable.audience_usage_info_repository import AudienceUsageInfoRepository
from src.features.audience_timetable.audience_usage_repository import AudienceUsageRepository
from src.features.audience_timetable.schemas import Timetable, PartialAudience

times = [
    "8:00",
    "9:45",
    "11:30",
    "13:30",
    "15:15",
    "17:00",
    "18:40",
    "20:25",
]
MAX_PAIRS_IN_DAY = len(times)
FIRST_POSSIBLE_WEEK = 1
LAST_POSSIBLE_WEEK = 53 # Последняя неделя августа


class AudienceTimetableService:
    def get_audience_timetable(self, audience_id: int, week: int, audience: Audience):
        audience_usage = AudienceUsageRepository.get_audience_usage(audience_id, week)
        days_date = audience_usage.pop("days_date")
        timetable = {
            "week_info": {
                "first": FIRST_POSSIBLE_WEEK,
                "last": LAST_POSSIBLE_WEEK,
                "selected": audience_usage["week"],
                "dates": audience_usage["dates"],
            },
            "days": [],
        }

        for day_number, day in enumerate(audience_usage["days"]):
            day_obj = {"pairs": [], "date": days_date[day_number]}
            for pair_index in range(MAX_PAIRS_IN_DAY):
                if day[pair_index]:
                    usage_info = AudienceUsageInfoRepository.get_audience_usage_info(
                        audience_id, week, day_number + 1, pair_index + 1
                    )
                    type = usage_info.pop("type") if usage_info else None
                    pair = {
                        "position": pair_index + 1,
                        "time": times[pair_index],
                    }
                    if type is None:
                        pair["lessons"] = []
                    if type == "PAIR":
                        pair["lessons"] = [usage_info]
                    if type == "EVENT":
                        pair["event"] = usage_info

                    day_obj["pairs"].append(pair)
            timetable["days"].append(day_obj)

        return Timetable(
            **timetable, audience=PartialAudience(id=audience_id, number=audience.number, string=audience.number, building=audience.building)
        )
