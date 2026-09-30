from flask_app import app
from flask import render_template, session, redirect, request
from flask_app.models.usuario import Usuario


@app.route('/usuarios')
def usuarios():
    todos_usuarios = Usuario.get_all()

    return render_template('usuarios.html', todos_usuarios=todos_usuarios)

@app.route('/usuarios/crear', methods=['POST'])
def crear_usuario():
    data = {
        'nombre': request.form['nombre'],
        'email': request.form['email'],
        'password': request.form['password']
    }
    Usuario.save(data)
    return redirect('/usuarios')

@app.route('/usuarios/<int:id>')
def ver_usuario(id):
    usuario = Usuario.get_by_id(id)
    favoritos = Usuario.get_favoritos(usuario.id)
    return render_template('ver_usuario.html', usuario=usuario, favoritos=favoritos)

