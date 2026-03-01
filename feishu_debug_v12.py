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
    
    # Try getting primary calendar with union_id
    union_id = "on_d1a4893276725aef85c125890f5f51d0"
    url = f"https://open.feishu.cn/open-apis/calendar/v4/calendars/primary?user_id_type=union_id&user_id={union_id}"
    resp = requests.get(url, headers=headers)
    print(f"Primary Cal (union_id): {resp.status_code}")
    try:
        print(f"  {json.dumps(resp.json(), ensure_ascii=False, indent=2)}")
    except:
        print(f"  {resp.text[:100]}")
