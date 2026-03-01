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

def test_api(token, method, url, data=None):
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    if method == "GET":
        resp = requests.get(url, headers=headers)
    else:
        resp = requests.post(url, headers=headers, json=data)
    
    print(f"URL: {url}")
    print(f"Status: {resp.status_code}")
    try:
        print(f"Body: {json.dumps(resp.json(), ensure_ascii=False, indent=2)}")
    except:
        print(f"Body: {resp.text[:200]}")
    print("-" * 20)

if __name__ == "__main__":
    app_id = os.environ.get("FEISHU_APP_ID")
    app_secret = os.environ.get("FEISHU_APP_SECRET")
    token = get_tenant_access_token(app_id, app_secret)
    
    # 1. Test calendars list (calendars created by bot)
    test_api(token, "GET", "https://open.feishu.cn/open-apis/calendar/v4/calendars")
    
    # 2. Test calendar_list (calendars bot is subscribed to)
    test_api(token, "GET", "https://open.feishu.cn/open-apis/calendar/v4/calendar_list")
    
    # 3. Test searching for user primary calendar
    # If the user has a primary calendar, its ID is usually their open_id if the app has permission
    user_id = "ou_e88b929a8c679fb495d4c4fb78c8b1a2"
    test_api(token, "GET", f"https://open.feishu.cn/open-apis/calendar/v4/calendars/{user_id}")
