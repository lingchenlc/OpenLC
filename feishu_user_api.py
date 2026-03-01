import requests
import json
import os
from datetime import datetime, timedelta

def get_user_access_token():
    return os.environ.get("FEISHU_USER_TOKEN")

def get_user_calendar_events(token, start_ts, end_ts):
    # Endpoint to get primary calendar events for the user
    url = "https://open.feishu.cn/open-apis/calendar/v4/calendars/primary/events"
    params = {
        "start_time": start_ts,
        "end_time": end_ts,
        "user_id_type": "open_id"
    }
    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get(url, headers=headers, params=params)
    return resp.json()

if __name__ == "__main__":
    user_token = get_user_access_token()
    if not user_token:
        print("请设置环境变量 FEISHU_USER_TOKEN")
        exit(1)
    
    # 2026-03-02
    start_ts = int((datetime(2026, 3, 2, 0, 0, 0) - timedelta(hours=8)).timestamp())
    end_ts = int((datetime(2026, 3, 2, 23, 59, 59) - timedelta(hours=8)).timestamp())
    
    events_resp = get_user_calendar_events(user_token, start_ts, end_ts)
    print(json.dumps(events_resp, ensure_ascii=False, indent=2))
