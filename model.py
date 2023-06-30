from app2 import app, db    


class Producto(db.Model):  # Producto hereda de db.Model

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    precio = db.Column(db.Integer)
    stock = db.Column(db.Integer)
    imagen = db.Column(db.String(400))

    def __init__(self, nombre, precio, stock, imagen):

        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.imagen = imagen

with app.app_context():
    db.create_all()  # Crea todas las tablas en la base de datos