#  Interes compuesto

# input
c = int(input("Ingresa tu capital : "))

# Processing
a = 2 * c
m = 0

while c<a:
    c = c + 0.05*c
    m = m+1
print("el mes es:" + str(m))