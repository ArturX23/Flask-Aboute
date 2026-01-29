from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def mypage():
    return render_template("form.html")


@app.route("/me", methods=['GET'])
def me():
    return render_template("me.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        text = request.form["message"]
        print("Masz wiadomość:", text)
    return render_template("contact.html")


