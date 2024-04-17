from flask import Flask, request
import time

app = Flask(__name__)

@app.route('/')
def home():
    ip_address = request.remote_addr
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    with open('user_ips.txt', 'a') as f:
        f.write(f'{timestamp} - {ip_address}\n')
    return "Hello, World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)