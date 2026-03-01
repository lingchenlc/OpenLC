import requests
import json
import os

def get_tenant_access_token(app_id, app_secret):
    url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
    payload = json.dumps({"app_id": app_id, "app_secret": app_secret})
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=payload)
    return response.json().get("tenant_access_token")

if __name__ == "__main__":
    app_id = os.environ.get("FEISHU_APP_ID")
    app_secret = os.environ.get("FEISHU_APP_SECRET")
    token = get_tenant_access_token(app_id, app_secret)
    
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    
    # 1. Search for calendars with an empty query (to find all accessible)
    url = "https://open.feishu.cn/open-apis/calendar/v4/calendars/search"
    resp = requests.post(url, headers=headers, json={"query": ""})
    print(f"Search Results: {json.dumps(resp.json(), ensure_ascii=False, indent=2)}")
    
    # 2. Try to get events using the specific calendar ID from Turn 5
    cal_id = "feishu.cn_yenbVDdJkJL5zQJXHQKRGf@group.calendar.feishu.cn"
    url = f"https://open.feishu.cn/open-apis/calendar/v4/calendars/{cal_id}/events"
    resp = requests.get(url, headers=headers)
    print(f"OpenClaw 日历 Events: {len(resp.json().get('data', {}).get('items', []))}")
