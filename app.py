from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        expression = request.form.get("expression", "")
        try:
            # Evaluate the expression safely
            result = str(eval(expression))
        except Exception:
            result = "Error"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
