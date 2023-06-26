import paho.mqtt.client as mqtt
import pandas as pd
import datetime

reception = []

def initialisation_connexion(client, userdata, flags, rc):
    client.subscribe("IUT/Colmar2023/SAE2.04/Maison1")
    client.subscribe("IUT/Colmar2023/SAE2.04/Maison2")

def reception_message(client, userdata, msg):
    topic = msg.topic
    payload = str(msg.payload)
    print(payload)

    info = [topic, payload]

    global reception
    reception.append(info)
    if len(reception) > 20:
        reception = reception[-20:]

    # Vérification de l'état de la connexion
    if not client.is_connected():
        enregistrer_sur_excel()

def enregistrer_sur_excel():
    # Convertir les données de réception en DataFrame
    df = pd.DataFrame(reception, columns=['Topic', 'Payload'])

    # Ajouter une colonne avec la date et l'heure actuelles
    df['Timestamp'] = datetime.datetime.now()

    # Enregistrer le DataFrame dans un fichier Excel
    df.to_excel('donnees.xlsx', index=False)

def connexion():
    client = mqtt.Client()
    client.on_connect = initialisation_connexion
    client.on_message = reception_message

    client.connect("test.mosquitto.org", 1883, 60)

    return client

client = connexion()
client.loop_start()
