from flask import Flask, request, session, redirect, url_for, render_template
import random

app = Flask(__name__)
app.secret_key = 'geheim123'  # Nodig voor sessies

@app.route('/', methods=['GET', 'POST'])
def raad_het_getal():
    if 'geheim' not in session:
        session['geheim'] = random.randint(1, 100)

    boodschap = ""

    if request.method == 'POST':
        if 'gok' in request.form and request.form['gok']:  # veilige check
            gok = int(request.form['gok'])

            if gok < session['geheim']:
                boodschap = "Hoger!"
            elif gok > session['geheim']:
                boodschap = "Lager!"
            else:
                boodschap = "Proficiat! Je hebt het getal geraden."
                session.pop('geheim', None)  # spel opnieuw starten

    return render_template('raad.html', boodschap=boodschap)

if __name__ == '__main__':
    app.run(debug=True)
