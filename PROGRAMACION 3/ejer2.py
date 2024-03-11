def es_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
        return f"{anio} es un año bisiesto."
    else:
        return f"{anio} no es un año bisiesto."

def main():
    year = int(input("Ingrese un año: "))
    print(es_bisiesto(year))

main()