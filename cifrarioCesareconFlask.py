from flask import Flask, render_template, request

app = Flask(__name__)

def cifrario_di_cesare(parola, chiave):
    parola_cifrata = ""
    for carattere in parola:
        if carattere.isalpha():
            valore_cifrato = ord(carattere) + chiave
            if carattere.isupper():
                if valore_cifrato > ord('Z'):
                    valore_cifrato -= 26
            else:
                if valore_cifrato > ord('z'):
                    valore_cifrato -= 26
            parola_cifrata += chr(valore_cifrato)
        else:
            parola_cifrata += carattere
    return parola_cifrata

@app.route('/', methods=['GET', 'POST'])
def index():
    parola_cifrata = ""
    if request.method == 'POST':
        parola = request.form['parola']
        try:
            chiave = int(request.form['chiave'])
            parola_cifrata = cifrario_di_cesare(parola, chiave)
        except ValueError:
            error_message = "La chiave di cifratura deve essere un numero intero."
            return render_template('index.html', error_message=error_message)
    return render_template('index.html', parola_cifrata=parola_cifrata)

if __name__ == '__main__':
    app.run(debug=True)
