from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '<html><head><style>h1 { font-size: 48px; text-align: center; margin-top: 50px; } .container { display: flex; justify-content: center; align-items: flex-end; height: calc(100vh - 150px); } .square { width: 100px; height: 100px; background-color: red; animation: spin 2s linear infinite; } @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } } .footer { text-align: center; font-size: 24px; margin-top: 50px; }</style></head><body><h1>***** Rekruto! *****</h1><div class="container"><div class="square"></div></div><p class="footer">Кирилл Волосников</p></body></html>'

@app.route('/x')
def hello():
    name = request.args.get('name')
    message = request.args.get('message')
    return f'Hello {name}! {message}!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
