import flask
import json

app = flask.Flask(__name__)

@app.route('/')
def home():
    print('home')
    return flask.render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
