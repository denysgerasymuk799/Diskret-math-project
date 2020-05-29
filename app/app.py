from flask import Flask, render_template, request
from app.RSA import decoder

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def input_profession():
    """
    Function for generating main web-page
    :return: rendered html template
    """
    response = ""
    if request.method == 'POST':
        response = "Invalid input"
        message = request.form['message']
        try:
            p = int(request.form['p'])
            q = int(request.form['q'])
            e = int(request.form['e'])
        except ValueError:
            return render_template("index.html", decoded=response)
        if message and p and q and e:
            response = decoder(message, p, q, e)
    return render_template("index.html", decoded=response)

