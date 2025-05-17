from flask import Flask
from data.data_productos import productos, categorias

app = Flask(__name__)



@app.route("/")
def home():
    return "<h1>Hola soy Valentin Castrillo. Para poder ver los productos y categorias poner junto a la direccion  /productos o /categorias</h1>"

@app.route("/productos")

def lista_productos():
    salida = "<h1>Lista de productos</h1>"
    for producto in productos:
        salida += f"<p> Id: {producto['id']} - Descripcion: {producto['descripcion']}- id_categoria: {producto['categoria_id']} </p>"
    return salida

@app.route("/categorias")

def lista_categorias():
    salida = "<h1>Lista de categorias</h1>"
    for categoria in categorias:
        salida += f"<p>Id: {categoria['id']} - {categoria['descripcion']}</p>"
    return salida

if __name__ == "__main__":
    app.run(debug=True)


