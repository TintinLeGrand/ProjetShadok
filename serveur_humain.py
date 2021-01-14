#!/usr/bin/python
import socket      
# Une socket est une interface logicielle, c'esat-Ã -dire un objet qui reprÃ©sente la connexion entre notre machine et une machine distante sur le rÃ©seau.
# Par dÃ©faut, la socketc'Ã©Ã©e utilise IPv4 et TCP.
# Cet ensemble est disponible a l'installation de Python, dans la bibliotheque de base.
 
hote = '127.0.0.1' # Adresse locale de l'ordinateur.
portEcoute = 233          # Choix d'un port d'Ã©coute.
portReponse = 234          # Choix d'un port de reponse.
 
# Creation du connecteur d'ecoute par l'instruction 'socket' 
connecteurEcoute = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 
# Creation du connecteur de reponse
connecteurReponse = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

connecteurEcoute.bind((hote,portEcoute)) # instruction 'bind' de la bibliotheque du connecteur
print ("Le programme est Ã  l'Ã©coute d'une Ã©ventuelle discussion, vous en serez averti.")
connecteurEcoute.listen(1)                  # Ã©coute...
client, adresse = connecteurEcoute.accept() # accepte...
print ("La machine ",adresse," veut discuter ! J'attends son message.")
connecteurReponse.connect((hote,portReponse ))
print ("Note : je me suis connectÃ© Ã ",adresse," pour lui repondre")
 
while True:
        message = str(client.recv(255),'mac_roman') # reception de la reponse, 255 caracteres max ; 
        if not message: 
                break  # casse la boucle si pas de message
        print ("\nMessage : ",message,"\a" + "\n\nVotre reponse :")
        msgR = bytes(input('>> '), 'mac_roman')
        connecteurReponse.send(msgR)        # envoi. 
 
client.close() # ferme la connexion lorsque le client est parti : [ctrl+C] pour abandonner l'execution du programme.