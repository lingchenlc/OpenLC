import requests
import json
import os
from datetime import datetime, timedelta

def get_tenant_access_token(app_id, app_secret):
    url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
    payload = json.dumps({"app_id": app_id, "app_secret": app_secret})
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json().get("tenant_access_token")

def fetch_events(token, cal_id, start_ts, end_ts):
    url = f"https://open.feishu.cn/open-apis/calendar/v4/calendars/{cal_id}/events?start_time={start_ts}&end_time={end_ts}"
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    response = requests.request("GET", url, headers=headers)
    return response.json()

if __name__ == "__main__":
    app_id = os.environ.get("FEISHU_APP_ID")
    app_secret = os.environ.get("FEISHU_APP_SECRET")
    token = get_tenant_access_token(app_id, app_secret)
    
    # Time: 2026-03-02 GMT+8
    start_ts = int((datetime(2026, 3, 2, 0, 0, 0) - timedelta(hours=8)).timestamp())
    end_ts = int((datetime(2026, 3, 2, 23, 59, 59) - timedelta(hours=8)).timestamp())
    
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    
    # Try both endpoints to be complete
    endpoints = ["https://open.feishu.cn/open-apis/calendar/v4/calendars", 
                 "https://open.feishu.cn/open-apis/calendar/v4/calendar_list"]
    
    all_events = []
    seen_cal_ids = set()
    
    for url in endpoints:
        resp = requests.get(url, headers=headers).json()
        if resp.get("code") == 0:
            data = resp.get("data", {})
            cals = data.get("calendar_list", []) or data.get("calendars", [])
            for cal in cals:
                cal_id = cal.get("calendar_id")
                if cal_id in seen_cal_ids: continue
                seen_cal_ids.add(cal_id)
                
                events_resp = fetch_events(token, cal_id, start_ts, end_ts)
                if events_resp.get("code") == 0:
                    items = events_resp.get("data", {}).get("items", [])
                    for item in items:
                        s_ts = item.get("start_time", {}).get("timestamp")
                        e_ts = item.get("end_time", {}).get("timestamp")
                        all_events.append({
                            "summary": item.get("summary"),
                            "start": (datetime.fromtimestamp(int(s_ts)) + timedelta(hours=8)).strftime('%H:%M'),
                            "end": (datetime.fromtimestamp(int(e_ts)) + timedelta(hours=8)).strftime('%H:%M'),
                            "calendar": cal.get("summary")
                        })
    
    print(json.dumps(all_events, ensure_ascii=False, indent=2))
