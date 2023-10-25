from flask import Flask, request, make_response, render_template, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Chiave segreta per firmare la sessione


@app.route('/')
def index():
    username = session.get('username')
    last_access = session.get('last_access')
    if username:
        last_access = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        session['last_access'] = last_access
        return f'Ciao {username}! Ultimo accesso: {last_access}'
    else:
        return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    if username:
        session['username'] = username
        session['last_access'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return f'Login effettuato come {username}.'
    else:
        return 'Nome utente mancante. Impossibile effettuare il login.'


if __name__ == '__main__':
    app.run()