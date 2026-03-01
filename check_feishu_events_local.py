import sys
import requests
import json
import os
from datetime import datetime, timezone

APP_ID = os.environ.get("FEISHU_APP_ID")
APP_SECRET = os.environ.get("FEISHU_APP_SECRET")

def get_tenant_access_token():
    url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
    headers = {"Content-Type": "application/json; charset=utf-8"}
    data = {"app_id": APP_ID, "app_secret": APP_SECRET}
    resp = requests.post(url, headers=headers, json=data)
    resp.raise_for_status()
    return resp.json().get("tenant_access_token")

def list_calendars(token):
    url = "https://open.feishu.cn/open-apis/calendar/v4/calendars"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json; charset=utf-8"
    }
    resp = requests.get(url, headers=headers)
    return resp.json()

def get_calendar_list(token):
    url = "https://open.feishu.cn/open-apis/calendar/v4/calendar_list"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json; charset=utf-8"
    }
    resp = requests.get(url, headers=headers)
    return resp.json()

if __name__ == "__main__":
    try:
        token = get_tenant_access_token()
        cal_list = get_calendar_list(token)
        print("Calendar List Results:")
        print(json.dumps(cal_list, ensure_ascii=False, indent=2))
    except Exception as e:
        print(json.dumps({"error": str(e)}))
