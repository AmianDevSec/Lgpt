import requests as r

url  = "https://lgpt-back-end.onrender.com/ai/deepseek?prompt=coulduhelpme?"

response = r.request(url=url, timeout=5, method="get")

print(response.json()["response"])