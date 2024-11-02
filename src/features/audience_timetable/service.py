from src.features.audience_timetable.audience_usage_info_repository import AudienceUsageInfoRepository
from src.features.audience_timetable.audience_usage_repository import AudienceUsageRepository
from src.features.audience_timetable.schemas import Timetable

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


class AudienceTimetableService:
    def get_audience_timetable(self, audience_id: int, week: int):
        audience_usage = AudienceUsageRepository.get_audience_usage(audience_id, week)
        days_date = audience_usage.pop("days_date")
        timetable = {
            "week_info": {
                "first": 1,
                "last": 53,
                "selected": audience_usage["week"],
                "dates": audience_usage["dates"],
            },
            "days": [],
        }

        for day_number, day in enumerate(audience_usage["days"]):
            day_obj = {"pairs": [], "date": days_date[day_number]}
            for pair_index in range(8):
                if day[pair_index]:
                    usage_info = AudienceUsageInfoRepository.get_audience_usage_info(
                        audience_id, week, day_number + 1, pair_index + 1
                    )
                    type = usage_info.pop("type")
                    day_obj["pairs"].append(
                        {
                            "position": pair_index + 1,
                            "time": times[pair_index],
                            "lessons": [usage_info] if type == "PAIR" else [],
                            "event": usage_info if type == "EVENT" else None,
                        }
                    )
            timetable["days"].append(day_obj)

        return Timetable(**timetable)
