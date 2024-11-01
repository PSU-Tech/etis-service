from src.core.etis_http.client import http_client
from src.features.audience_timetable.parser import parse_audience_usage_info


class AudienceUsageInfoRepository:
    @staticmethod
    def get_audience_usage_info(audience_id: int, period: int, week: int, day: int, pair: int):
        res = http_client.get_audience_usage_info(audience_id, period, week, day, pair)
        return parse_audience_usage_info(res)
