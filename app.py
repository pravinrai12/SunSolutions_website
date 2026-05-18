from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "SunSolutions_solar_secret_key"  # Required for flashing messages


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # In a real production app, you would send an email or save to a DB here
        name = request.form.get("name")
        email = request.form.get("email")

        flash(
            f"Thank you, {name}! Your message has been sent successfully. We will contact you at {email} soon.",
            "success",
        )
        return redirect(url_for("contact"))
    return render_template("contact.html")


if __name__ == "__main__":
    import os

    # This tells the app to use the port Render provides, or 5000 locally
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
