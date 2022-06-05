calificacion = input("Introduce tu calificacion del AZ-900: ") #imprime y pide el puntaje de tu calificacion
calificacion = int(calificacion)#cambiamos el tipo de variable a entero

if calificacion < 700: #si el valor es menor
    print("No Obtuviste el puntaje para pasar") #si el valor es menor  a 700 se imprime esto
elif calificacion > 1000: #una nueva condicion por si es mayor a mil
    print("No es posible sacar mas de mil") #se imprime si es mayor a mil
else:#si ninguna de las dos anteiores se cumple se imprime esta
    print("Felicidades optuviste tu certificacion") #impresion por si no se cumple minguna de las anteriores

# Verificador de edad
edad = input("Introduce tu edad: ")#imprime y pide tu edad
edad = int(edad)#cambia el tipo de la variable a entero

if edad >= 18 and edad <= 100:#doble condicion por si es mayoro igual a 18 y si es menor o igual a 100
    print("Bienvenido al mamitas") #mesaje
elif edad > 100:#condicion si es mayor a 100
    print("Si vienes acompadado de tus abuelitos, si te podemos fiar")#mensaje
elif edad < 0:#condicion si es menor a 0
    print("Ni que fueras vijero del tiempo")#mensaje
else:#por si ninguna de las anteiores se cumple
    print("No puedes llevarte esos cigarros")#mensaje