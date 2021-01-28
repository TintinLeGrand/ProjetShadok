#!/usr/bin/python
import socket      
# Une socket est une interface logicielle, c'esat-Ã -dire un objet qui reprÃ©sente la connexion entre notre machine et une machine distante sur le rÃ©seau.
# Par dÃ©faut, la socketc'Ã©Ã©e utilise IPv4 et TCP.
# Cet ensemble est disponible a l'installation de Python, dans la bibliotheque de base.
from shadoks import *

Hote = 'IP' # Adresse du serveur.
portEcoute = 233 # Port d'Ã©coute du serveur.
portReponse = 234 # Port de rÃ©ponse du serveur.

# Creation du connecteur d'ecoute par l'instruction 'socket' 
connecteurEcoute = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 
# Creation du connecteur de reponse
connecteurReponse = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

connecteurEcoute.connect((Hote,portEcoute))       # Se connecte au serveur

connecteurReponse.bind((Hote,portReponse))      # instruction 'bind' de la bibliotheque du connecteur
connecteurReponse.listen(1)                     # Ã©coute...
client, adresse = connecteurReponse.accept()    # accepte...
print ("L'adresse",adresse," vous a entendu et attend votre message.") 

while True:
        msg= input('>> ')
        msg = bytes(decode_du_shadok(msg), 'mac_roman')
        connecteurEcoute.send(msg)      # envoi.
        print ("Attente de la reponse...") 
        message = str(client.recv(255),'mac_roman') # reception de la reponse, 255 caracteres max
        if not message:
                break# casse la boucle si pas de message
        message = code_en_shadok(message)
        print ("\n",adresse,":",message,"\a\n")  # affiche la reponse 

client.close() # ferme la connexion lorsque le client quitte.
