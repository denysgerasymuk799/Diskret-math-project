from flask import Flask, render_template, request
from flask_app.RSA import decoder, encoder

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def input_profession():
    """
    Function for generating main web-page
    :return: rendered html template with decoded or encoded message
    """
    response_decoded = ""
    response_encoded = ""

    if request.method == 'POST':
        response = "Invalid input"
        simple_message = request.form['message0']
        encoded_message = request.form['message']

        if simple_message:
            try:
                p0 = int(request.form['p0'])
                q0 = int(request.form['q0'])
                e0 = int(request.form['e0'])
                if p0 * q0 < 255255:
                    raise ValueError
            except ValueError:
                return render_template("index.html", decoded=response, encoded=response)

        if encoded_message:
            try:
                p = int(request.form['p'])
                q = int(request.form['q'])
                e = int(request.form['e'])
                if p * q < 255255:
                    raise ValueError
            except ValueError:
                return render_template("index.html", decoded=response, encoded=response)

        if simple_message and p0 and q0 and e0:
            response_encoded = encoder(simple_message, p0, q0, e0)

        if encoded_message and p and q and e:
            response_decoded = decoder(encoded_message, p, q, e)

    return render_template("index.html", decoded=response_decoded, encoded=response_encoded)


if __name__ == '__main__':
    app.run(debug=True)
