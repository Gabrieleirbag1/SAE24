import paho.mqtt.client as mqtt
import re
import datetime
import pandas as pd

reception = []


def initialisation_connexion(client, userdata, flags, rc):
    client.subscribe("IUT/Colmar2023/SAE2.04/Maison1")
    client.subscribe("IUT/Colmar2023/SAE2.04/Maison2")
    client.subscribe("GABRIEL/SAE/Maison")

def reception_message(client, userdata, msg):
    from mqtt.models import Mq, Do
    topic = msg.topic
    payload = str(msg.payload)
    #print(payload)

    info = [topic, payload]

    global reception
    reception.append(info)
    if len(reception) > 20:
        reception = reception[-20:]

    if not client.is_connected():
        enregistrer_sur_excel()

    def enregistrer_sur_excel():
        df = pd.DataFrame(reception, columns=['Topic', 'Payload'])
        df['Timestamp'] = datetime.datetime.now()
        df.to_excel('donnees.xlsx', index=False)


    emplacement = topic.split("/")[-1]

    mqid_match = re.search(r"Id=([^,]+)", payload)
    if not mqid_match:
        #print("Le message ne contient pas le format attendu pour le mqid.")
        return  
    
    mqid = mqid_match.group(1)

    piece_match = re.search(r"piece=([^,]+)", payload)
    if not piece_match:
        #print("Le message ne contient pas le format attendu pour la piece.")
        return  
    
    piece = piece_match.group(1)
    
    date_match = re.search(r"date=(\d{2}/\d{2}/\d{4})", payload)
    if not date_match:
        #print("Le message ne contient pas le format attendu pour la date.")
        return

    date_str = date_match.group(1)
    date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()

    heure_match = re.search(r"time=(\d+:\d+:\d+)", payload)
    if not heure_match:
        #print("Le message ne contient pas le format attendu pour l'heure.")
        return  
    
    heure = heure_match.group(1)

    temp_match = re.search(r"temp=([\d.]+)", payload)
    if not temp_match:
        print("Le message ne contient pas le format attendu pour la température.")
        return  
    
    temp = float(temp_match.group(1))

    nom = mqid

    mqnom = mqid
    
    mqdate = date

    do = Do(mqid=mqid, date=date, heure=heure, temp=temp, mqnom=mqnom)
    do.save()

    mq = Mq(nom=nom, piece=piece, emplacement=emplacement, idmqtt=do, mqdate=mqdate)
    mq.save()


def connexion():
    client = mqtt.Client()
    client.on_connect = initialisation_connexion
    client.on_message = reception_message

    client.connect("test.mosquitto.org", 1883, 60)

    return client



client = connexion()

client.loop_start()
