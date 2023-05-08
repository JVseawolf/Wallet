wallet = 0
movimiento = 0
newmovimiento = True
q_movimientos = 0

error = True
error_nick_reg = True
error_pass_reg = True
error_movimiento = True

usuarios_lista = ["Javier"]
usuarios_pass = ["1234"]
usuarios_saldo = [100]
usuarios_qmovimientos = [0]

def reg_user():
    usuarios_lista.append(new_user_nick)
    usuarios_pass.append(new_user_pass)
    usuarios_saldo.append(100)
    usuarios_qmovimientos.append(0)


print("\n¡Hola!")

while error:
    new_user = str(input("¿Ya tenés un usuario y contraseña?\n"))

    if new_user == "si":
        nick_login = str(input("\nIngrese su nombre de usuario\n"))
        if nick_login in usuarios_lista:
            pass_login = str(input("\nIngrese su contraseña.\n"))
            if pass_login == usuarios_pass[usuarios_lista.index(nick_login)]:
                print(f"\n¡Bienvenido {nick_login}!")
                error = False
            else:
                print("\nContraseña incorrecta.\n")
        else:
            print("\nEl usuario no existe.\n")
    elif new_user == "no":
        while error_nick_reg:
            new_user_nick = str(input("\n¡Bienvenido!\nIngrese un nuevo nombre de usuario.\n"))
            if new_user_nick not in usuarios_lista:
                error_nick_reg = False
                while error_pass_reg:
                    new_user_pass = str(input("\nEstablezca su contraseña\n"))
                    new_user_pass_chck = str(input("\nVuelva a escribir su contraseña\n"))
                    if new_user_pass_chck == new_user_pass:
                        reg_user()
                        error_pass_reg = False
                    else:
                        print("\nNo escribió la misma contraseña\n")
            else:
                print("\nEl usuario ya existe. Ingrese un nombre de usuario diferente.\n")

    else:
        print("\nEntrada incorrecta.\n")

while newmovimiento:
    if error_movimiento:
        print(f"los usuarios disponibles para realizar transferencias son {usuarios_lista}")
        usuario_dest = str(input("\nIngrese destinatario"))
        if usuario_dest not in usuarios_lista:
            print("\nEl usuario no existe")
        else:
            error_neg = True
            while error_neg:
                try:
                    movimiento = float(input("\nIngrese movimiento:\n"))
                except ValueError:
                    print("\nDebe ingresar un número.\n")
                    continue
                if movimiento < 0:
                    print("Solo puede enviar chapitas")
                else:
                    usuarios_saldo[usuarios_lista.index(usuario_dest)] += movimiento
                    usuarios_saldo[usuarios_lista.index(nick_login)] -= movimiento
                    if usuario_dest != nick_login:
                        usuarios_qmovimientos[usuarios_lista.index(nick_login)] += 1
                    newmovimiento = str(input("\nRealizar nuevo movimiento?\n"))
                    error_neg = False
    else:
        newmovimiento = str(input("\nRealizar nuevo movimiento?\n"))
    if newmovimiento == "si":
        error_movimiento = True
    elif newmovimiento == "no":
        newmovimiento = False
    else:
        error_movimiento = False
        print("\nEntrada incorrecta\n")


print(usuarios_lista)
print(usuarios_saldo)
print(usuarios_qmovimientos)


"""
print(f"\nel saldo de {nick_login} es de {wallet} chapitas\n")
print(f"movimientos realizados: {q_movimientos}")
"""



"""
print(type(wallet))
print(type(movimiento))
print(type(newmovimiento))
"""