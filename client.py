import requests

resp = requests.get(
    "http://0.0.0.0:8000/predict?source=https://raw.githubusercontent.com/ultralytics/ultralytics/main/ultralytics/assets/zidane.jpg&save_txt=T",
    verify=False,
)
print(resp.content)
