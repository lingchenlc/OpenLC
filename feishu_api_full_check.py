import requests
import json
import os
from datetime import datetime, timedelta

def get_tenant_access_token(app_id, app_secret):
    url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
    payload = json.dumps({"app_id": app_id, "app_secret": app_secret})
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=payload)
    return response.json().get("tenant_access_token")

def get_calendar_list(token):
    # This endpoint returns the calendars that the bot has added to its list
    url = "https://open.feishu.cn/open-apis/calendar/v4/calendar_list"
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=headers)
    return response.json()

def get_events(token, calendar_id, start_ts, end_ts):
    url = f"https://open.feishu.cn/open-apis/calendar/v4/calendars/{calendar_id}/events?start_time={start_ts}&end_time={end_ts}"
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=headers)
    return response.json()

if __name__ == "__main__":
    app_id = os.environ.get("FEISHU_APP_ID")
    app_secret = os.environ.get("FEISHU_APP_SECRET")
    token = get_tenant_access_token(app_id, app_secret)
    
    if not token:
        print(json.dumps({"error": "Failed to get token"}))
        exit(1)

    # Search for events for March 2nd, 2026 (GMT+8)
    start_dt = datetime(2026, 3, 2, 0, 0, 0) - timedelta(hours=8)
    end_dt = datetime(2026, 3, 2, 23, 59, 59) - timedelta(hours=8)
    start_ts = int(start_dt.timestamp())
    end_ts = int(end_dt.timestamp())

    cal_list_resp = get_calendar_list(token)
    if cal_list_resp.get("code") != 0:
        print(json.dumps({"error": "Failed to get calendar list", "resp": cal_list_resp}))
        exit(1)

    calendars = cal_list_resp.get("data", {}).get("calendar_list", [])
    report = {"calendars_found": len(calendars), "events": []}

    for cal in calendars:
        cal_id = cal.get("calendar_id")
        cal_name = cal.get("summary")
        ev_resp = get_events(token, cal_id, start_ts, end_ts)
        
        if ev_resp.get("code") == 0:
            items = ev_resp.get("data", {}).get("items", [])
            for item in items:
                s_ts = int(item.get("start_time", {}).get("timestamp"))
                e_ts = int(item.get("end_time", {}).get("timestamp"))
                report["events"].append({
                    "summary": item.get("summary"),
                    "start": (datetime.fromtimestamp(s_ts) + timedelta(hours=8)).strftime('%H:%M'),
                    "end": (datetime.fromtimestamp(e_ts) + timedelta(hours=8)).strftime('%H:%M'),
                    "calendar": cal_name,
                    "id": item.get("event_id")
                })
        else:
            report["events"].append({"error": f"Failed to fetch events for {cal_name}", "code": ev_resp.get("code")})

    print(json.dumps(report, ensure_ascii=False, indent=2))
