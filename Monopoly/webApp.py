from flask import Flask, render_template, request, session, url_for, redirect
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from mmysql import get_customers, get_tables, get_mysql_uri
import mmysql
'''
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
'''

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

#    users = [ 'Rosalia','Adrianna','Victoria' ]
#    return users


@app.route('/classicmodels')
def get_costomers(): 
     get_session = sessionmaker(bind=create_engine(get_mysql_uri()))
     session = get_session()
     customers = get_customers(session)
     customer_list =(c for c in customers)
     
     output = "<HEAD>"
     output += "    <link href='file:./web.css' rel='stylesheet'>"
     output += "</HEAD>"
     output += "<BODY>"
     output += "<H1>Customers</H1>"

     output += "<TABLE>"
     for c in customer_list:
         output += "<TR>"
         for f in c:
             output += "<TD background-color ='aquamarine'>" +str(f) + "</TD>"
         output += "</TR>"           
     output += "</TABLE>"
     output += "</BODY>"
     
     return(output)

@app.route('/classicmodels/tables')
def get_tables():
     get_session = sessionmaker(bind=create_engine(get_mysql_uri()))
     session = get_session()
     output = mmysql.get_tables(session)
     outputstr = ""
     for i in output:
         outputstr += str(i[0]) + ' '

     outputstrlist = outputstr.split()
     newoutputstr = "<LIST>"
     for t in outputstrlist:
       newoutputstr += ("<LI>" + str(t)  + "</LI>")

     newoutputstr += "</LIST>"
   
     return newoutputstr
     
@app.route("/login", methods=["GET", "POST"])
def login():
    """Route used for login purpose"""
    if request.method == "GET":
        return render_template("login.html")
    if "user_id" in session:
        return redirect(url_for("index"))
        
    # getting input
    email = request.form.get("email")
    password = request.form.get("password")
    # validate input
    if email is None or password is None:
        return render_template("login.html", error="Please fill all fields"), 400
#    user_data = user.login(email, password)
    print(email, password)
    print(f'Logging {email} with {password}')
#    if user_data is None:
#        return render_template("login.html", error="Invalid email or password"), 403
    # saving session
#    session["user_id"] = user_data[0]
#    session["user_name"] = user_data[1]
    return redirect(url_for("index"))

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if "user_id" in session:
        return redirect(url_for("index"))

    if request.method == "GET":
        return render_template("register.html")
    # loading input from form
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    print(name)
    # validating input
    if name is None or password is None or email is None:
        return render_template("register.html", error="Please fill all fields"), 400

    # check for email already exists
    if user.is_email_exists(email) is not None:
        return render_template("register.html", error="Email already exists"), 403

    user_data = user.register(name, email, password)
    if user_data is None:
        return render_template("register.html", error="Could not add user"), 403

    session["user_id"] = user_data[0]
    session["user_name"] = user_data[1]
    return redirect(url_for("index"))
     
def DBconnect():
   print('trying connection')
   app.run(host='127.0.0.1', port=5001, debug=True)

if __name__ == "__main__":
    DBconnect()
    run()
'''
def on_activate(app):
    win = Gtk.ApplicationWindow(application=app)
    btn1 = Gtk.Button(label="Executive")
    btn1.connect('clicked', lambda x: win.destroy())
    win.add(btn1)
    btn2 = Gtk.Button(label="Executive")
    btn2.connect('clicked', lambda x: print("not implemented"))
    win.add(btn2)
    btn3 = Gtk.Button(label="Executive")
    btn3.connect('clicked', DBconnect)
    win.add(btn3)
    win.show_all()

app = Gtk.Application(application_id='org.gtk.Example')
app.connect('activate', on_activate)
app.run()

'''