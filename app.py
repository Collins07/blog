from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm


app = Flask(__name__)
app.config.from_pyfile('config.py')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)


posts = [
    {
        'author':'Collins Nyakoe',
        'title':'Blog1',
        'content':'Software Development',
        'date_posted':'April 27 2022'
    },
    {
        'author':'Abaya Nyakoe',
        'title':'Blog2',
        'content':'Data Science',
        'date_posted':'April 27 2022'
    }
]




@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About') 


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'{ form.username.data} your account has been created', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form=form)


@app.route('/login',methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'mynamecollins@gmail.com' and form.password.data == 'password':
            flash('Successfully logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Log In Unsuccessful!', 'danger')    
    return render_template('login.html', form=form) 





if __name__ == '__main__':
    app.run(debug = True)    