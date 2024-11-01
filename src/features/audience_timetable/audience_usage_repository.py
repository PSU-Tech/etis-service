from src.core.etis_http.client import http_client
from src.features.audience_timetable.parser import parse_audience_usage


class AudienceUsageRepository:
    @staticmethod
    def get_audience_usage(audience_id: int, week: int):
        html = http_client.get_audience_usage(audience_id, week)
        return parse_audience_usage(html)
