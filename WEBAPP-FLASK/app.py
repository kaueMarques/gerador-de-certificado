from flask import Flask, render_template


app = Flask(__name__)

@app.route('/') 
def hl():
    return render_template('index.html')

@app.route('/verificar/<string:cod>')
def hl2(cod):
    return f"O código {cod} é valido pertence a Joãozinho"

if __name__ == "__main__":
        app.run(debug=True)