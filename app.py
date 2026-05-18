from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "SunSolutions_solar_secret_key"  # Required for flashing messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # In a real production app, you would send an email or save to a DB here
        name = request.form.get('name')
        email = request.form.get('email')
        
        flash(f"Thank you, {name}! Your message has been sent successfully. We will contact you at {email} soon.", "success")
        return redirect(url_for('contact'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)