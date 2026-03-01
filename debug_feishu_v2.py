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

def fetch_events(token, cal_id, start_ts, end_ts):
    url = f"https://open.feishu.cn/open-apis/calendar/v4/calendars/{cal_id}/events?start_time={start_ts}&end_time={end_ts}"
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=headers)
    return response.json()

if __name__ == "__main__":
    app_id = os.environ.get("FEISHU_APP_ID")
    app_secret = os.environ.get("FEISHU_APP_SECRET")
    token = get_tenant_access_token(app_id, app_secret)
    
    # 2026-03-02 GMT+8
    start_dt = datetime(2026, 3, 2, 0, 0, 0) - timedelta(hours=8)
    end_dt = datetime(2026, 3, 2, 23, 59, 59) - timedelta(hours=8)
    start_ts = int(start_dt.timestamp())
    end_ts = int(end_dt.timestamp())
    
    headers = {'Authorization': f'Bearer {token}'}
    
    all_events = []
    
    # 1. Get calendars the bot owns/has access to
    cal_resp = requests.get("https://open.feishu.cn/open-apis/calendar/v4/calendars", headers=headers).json()
    if cal_resp.get("code") == 0:
        for cal in cal_resp.get("data", {}).get("calendar_list", []):
            cid = cal.get("calendar_id")
            name = cal.get("summary")
            e_resp = fetch_events(token, cid, start_ts, end_ts)
            if e_resp.get("code") == 0:
                for item in e_resp.get("data", {}).get("items", []):
                    s_ts = int(item.get("start_time", {}).get("timestamp"))
                    e_ts = int(item.get("end_time", {}).get("timestamp"))
                    all_events.append({
                        "summary": item.get("summary"),
                        "start": (datetime.fromtimestamp(s_ts) + timedelta(hours=8)).strftime('%H:%M'),
                        "calendar": name
                    })

    # 2. Try to search for the user's primary calendar if we can find it
    # Often it's the email or something. Since we don't know, we'll ask.
    # But let's check if there's a "primary" for the bot itself (useless here).

    # 3. Use the Search Events API if available
    # POST https://open.feishu.cn/open-apis/calendar/v4/calendars/primary/events/search
    # But "primary" refers to the caller's primary calendar.

    print(json.dumps(all_events, ensure_ascii=False, indent=2))
