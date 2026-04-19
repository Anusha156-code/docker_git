from flask import Flask 
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello learning devops is easy but mastering need practice and patience and yes u will be on perfect path and ready..."
if __name__ == "__main__":
    app.run(host = "0.0.0.0" ,port= 5000)