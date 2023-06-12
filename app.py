from flask import Flask, render_template, request, Response


app = Flask(__name__)


@app.route("/",methods=['GET'])
def index_get():
    return render_template('index.html')

@app.route("/takeuchi", methods=['GET'])
def takeuchi_get():
    return render_template('5431.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)