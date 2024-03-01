from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        countdown_minutes = int(request.form.get('countdownminuts'))
        countdown_seconds = int(request.form.get('countdownsegons'))
        end_time = datetime.now() + timedelta(minutes=countdown_minutes, seconds=countdown_seconds)
        return redirect(url_for('countdown', end_time=end_time.timestamp()))
    return render_template('index.html')

@app.route('/<float:end_time>')
def countdown(end_time):
    end_time = datetime.fromtimestamp(end_time)
    remaining_time = end_time - datetime.now()
    minutes = remaining_time.seconds // 60
    seconds = remaining_time.seconds % 60
    return redirect(url_for('countdown', end_time=end_time.timestamp()))    
if __name__ == '__main__':
    app.run(debug=True)