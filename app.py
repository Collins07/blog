from flask import Flask, render_template, url_for


app = Flask(__name__)
app.config.from_pyfile('config.py')
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




if __name__ == '__main__':
    app.run(debug = True)    