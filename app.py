print("Bienvenido al Horóscopo")
user_option = ""

while user_option != "exit":
    print("###############################")
    print("Selecciona el número correspondiente a tu signo")
    print("1 Acuario")
    print("2 Aries")
    print("3 Cancer")
    print("4 Capricornio")
    print("5 Geminis")
    print("6 Leo")
    print("7 Libra")
    print("8 Piscis")
    print("9 Sagitario")
    print("10 Escorpión")
    print("11 Tauro")
    print("12 Virgo")
    print("13 Color de la suerte")
    print("0 Salir")
    print("###############################")

    user_option =input()

def read_file(file_name):
    file = open("signs/" + file_name, "r", encoding="UTF-8")
    for line in file:
        print(line)

while user_option !="exit":
    menu()
    user_input = input()
    if user_option == "1":
        file = open("signs/aquarius.txt", "r")
        for line in file:
            print(line)
    elif user_option == "2":
        file = open("signs/aries.txt", "r")
        for line in file:
            print(line)
    elif user_option == "3":
        file = open("signs/cancer.txt", "r")
        for line in file:
            print(line)
    elif user_option == "4":
        file = open("signs/capricornus.txt", "r")
        for line in file:
            print(line)
    elif user_option == "5":
        file = open("signs/gemini.txt", "r")
        for line in file:
            print(line)
    elif user_option == "6":
        file = open("signs/leo.txt", "r")
        for line in file:
            print(line)
    elif user_option == "7":
        file = open("signs/libra.txt", "r")
        for line in file:
            print(line)
    elif user_option == "8":
        file = open("signs/pisces.txt", "r")
        for line in file:
            print(line)
    elif user_option == "9":
        file = open("signs/sagittarius.txt", "r")
        for line in file:
            print(line)
    elif user_option == "10":
        file = open("signs/scorpio.txt", "r")
        for line in file:
            print(line)
    elif user_option == "11":
        file = open("signs/taurus.txt", "r")
        for line in file:
            print(line)
    elif user_option == "12":
        file = open("signs/virgo.txt", "r")
        for line in file:
            print(line)
    elif user_option == "13":
        file = open("tu-color-de-la-suerte.txt", "r")
        for line in file:
            print(line)
    elif user_option == "0":
        file = open("exit")
        for line in file:
            print(line)
    else:
        print("opción incorrecta")