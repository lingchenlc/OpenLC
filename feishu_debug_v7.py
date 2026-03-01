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
    
    # Try to access events of the user directly
    user_id = "ou_e88b929a8c679fb495d4c4fb78c8b1a2"
    url = f"https://open.feishu.cn/open-apis/calendar/v4/calendars/{user_id}/events"
    resp = requests.get(url, headers=headers)
    print(f"Events for User ({user_id}): {resp.status_code}")
    print(f"Body: {json.dumps(resp.json(), ensure_ascii=False, indent=2)}")
    
    # Try with another ID format if any
    # From CalDAV script: u_lswb8522
    url = f"https://open.feishu.cn/open-apis/calendar/v4/calendars/u_lswb8522/events"
    resp = requests.get(url, headers=headers)
    print(f"Events for User (u_lswb8522): {resp.status_code}")
    print(f"Body: {json.dumps(resp.json(), ensure_ascii=False, indent=2)}")
