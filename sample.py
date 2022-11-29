from flask import Flask

app = Flask(__name__)


# ルートディレクトリにアクセスがあった時の処理
@app.route('/')
def hello():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
