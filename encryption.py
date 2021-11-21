key = 123
def encrypt(password):
    password = password.encode()
    password_array = bytearray(password)
    for index, value in enumerate(password_array):
        password_array[index] = value ^ key
    return password_array.decode()



def decrypt(password):
    password = password.encode()
    password_array = bytearray(password)
    for index, value in enumerate(password_array):
        password_array[index] = value ^ key
    return password_array.decode()

def add():
    name = input("Account Name: ")
    passwrd = input("Password: ")

    with open("password.txt","a") as file:
        passwrd = encrypt(passwrd)
        file.write(name+"|"+passwrd+"\n")

def view():
    with open("password.txt","r") as file:
        for lines in file.readlines():
            data = lines.rstrip()
            name, passwrd = data.split("|")
            passwrd = decrypt(passwrd)
            print("Name: "+name+"    Password: "+passwrd)


while True:
    mode = input("View/Add/Quit? ").lower()
    if (mode == "view"):
        view()
    elif (mode == "add"):
        add()
    elif (mode == "quit"):
        break
    else:
        continue