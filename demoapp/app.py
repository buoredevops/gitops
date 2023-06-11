from flask import Flask
app = Flask(__name__)

@app.route('/')
def welcome():
    return {"message": "Welcome Home!"}


if __name__=="main":
    app.run()

