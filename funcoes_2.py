def loginUsuario(perfil):
    if perfil.lower() == 'admin':
        print("olá, administrador!")
    else:
        print("olá, usuário!")

loginUsuario('Admin')
loginUsuario('admin')
loginUsuario('User')
loginUsuario('usuário')
loginUsuario('etc')