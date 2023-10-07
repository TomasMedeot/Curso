from flask import * 
'''
from flask import *
de flask (la libreria) importar * (todo)

flask con f minuscula es el conjunto de archivos que hacen a flask
'''
servidor = Flask("server") #Flask con F mayucula es el objeto

@servidor.route("/", methods=['GET'])
def main():
    return redirect("/saludo")

@servidor.route("/saludo", methods=['GET','POST'])
def saludo():
    if request.method == 'GET':
        return {"saludo":"hola"}
    elif request.method == 'POST':
        data = request.get_json()
        print(data["nombre"])
        return {"saludo":"chau"}

if __name__ == "__main__":
    servidor.run(debug=True, host="localhost", port=5000)