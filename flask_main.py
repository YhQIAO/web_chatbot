from flask import Flask,  render_template, request, redirect, url_for,jsonify
from werkzeug.utils import secure_filename
import os
from datetime import timedelta
import urllib
import requests


app = Flask(__name__)
app.config['UPLOAD_POLDER'] = 'static/images/'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)

# 进入主页
@app.route('/index',methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/returnMessage',methods=['GET','POST'])
def returnMessage():
    send_message = request.values.get("send_message")
    print("对方发送的消息：" + send_message) 
    url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg={}'.format(urllib.parse.quote(send_message))
    html = requests.get(url)
    print("自动回复消息："+html.json()["content"])
    return html.json()["content"]



if __name__ == '__main__':
    app.run(debug=True)