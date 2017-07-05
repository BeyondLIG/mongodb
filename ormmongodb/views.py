from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {'db':'jikexueyuan'}

db = MongoEngine(app)



@app.route('/hello/')
def hello():
    print('hello world')


if __name__ == '__main__':
    app.run(debug=True)