import os
from datetime import datetime
import json

class Users:
    def __init__(self, username, password, balance = 100, num_movements = 0):
        self.username = username
        self.password = password
        self.balance = balance
        self.num_movements = num_movements

my_user = {}
registered_users = {}

def movement_json(new_username, receiver = None, amount = 0):
    registered_users = json.load(open("Wallet/balance_json.json"))
    registered_users[new_username] = registered_users[new_username] - amount
    registered_users[receiver] = registered_users[receiver] + amount
    new_json = open("Wallet/balance_json.json", "w+")
    json.dump(registered_users, new_json, indent = 2)
    new_json.close()

def balance_json(new_username):
    new_json = open("Wallet/balance_json.json", "w+")
    registered_users[my_user[new_username].username] = my_user[new_username].balance
    json.dump(registered_users, new_json, indent = 2)
    new_json.close

def register_user():
    print("¡Bienvenido!")
    while True:
        try:
            registered_users = json.load(open("Wallet/balance_json.json"))
        except:
            new_json = open("Wallet/balance_json.json", "w+")
            json.dump({}, new_json, indent = 2)
            new_json.close()
            registered_users = json.load(open("Wallet/balance_json.json"))
        finally:
            while True:
                new_username = input("Ingrese su nombre de usuario")            
                if new_username not in registered_users:
                    while True:
                        new_password = input("Ingrese su contraseña")
                        password_confirm = input("Confirme su contraseña")
                        if new_password == password_confirm:
                            my_user[new_username] = Users(new_username, new_password)
                            balance_json(new_username)
                            print("Registro exitoso")
                            log_write("reg", new_username)
                            break
                        else:
                            print("Las contraseñas no coinciden")
                    break       
                else:
                    print("El usuario ya existe. Ingrese un nombre de usuario diferente")
            break
def login_user():
    while True:
        username = input("Ingrese su nombre de usuario")
        if username in registered_users:
            while True:
                password = input("Ingrese su contraseña")
                if password == my_user[username].password:
                    print(f"¡Bienvenido {username}!")
                    log_write("login", username)
                    return username
                    break
                else:
                    print("Contraseña incorrecta")
            break
        else:
            print("Usuario inexistente")

def make_movement(sender, receiver, amount):
    if amount < 0:
        print("Solo puede enviar chapitas")
    elif my_user[sender].balance < amount:
        print("No dispone de saldo suficiente en su cuenta")
    else:
        my_user[sender].balance -= amount
        registered_users[sender] = registered_users[sender] - amount
        registered_users[receiver] = registered_users[receiver] + amount
        my_user[sender].num_movements += 1
        movement_json(sender, receiver, amount)
        print("Movimiento realizado con éxito")
        log_write("movement", sender, amount, receiver)
        
def users_display(actual_user):
    print("Usuarios disponibles para transferencia:")
    for username in registered_users:
        if username != actual_user:
            print(username)

def users_info_display():
    for username in my_user:
        print(username, my_user[username].balance, my_user[username].num_movements)

def current_time():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return dt_string

def log_write(log_operation, log_user, log_amount = 0, log_receiver = None):
    if log_operation == "reg":
        wallet_log = open("Wallet/wallet_log.txt", "a")
        wallet_log.write(f"\n{current_time()}\nSe registró el usuario {log_user}.")
        wallet_log.close
    elif log_operation == "login":
        wallet_log = open("Wallet/wallet_log.txt", "a")
        wallet_log.write(f"\n{current_time()}\n{log_user} inció sesión.")
        wallet_log.close
    elif log_operation == "movement":
        wallet_log = open("Wallet/wallet_log.txt", "a")
        wallet_log.write(f"\n{current_time()}\n{log_user} envió {log_amount} chapitas a {log_receiver}")
        wallet_log.close
    elif log_operation == "exit":
        wallet_log = open("Wallet/wallet_log.txt", "a")
        wallet_log.write(f"\n{current_time()}\n{log_user} cerró su sesión")
        wallet_log.close

def main():
    print("¡Hola!")
    terminate = True
    while terminate == True:
        while True:
            existing_user = input("Ya tienes un usuario y contraseña (si/no)")
            if existing_user.lower() == "si":
                user = login_user()
                if user:
                    break
            elif existing_user.lower() == "no":
                register_user()
            else:
                print("Entrada incorrecta")

        while True:
            next_operation = input("Elija una operación\n1 - Transferir chapitas\n2 - Salir")
            if next_operation == "1":
                while True:
                    users_display(user)
                    receiver = input("Indique el destinatario de la transferencia")
                    if receiver not in my_user:
                        print("Usuario de destino inexistente")
                    elif receiver == user:
                        print("No puede realizar una transeferencia a su propia cuenta")
                    else:
                        amount = float(input("Indique la cantidad de chapitas a transferir"))
                        make_movement(user, receiver, amount)
                        new_movement = input("¿Desea realizar un nuevo movimiento? (si/no)")
                        if new_movement == "no":
                            break
                        elif new_movement != "si" and new_movement != "no":
                            print("Entrada incorrecta")
            elif next_operation == "2":
                users_info_display()
                log_write("exit", my_user[user].username)
                break
            elif next_operation == "end":
                terminate = False
                break
            else:
                print("Entrada incorrecta")

if __name__ == "__main__":
    main()
