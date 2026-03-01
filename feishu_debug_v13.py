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
    
    # Try searching calendars by the user's ID
    url = "https://open.feishu.cn/open-apis/calendar/v4/calendars/search"
    resp = requests.post(url, headers=headers, json={"query": "u_lswb8522"})
    print(f"Search Results (u_lswb8522): {json.dumps(resp.json(), ensure_ascii=False, indent=2)}")
    
    # Try searching for the user's name
    resp = requests.post(url, headers=headers, json={"query": "凌晨"})
    print(f"Search Results (凌晨): {json.dumps(resp.json(), ensure_ascii=False, indent=2)}")
