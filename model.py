from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Proveedor(db.Model):
    __tablename__ = 'proveedor'
    numero_identificacion = db.Column(db.String(20), primary_key=True, unique=True)
    tipo_identificacion = db.Column(db.String(100), nullable=True)
    nombre_proveedor = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(200), nullable=True)
    nombre_contacto = db.Column(db.String(100), nullable=False)
    celular_contacto = db.Column(db.String(20), nullable=True)
    actividad_economica = db.Column(db.Integer, nullable=True)
    productos = db.relationship('Producto', secondary='producto_proveedor', back_populates='proveedores')

class Producto(db.Model):
    __tablename__ = 'producto'
    codigo = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True )
    nombre = db.Column(db.String(40), nullable=True)
    descripcion = db.Column(db.String(200), nullable=True)
    estado = db.Column(db.Boolean, default=True)
    nombre_laboratorio = db.Column(db.String(50), nullable=True)
    fecha_registro = db.Column(db.Date, default=datetime.utcnow)
    proveedores = db.relationship('Proveedor', secondary='producto_proveedor', back_populates='productos')
    recepciones = db.relationship('RecepcionProductos', back_populates='producto')

producto_proveedor = db.Table(
    'producto_proveedor',
    db.Column('producto_codigo', db.Integer, db.ForeignKey('producto.codigo'), primary_key=True),
    db.Column('proveedor_id', db.String(20), db.ForeignKey('proveedor.numero_identificacion'), primary_key=True)
)

class RecepcionProductos(db.Model):
    __tablename__ = 'recepcionproductos'
    numero_factura = db.Column(db.String(50), primary_key=True)
    fecha_recepcion = db.Column(db.DateTime, default=datetime.utcnow)
    producto_codigo = db.Column(db.Integer, db.ForeignKey('producto.codigo'), nullable=False)
    proveedor_id = db.Column(db.String(20), db.ForeignKey('proveedor.numero_identificacion'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    lote = db.Column(db.String(50), nullable=True)
    registro_invima = db.Column(db.String(50), nullable=True)
    fecha_vencimiento = db.Column(db.Date, nullable=True)
    estado_presentacion = db.Column(db.Text, nullable=True)
    producto = db.relationship('Producto', back_populates='recepciones')
    proveedor = db.relationship('Proveedor')

