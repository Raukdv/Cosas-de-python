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

#Generador de codigo de 128Bits string
import random
hash = random.getrandbits(128)
print(hex(hash))


######################################################
#CODIGO PARA LISTAR LLAMADAS DE SIGNALWIRE Y LAS EXPORTA A EXCEL
def get_signal_records():
    import csv
    import pandas as pd # pip install pandas
    import numpy as np  #pip install numpy
    import requests as r #pip install requests
    import json
    import time
    from signalwire.rest import Client as signalwire_client #pip install signalwire o pipenv install signalwire

    signalwire_space_url='example.signalwire.com' #SPACE URL
    project_id='XXXXXXXXXXXXXXXXXXXXXXX' #PROJECT ID // ACCOUNT ID
    token='xDXdxDXdxDXdXdXdx' #API TOKEN / AUHT TOKEN
    full_url = 'https://'+signalwire_space_url #SUSPECT URT
    files_url='https://files.signalwire.com/xxxxxxxxxxxxx/' #SUSPECT FILES URL, YOU WILL FIND THIS URL IN THE FILES OF RECORDS (MP3 OR WAV) THIS ACT AS UNIQUE URL FOR YOU PROJECT
    
    #conexion con el cliente, es decir tu cuenta
    client = signalwire_client(
        'ProjectID', 
        'APITOKEN', 
        signalwire_space_url='example.signalwire.com'
        )
    
    #Listado por rango de fechas
    calls = client.calls.list(start_time_after=datetime(2021, 8, 31), start_time_before=datetime(2021, 10, 1))
    
    with open('signalwire.csv', 'w', newline='') as csvfile:
        fieldnames = [
            'account_sid', 
            'sid', 
            'phone_number_sid', 
            'duration', 
            'start_time',
            'end_time',
            'from',
            'to',
            'direction',
            'date_created',
            'in_signalwire',
            'files_mp3',
            'files_wav',
            ]

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for record in calls:
            print('Starting excel create proccess for:' +str(record.sid))

            uris_records = record.subresource_uris
            uri = uris_records['recordings']
            final_uri = full_url+uri

            print('Requesting proccess for:'+str(record.sid))

            con = r.get(final_uri+'.json',
            auth=(project_id, token),
            headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'},
            )

            print(con.status_code)
            if con.status_code == 200:
                print('Request accept with 200 for: '+str(record.sid))
                print('Starting urls files format')

                return_value = json.loads(con.content.decode('utf-8'))
                        
                id_record = return_value['recordings'] if 'recordings' in return_value and return_value['recordings'] != None else None

                if id_record:
                    print('Record for: '+str(record.sid))
                    id_record=id_record[0]
                    in_signalwire_url = full_url+'/laml-recordings/'+str(id_record['sid'])
                    mp3_url = files_url+project_id+'/recordings/'+id_record['sid']+'.mp3'
                    wav_url = files_url+project_id+'/recordings/'+id_record['sid']+'.wav'
                else:
                    print('No Records for: '+str(record.sid))
                    in_signalwire_url = 'Theres no records in this call'
                    mp3_url = 'Theres no records in this call'
                    wav_url = 'Theres no records in this call'                   
            else:
                print('Request denied with {con.status_code} for: '+str(record.sid))
                in_signalwire_url = 'Theres no records in this call'
                mp3_url = 'Theres no records in this call'
                wav_url = 'Theres no records in this call'

            writer.writerow(
                {'account_sid': record.account_sid,
                'sid': record.sid, 
                'phone_number_sid': record.phone_number_sid, 
                'duration':record.duration, 
                'start_time': record.start_time,
                'end_time': record.end_time,
                'from': record.from_,
                'to': record.to,
                'direction': record.direction,
                'date_created': record.date_created,
                'in_signalwire':in_signalwire_url,
                'files_mp3':mp3_url,
                'files_wav':wav_url
                }
            )
            
        time.sleep(2)
        # Reading the csv file 
        df_new = pd.read_csv('signalwire.csv') 
        # saving xlsx file 
        GFG = pd.ExcelWriter('signalwire.xlsx') 
        df_new.to_excel(GFG, index = False) 
        GFG.save()

#SSL CHECKER#
import socket
import ssl
import datetime

def ssl_check(hostname):
    print(hostname)
    ssl_date_fmt = r'%b %d %H:%M:%S %Y %Z'
    context = ssl.create_default_context()
    conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=hostname,)
    conn.settimeout(3.0)
    try:
        conn.connect((hostname, 443))
        ssl_info = conn.getpeercert()

        print(ssl_info)

        Exp_on = datetime.datetime.strptime(ssl_info['notAfter'], ssl_date_fmt)
        print(f'{hostname} expires on: {Exp_on}')
        print('------------------------')
        print('------------------------')
    except:
        print('domain has not SSL')
        print('------------------------')
        print('------------------------')

domains = ['google.com.site', 'google.com']
for hostname in domains:
    ssl_check(hostname)
################################################
