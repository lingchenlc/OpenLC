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
    
    # Try all known user IDs to get primary calendar
    user_ids = [
        ("ou_e88b929a8c679fb495d4c4fb78c8b1a2", "open_id"),
        ("on_d1a4893276725aef85c125890f5f51d0", "union_id"),
        ("u_lswb8522", "user_id")
    ]
    
    for uid, utype in user_ids:
        # Feishu primary calendar ID is the user's ID
        url = f"https://open.feishu.cn/open-apis/calendar/v4/calendars/{uid}"
        resp = requests.get(url, headers=headers)
        print(f"Calendar for {uid} ({utype}): {resp.status_code}")
        if resp.status_code == 200:
            print(f"  {json.dumps(resp.json(), ensure_ascii=False, indent=2)}")
            # Try to get events
            url_events = f"https://open.feishu.cn/open-apis/calendar/v4/calendars/{uid}/events"
            revents = requests.get(url_events, headers=headers)
            print(f"    Events: {revents.status_code}")
