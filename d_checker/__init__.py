from flask import Flask

app = Flask(__name__)
app.secret_key = "masmdamdasmdas214"

from d_checker import routes
