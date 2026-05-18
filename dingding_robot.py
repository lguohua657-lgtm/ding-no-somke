import json
import requests
from flask import Flask, request

app = Flask(__name__)

# 你的钉钉机器人 Webhook
DINGTALK_WEBHOOK = "https://oapi.dingtalk.com/robot/send?access_token=20a5b1c3c1b269d28c6d67ef8c2b52a2c5806b97dd8a06caaac260fad0cfec5c"

def send_remind():
    headers = {"Content-Type": "application/json"}
    data = {
        "msgtype": "text",
        "text": {"content": "吸烟有害健康，请减少吸烟！"}
    }
    requests.post(DINGTALK_WEBHOOK, headers=headers, json=data)

@app.route("/webhook", methods=["POST"])
def receive():
    try:
        _ = request.get_json()
    except:
        pass
    send_remind()
    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
