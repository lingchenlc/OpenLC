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
    
    # Try searching for a user named LC or anything like that
    url = "https://open.feishu.cn/open-apis/contact/v3/users/search"
    resp = requests.post(url, headers=headers, json={"query": "LC"})
    print(f"User Search (LC): {json.dumps(resp.json(), ensure_ascii=False, indent=2)}")
    
    # Try searching for the email chling.cl@gmail.com
    url = "https://open.feishu.cn/open-apis/contact/v3/users/batch_get_id?user_id_type=open_id"
    resp = requests.post(url, headers=headers, json={"emails": ["chling.cl@gmail.com"]})
    print(f"User Batch Get (Email): {json.dumps(resp.json(), ensure_ascii=False, indent=2)}")
