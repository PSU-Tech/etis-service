import datetime
from typing import Any, Optional

import requests

ORIGIN_URL = "https://etis.psu.ru/pls/education"
PROXY_URL = "https://etisproxy0.damego.ru/etis/pls/education"


class ETISHTTPClient:
    def __init__(self):
        self.session = requests.Session()

    def request(self, method: str, endpoint: str, *, params: Optional[dict[str, Any]] = None):
        print(f"[{method}] {endpoint} {params=}")
        return self.session.request(method, PROXY_URL + endpoint, params=params)

    def get_audience_usage(self, audience_id: int, week: int):
        params = {"P_ROO_ID": audience_id, "P_STEP": 2, "P_WEEK": week, "P_PAIRS": 1, "P_GRP": ""}

        response = self.request("GET", "/rep_chk2.usage_tr", params=params)
        return response.text

    def get_audience_usage_info(self, audience_id: int, period: int, week: int, day: int, pair: int):
        params = {
            "P_TY_ID": datetime.datetime.today().year,
            "P_WEEK": week,
            "P_DAY": day,
            "P_PAIR": pair,
            "P_TERM": period,
            "P_ROO_ID": audience_id,
        }
        response = self.request("GET", "/rep_chk2.usage_tr_info", params=params)
        return response.text


http_client = ETISHTTPClient()
