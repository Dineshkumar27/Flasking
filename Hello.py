from flask import Flask, render_template, url_for, flash,redirect

from forms import Registrationform,Loginform
app = Flask(__name__)
app.config['SECRET_KEY']='6a6bed92766c1a7fe4a48e1c6c1aa564'
posts=[
    {
        'author':'Dinesh Kumar',
        'title':'Python flask',
        'content':'First post content',
        'date_posted':'July 8, 2020'
    },
{
        'author':'Ranjan Sha',
        'title':'Python Django',
        'content':'First Django Conent Blog',
        'date_posted':'July 9, 2020'
    }
]
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=posts)


@app.route('/about')
def about():
    return render_template('about.html',title="About us")

@app.route('/register',methods=['GET','POST'])
def register():
    form=Registrationform()
    if form.validate_on_submit():
        flash(f'Account Created for the user {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title="Registration",form=form)


@app.route('/login',methods=['GET','POST'])
def login():
    form=Loginform()
    if form.validate_on_submit():
        if form.email.data=='dkumar.270985@gmail.com' and form.password.data=='dinesh1342':
            flash(f'Welcome {form.email.data}!!','success')
            return redirect(url_for('home'))
        else:
            flash('Check your username and password', 'danger')


    return render_template('login.html',title="Registration",form=form)

if __name__=='__main__':
    app.run(debug=True)



