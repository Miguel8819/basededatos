print ("Hola, mundo")
print ("\n")

numero1=4
numero2=2
resultado=numero1+numero2
resultado=str(resultado)
print ("El resultado de la suma es: "+resultado)
print ("\n")

precio=100
iva=(precio*21)/100
total= precio+iva
print ("El iva es: "+ str (iva))
print ("El total con iva es: "+ str (total))
print ("\n")

print ("Ingresa dos numeros:")
n1=int(input("Numero 1: "))
n2=int(input("Numero 2: "))
if n1==n2:
    print ("Los dos numeros son iguales")
elif n1>n2:
    print ("El Numero 1 es mayor")
else:
    print ("El Numero 2 es mayor")  

print ("\n")

print("Ingresa un numero")
Numero=int(input("Numero :"))
if Numero>=0 and Numero<=10:
    print ("El numero ingresado esta entre 0 y 10")
elif Numero>=11 and Numero<=20:
    print ("El numero ingresado esta entre 11 y 20")
elif Numero>=21 and Numero<=30:
    print ("El numero ingresado esta entre 21 y 30")
else:
    print ("Fin")
    print ("\n")
    
n=1
while n<=100:
    print (n,end=",")
    n=n+1
  
for numero in range (100):
    print (numero+1, end=",")
    

