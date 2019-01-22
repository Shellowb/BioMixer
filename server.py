from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/library")
def library():
    return render_template('library.html')

@app.route("/prepare")
def prepare():
    return render_template('prepare.html')

@app.route("/mixing")
def mixing():
    return render_template('mixing.html')

if __name__ ==  "__main__":
    app.run(debug = True, host = "0.0.0.0", port= 80)

