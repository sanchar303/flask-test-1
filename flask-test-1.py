from flask import *

vHost = "192.168.100.56"
vPort = 8081
app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/biodata")
def biodata():
    return render_template("biodata.html")

@app.route("/family")
def family():
    return render_template("family.html")

@app.route("/best_places")
def best_places():
    return render_template("best_places.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(port=vPort,host=vHost,debug=True)
