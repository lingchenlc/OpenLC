import requests
import json
import os
from datetime import datetime, timedelta

def get_tenant_access_token(app_id, app_secret):
    url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
    payload = json.dumps({
        "app_id": app_id,
        "app_secret": app_secret
    })
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json().get("tenant_access_token")

def get_calendar_list(token):
    url = "https://open.feishu.cn/open-apis/calendar/v4/calendars"
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers)
    return response.json()

def get_events(token, calendar_id, start_time, end_time):
    url = f"https://open.feishu.cn/open-apis/calendar/v4/calendars/{calendar_id}/events?start_time={start_time}&end_time={end_time}"
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers)
    return response.json()

if __name__ == "__main__":
    app_id = os.environ.get("FEISHU_APP_ID")
    app_secret = os.environ.get("FEISHU_APP_SECRET")
    
    if not app_id or not app_secret:
        print("Missing FEISHU_APP_ID or FEISHU_APP_SECRET")
        exit(1)
        
    token = get_tenant_access_token(app_id, app_secret)
    if not token:
        print("Failed to get token")
        exit(1)
    
    # Target date: 2026-03-02
    start_dt = datetime(2026, 3, 2, 0, 0, 0) - timedelta(hours=8)
    end_dt = datetime(2026, 3, 2, 23, 59, 59) - timedelta(hours=8)
    
    start_ts = int(start_dt.timestamp())
    end_ts = int(end_dt.timestamp())
    
def get_calendar_list_alt(token):
    url = "https://open.feishu.cn/open-apis/calendar/v4/calendar_list"
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers)
    print(f"Response Status: {response.status_code}")
    print(f"Response Text: {response.text[:100]}")
    return response.json()

if __name__ == "__main__":
    # ...
    cals_resp = get_calendar_list_alt(token)
    calendars = cals_resp.get("data", {}).get("calendar_list", [])
    
    print(f"Calendars found: {len(calendars)}")
    all_events = []
    for cal in calendars:
        cal_id = cal.get("calendar_id")
        print(f"Checking calendar: {cal.get('summary')} ({cal_id})")
        events_resp = get_events(token, cal_id, start_ts, end_ts)
        items = events_resp.get("data", {}).get("items", [])
        print(f"  Events found: {len(items)}")
        for item in items:
            start_info = item.get("start_time", {})
            end_info = item.get("end_info", {}) # Wait, end_info? No, end_time
            
            s_ts = start_info.get("timestamp")
            e_ts = item.get("end_time", {}).get("timestamp")
            
            s_dt = datetime.fromtimestamp(int(s_ts)) + timedelta(hours=8)
            e_dt = datetime.fromtimestamp(int(e_ts)) + timedelta(hours=8)
            
            all_events.append({
                "summary": item.get("summary"),
                "start": s_dt.strftime('%H:%M'),
                "end": e_dt.strftime('%H:%M'),
                "calendar": cal.get("summary")
            })
    
    # Also check the user's open_id as a potential calendar_id
    # Also check the "primary" calendar
    print(f"Checking primary calendar...")
    events_resp = get_events(token, "primary", start_ts, end_ts)
    if events_resp.get("code") == 0:
        items = events_resp.get("data", {}).get("items", [])
        print(f"  Events found: {len(items)}")
        for item in items:
            s_ts = item.get("start_time", {}).get("timestamp")
            e_ts = item.get("end_time", {}).get("timestamp")
            s_dt = datetime.fromtimestamp(int(s_ts)) + timedelta(hours=8)
            e_dt = datetime.fromtimestamp(int(e_ts)) + timedelta(hours=8)
            all_events.append({
                "summary": item.get("summary"),
                "start": s_dt.strftime('%H:%M'),
                "end": e_dt.strftime('%H:%M'),
                "calendar": "Primary"
            })
    else:
        print(f"  Error checking primary calendar: {events_resp.get('msg')}")
    print(json.dumps(all_events, ensure_ascii=False, indent=2))
