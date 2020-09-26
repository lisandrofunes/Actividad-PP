hsa = float(input("Ingrese la hora de salida\n"))
hlle = float(input("Ingrese las horas de vuelo\n"))
hdif = float(input("Ingrese la diferencia horaria\n"))
total = 0 ;
total = hsa + hlle + hdif

while total > 24:
    total = total - 24
print(total , "Hs")
