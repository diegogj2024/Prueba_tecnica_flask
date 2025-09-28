from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Proveedor(db.Model):
    __tablename__ = 'proveedor'
    numero_identificacion = db.Column(db.String(20), primary_key=True, unique=True, nullable=False)
    tipo_identificacion = db.Column(db.String(100), nullable=False)
    nombre_proveedor = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(200), nullable=False)
    nombre_contacto = db.Column(db.String(100), nullable=False)
    celular_contacto = db.Column(db.BigInteger, nullable=False)
    actividad_economica = db.Column(db.Integer, nullable=False)

class Producto(db.Model):
    __tablename__ = 'producto'
    codigo = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True, nullable=False)
    nombre = db.Column(db.String(40), nullable=False)
    descripcion = db.Column(db.String(200), nullable=False)
    estado = db.Column(db.Boolean, default=True, nullable=False)
    nombre_laboratorio = db.Column(db.String(50), nullable=False)
    fecha_registro = db.Column(db.Date, default=datetime.utcnow, nullable=False)
    recepciones = db.relationship('RecepcionProductos', back_populates='producto')

class RecepcionProductos(db.Model):
    __tablename__ = 'recepcionproductos'
    numero_factura = db.Column(db.String(50), primary_key=True, nullable=False)
    fecha_recepcion = db.Column(db.Date, default=datetime.utcnow, nullable=False)
    producto_codigo = db.Column(db.Integer, db.ForeignKey('producto.codigo'), nullable=False)
    proveedor_id = db.Column(db.String(20), db.ForeignKey('proveedor.numero_identificacion'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    lote = db.Column(db.String(50), nullable=False)
    registro_invima = db.Column(db.String(50), nullable=False)
    fecha_vencimiento = db.Column(db.Date, nullable=False)
    estado_presentacion = db.Column(db.Text, nullable=False)
    producto = db.relationship('Producto', back_populates='recepciones')
    proveedor = db.relationship('Proveedor')
