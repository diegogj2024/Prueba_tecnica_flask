from flask import Flask,request,render_template,redirect, url_for,session,flash
from model import db,Producto
import service

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin12345@localhost/prueba_tecnica'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/productos')
def productos():
    productos=service.obtener_productos()
    return render_template('/productos.html',productos=productos)

@app.route('/new_product')
def new_product():
    return render_template('newproduct.html')

@app.route('/guardar_producto', methods=['POST'])
def guardar_producto():
    nombre_producto=request.form['nombre_p']
    descripcion_producto=request.form['descripcion_p']
    nombre_laboratorio=request.form['nombre_lab']
    aviso=service.guardar_producto(nombre_producto,descripcion_producto,nombre_laboratorio)
    return render_template('newproduct.html',aviso=aviso)

@app.route('/formulario_editarproducto',methods=['POST'])
def formulario_editarproducto():
    codigo_producto=request.form['codigo_producto']
    producto_editar=service.obtener_producto_editar(codigo_producto)
    return render_template('actualizarproducto.html',producto_editar=producto_editar)

@app.route('/editar_producto', methods=['POST'])
def editar_producto():
    codigo=request.form['codigo_producto']
    nombre=request.form['nombre_p']
    descripcion=request.form['descripcion_p']
    estado_str=request.form['estado_p']
    estado = True if estado_str == 'True' else False
    laboratorio=request.form['nombre_lab']
    fecha=request.form['fecha_registro']
    aviso ,producto_editar=service.editar_producto(codigo,nombre,descripcion,estado,laboratorio,fecha)
    return render_template('actualizarproducto.html',aviso=aviso,producto_editar=producto_editar)
    
@app.route('/eliminar',methods=['POST'])
def eliminar():
    codigo=request.form['codigo_producto']
    service.eliminar_producto(codigo)
    productos=service.obtener_productos()
    return render_template('productos.html',productos=productos)

@app.route('/crear_proovedor')
def crear_proovedor():
    return render_template('crearproveedor.html')


@app.route('/guardar_proveedor', methods=['POST'])
def guardar_proveedor():
    tipo_doc=request.form['tipo_doc']
    numero_doc=request.form['numero_doc']
    nombre_proveedor=request.form['nombre_proveedor']
    direccion=request.form['direccion']
    nombre_contacto=request.form['nombre_contacto']
    celular_contacto=request.form['celular_contacto']
    actividad_economica=request.form['actividad_economina']
    aviso=service.guardar_proveedor(tipo_doc,numero_doc,nombre_proveedor,direccion,nombre_contacto,celular_contacto,actividad_economica)
    return render_template('crearproveedor.html',aviso=aviso)

    


if __name__ == '__main__':
    app.run(debug=True)