#progama que elabore un programa que guarde una palabra secreta
#el usuario debe adivinar dicha palabra  secreta.
#el usuario solo tiene 3 turnos para adivinar la palabra secreta

print ("adivine la palabra secreta tiene 3 intentos")


secreta = "pepe"
secreta2 = "PEPE"
palabra = input("ingrese palabra")




if palabra == secreta or secreta2:
    print("correcto")

else:
    print("aproveche su segundo intento ingrese la palabra")
    palabra = input("ingrese palabra")

    if palabra == secreta or secreta2:
        print("correcto")


    else:
        print("aproveche su tercer intento ingrese la palabra")
        palabra = input("ingrese palabra")

        if palabra == secreta or secreta2:
            print("correcto")

        else:
            print("que va eres malo no advinaste en tu tres intentos")