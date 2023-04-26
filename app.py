from flask import Flask , render_template # """ importa classe flasc """

app = Flask ("__name__") #""" cria uma insnância dessa classe """

@app.route("/")          #""" cria rotas com o decorator """
def home():
    return render_template ("/pag1.html")

@app.route("/quemsomos")          
def quemsomos():
    return render_template ("/pag2.html")

@app.route("/contatos")          
def contatos():
    return render_template ("/pag3.html") 