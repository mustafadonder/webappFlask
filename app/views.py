from flask import Flask,render_template,redirect,url_for,request, make_response, session,abort
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # burada kullanıcı adı ve şifre ile giris yapiliyor

        return redirect(url_for('loggedin'))
    return render_template('login.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # burada mesajı e-posta yoluyla göndermemizi sagliyor
        return redirect(url_for('thankyou'))
    return render_template('contact.html')

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')
    # başarılı bir mail gonderimi yaptıktan sonra, tesekkurler mesaji donduruyor

@app.route('/logged in')
def loggedin():
    return render_template('logged in.html')