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
    
    # Try to subscribe to the user's primary calendar
    user_id = "ou_e88b929a8c679fb495d4c4fb78c8b1a2"
    url = "https://open.feishu.cn/open-apis/calendar/v4/calendar_list"
    resp = requests.post(url, headers=headers, json={"calendar_id": user_id})
    print(f"Subscribe to ({user_id}): {resp.status_code}")
    try:
        print(f"  {json.dumps(resp.json(), ensure_ascii=False, indent=2)}")
    except:
        print(f"  {resp.text[:100]}")
    
    # Try again with a different ID format?
    # No, open_id is the standard for Feishu.
