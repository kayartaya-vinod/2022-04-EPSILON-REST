from flask import Flask  # import the class 'Flask' from module 'flask'

# create an object of class 'Flask'
app = Flask(__name__)


# handler method for a given url request (eg, '/')
@app.route('/')
def home():
    return """<html>
    <head>
        <title>Hello, from Flask!</title>
    </head>
    <body>
        <h1>Hello, world!</h1>
        <hr />
        <p>Created by Vinod; powered by Flask</p>
    </body>    
</html>"""


if __name__ == '__main__':
    app.run(debug=True, port=8080)  # starts HTTP web server
