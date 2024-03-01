from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        countdown = request.form.get('countdown')
        return redirect(url_for('countdown', countdown=countdown))
    return render_template('index.html')

@app.route('/<int:countdown>')
def countdown(countdown):
    return render_template('countdown.html', countdown=countdown)

if __name__ == '__main__':
    app.run(debug=True)