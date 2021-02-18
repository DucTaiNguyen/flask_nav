from flask import Flask, render_template
from flask_nav import Nav
from flask_nav.elements import Navbar, Subgroup, View, Link, Text, Separator
app = Flask(__name__)
nav = Nav(app)

nav.register_element('my_navbar',Navbar(
    'thenav',
    View('Home Page','index'),
    View('Logout', 'logout',),
    View('Login', 'login',),
    View('Admin', 'admin',),
    Link('Google','https://www.google.com'),
    Subgroup('Extras',
        Link('Yahooo','https://www.yahoo.com'),
        View('index','index')


    )))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/login', methods=('GET', 'POST'))
def login():
    return render_template('login.html')






if __name__=='__main__':
    app.run(debug=True)