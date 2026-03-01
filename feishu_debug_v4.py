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
    
    # 1. Get user info for ou_e88b929a8c679fb495d4c4fb78c8b1a2
    uid = "ou_e88b929a8c679fb495d4c4fb78c8b1a2"
    url = f"https://open.feishu.cn/open-apis/contact/v3/users/{uid}?user_id_type=open_id"
    resp = requests.get(url, headers=headers)
    print(f"User Info: {json.dumps(resp.json(), ensure_ascii=False, indent=2)}")
    
    # 2. Try to find primary calendar for this user
    # Try multiple ways to identify the user
    for user_type in ["open_id", "user_id"]:
        # If user_id, use u_lswb8522
        actual_id = uid if user_type == "open_id" else "u_lswb8522"
        url = f"https://open.feishu.cn/open-apis/calendar/v4/calendars/primary?user_id_type={user_type}&user_id={actual_id}"
        resp = requests.get(url, headers=headers)
        print(f"Primary Cal ({user_type}): {resp.status_code}")
        try:
            print(f"  {json.dumps(resp.json(), ensure_ascii=False, indent=2)}")
        except:
            print(f"  {resp.text[:100]}")
