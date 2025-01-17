from flask import Flask,render_template,request,redirect,url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_HOST"]="138.41.20.102"
app.config["MYSQL_PORT"]="53306"
app.config["MYSQL_USER"]="ospite"
app.config["MYSQL_PASSWORD"]="ospite"
app.config["MYSQL_DB"]="w3schools"

mysql=MySQL(app)


@app.route("/")   # lo slash qui dice il nome della risorsa per aprirla sul tipo web
def home():   #definisce una funzione
    return render_template("home.html",titolo="Home") #ritorna il file html e il titolo è quello della scheda

@app.route("/registrati",methods=["GET","POST"])
def register():
    if request.method=="GET":
        return render_template("register.html",titolo="Register") 
    else: 
        nome=request.form.get("nome") #si riferisce al nome nel campo name dell'input form
        cognome=request.form.get("cognome")
        username=request.form.get("username")
        password=request.form.get("password")
        cpassword=request.form.get("cpassword")

        if nome=="" or cognome=="" or username=="" or password=="" or cpassword=="": 
            return render_template("register.html",errore="campo non valido")
        else:
            if password!=password:
                return render_template("register.html",errore="password diverse")
            
        cursor=mysql.connection.cursor()

        #query che controlla username
        select="SELECT username FROM users WHERE username =%s"

    

@app.route("/login")
def login():
    return render_template("login.html",titolo="Login")

@app.route("/personale")
def personale():
    return render_template("personale.html",titolo="Personale")



app.run()
