from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    name = request.args.get("name", "Hacker")

    # ❗ Vulnerable: untrusted input directly passed into the template
    template = f"<h1>Hello {name}!</h1>"
    return render_template_string(template)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
