####################DICCIONARIOS AUTOMATICOS########################
pruebas = {}

counter = 0
valores = [4618, 4257, 4691, 4393, 4359, 4619, 4249, 4923, 4899, 5260, 4620]

for i in valores:
    counter +=1
    name= 'valor-'+str(counter)
    pruebas[name]= i

print(pruebas)
#############################################################

#Descomponer urls en porciones#
valor1 = 'http://mi-domino.com/sub-slug-1/'

clean1 = valor1.rstrip('/')

raw1 = clean1.replace('http://', '').replace('https://', '')

rawsplit = raw1.split("/")

print(rawsplit[1])
###########################################################


#Colocar la priemra letra en mayusculas de una cadena de texto tipo slug url#
text = 'mi-url-slug'

text1 = text.replace('-', ' ')

splitext = text1.split(' ')

title = ''
for mayus in splitext:
    title = title + mayus.capitalize() + ' '

print(title)

#GENERADORES DE PASSWORDS
from random import choice

longitud = 18
valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"

p = ""
p = p.join([choice(valores) for i in range(longitud)])
print(p)

#GENERADOR DE PASSWORD2
import random
import string
password = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for x in range(18))
#password = ''.join(random.choice(string.printable) for x in range(18))
print(str(password))

#################################################################

#Comparacion entre dos diccionarios:
import re
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}


car2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

message = car.items() ^ car2.items()

keys_changed =  [x for x,y in message if x]

print(keys_changed)

###################################
#Url checker
import re
regex = re.compile(
         r'^(?:http|ftp)s?://' # http:// or https://
         r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
         r'localhost|' #localhost...
         r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
         r'(?::\d+)?' # optional port
         r'(?:/?|[/?]\S+)$', re.IGNORECASE)
a = (re.match(regex, "http://www.example.com/") is not None) # True
b = (re.match(regex, "example.com") is not None) #False
print(a)
print(b)

########################################
#OBTENER EL NOMBRE DE UNA VARIABLE POR ITERACION DE LOCALS
value = 34

my_var_name = [ k for k,v in locals().items() if v is value][0]
print(my_var_name)
