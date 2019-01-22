from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='api-db', port=6379)

@app.route('/')
def hello():
    return redis.get('test')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
