import os 
from forms import AddForm
from flask import Flask, render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = '$33etwtrtwt!@@989'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///' + os.path.join(basedir,'datatest.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 


db=SQLAlchemy(app)
Migrate(app,db)

##Database Model

class Interestlist(db.Model):

    __tablename__ = 'interestlist'

    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.Text)
    state=db.Column(db.Text)
    city=db.Column(db.Text)
    phonenumber=db.Column(db.Integer)

    def __init__(self,email,state, city, phonenumber):
        self.email=email
        self.state=state
        self.city=city
        self.phonenumber=phonenumber



@app.route('/',methods=['GET','POST'])
def index():
    form=AddForm()
    
    if form.validate_on_submit():
        email=form.email.data
        state=form.state.data
        city=form.city.data
        phonenumber=form.phonenumber.data

        new_member=Interestlist(email=email, state=state, city=city, phonenumber=phonenumber)
        db.session.add(new_member)
        db.session.commit()

        return redirect(url_for('thankyou'))

    return render_template('index.html',form=form)

@app.route('/list')
def list():
    interestlist=Interestlist.query.all()
    return render_template('list.html',interestlist=interestlist)

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ =='__main__':
    app.run()