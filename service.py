from model import db, Producto,Proveedor,RecepcionProductos
from app import app
from datetime import datetime

def guardar_producto(nombre_producto,descripcion_producto,nombre_laboratorio):
        try:
            new_producto=Producto(
                nombre=nombre_producto,
                descripcion=descripcion_producto,
                nombre_laboratorio=nombre_laboratorio
            )
            db.session.add(new_producto)
            db.session.commit()
            return "Producto creado exitosamente"
        except Exception as e:
            return ("El Producto no pudo crear "+ e)
        
def obtener_productos():
    Productos=Producto.query.all()
    return Productos

def obtener_producto_editar(codigo_producto):
    producto_editar=Producto.query.filter_by(codigo=codigo_producto).first()
    return producto_editar


def editar_producto(codigo,nombre,descripcion,estado,nombre_lab,fecha):
    producto_editar=Producto.query.filter_by(codigo=codigo).first()
    fecha_obj = datetime.strptime(fecha, '%Y-%m-%d').date()
    try:
        producto_editar.nombre=nombre
        producto_editar.descripcion=descripcion
        producto_editar.estado=estado
        producto_editar.nombre_laboratorio=nombre_lab
        producto_editar.fecha_registro=fecha_obj
        db.session.commit()
        return "se edito exitosamente",producto_editar
    except Exception as e:
        return "error",producto_editar

def eliminar_producto(codigo):
     producto=Producto.query.filter_by(codigo=codigo).first()
     db.session.delete(producto)
     db.session.commit()


def guardar_proveedor(tipo_doc,numero_doc,nombre_proveedor,direccion,nombre_contacto,celular_contacto,actividad_economica):
    try:
        new_proveedor=Proveedor(
            numero_identificacion=numero_doc,
            tipo_identificacion=tipo_doc,
            nombre_proveedor=nombre_proveedor,
            direccion=direccion,
            nombre_contacto=nombre_contacto,
            celular_contacto=celular_contacto,
            actividad_economica=actividad_economica
        )
        db.session.add(new_proveedor)
        db.session.commit()
        return "Provedor creado exitosamente"
    except Exception as e:
        return "error"
    
def obtener_proveedores():
    proveedores=Proveedor.query.all()
    return proveedores

def obtener_editar_proveedor(numero_identificacion):
    proveedor=Proveedor.query.filter_by(numero_identificacion=numero_identificacion).first()
    return proveedor

def editar_proveedor(tipo_iden,numero_iden,nombre_proveedor,direccion,nombre_contacto,celular_contacto,actividad_economica):
    proveedor_editar=Proveedor.query.filter_by(numero_identificacion=numero_iden).first()
    
    try:
        if len(celular_contacto) > 20:
            return "error: el número de celular no puede tener más de 20 caracteres", proveedor_editar
        else:
            proveedor_editar.tipo_identificacion=tipo_iden
            proveedor_editar.nombre_proveedor=nombre_proveedor
            proveedor_editar.direccion=direccion
            proveedor_editar.nombre_contacto=nombre_contacto
            proveedor_editar.celular_contacto=celular_contacto
            proveedor_editar.actividad_economica=actividad_economica
            db.session.commit()
            return "se edito exitosamente", proveedor_editar 
    except Exception as e:
        db.session.rollback()
        return "error", proveedor_editar
    
def eliminar_proveedor(numero_identificacion):
    proveedor=Proveedor.query.filter_by(numero_identificacion=numero_identificacion).first()
    db.session.delete(proveedor)
    db.session.commit()