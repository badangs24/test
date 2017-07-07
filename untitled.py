from flask import Flask

app = Flask(__name__)


@app.route('/')
def click():
    return <a href='click here'>


if __name__ == '__main__':
    app.run()
