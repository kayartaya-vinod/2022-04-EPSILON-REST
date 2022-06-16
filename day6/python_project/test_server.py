from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', message='Hello, world!', username='Vinod')


if __name__ == '__main__':
    app.run(port=8080, debug=True)
