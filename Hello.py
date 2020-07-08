from flask import Flask,render_template
app = Flask(__name__)

posts=[
    {
        'author':'Dinesh Kumar',
        'title':'Python flask',
        'content':'First post content',
        'date_posted':'July 8, 2020'
    }
]
@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('home.html',posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__=='__main__':
    app.run(debug=True)



