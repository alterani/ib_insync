#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 13:52:23 2018

@author: enricoalterani
"""

import sys
from ib_insync import *
#SE VUOI TESTARE IN PYTHON NORMALE DEVI COMMENTARE
util.startLoop()
import pandas as pd
import numpy as np
import json

#mettere a no in produzione
tagSviluppo = 'SI'

def onError(reqId, errorCode, errorString):
    print('enrico')

ib = IB()

############################################
#   PARAMETRI CONNESSIONE DA FIEL JSON   ###
############################################

with open('config.json') as file:
    parametri = json.load(file)

accountName = parametri['accountName']
host = parametri['host']
port = int(parametri['port'])
clientId = int(parametri['clientId'])
    



def connessione():
    #CONNESSIONE
    return ib.connect(host,port,clientId) 
    
    
def disconnessione():
    #CONNESSIONE
    return ib.disconnect()

    
def printGui(messaggio = ""):
    
    print('\n\n##############################################################################')
    print('#####         I N T E R A C T I V E   B R O K E R   C L I E N T          #####')
    print('##############################################################################')
    guidainlinea()
          
def guidainlinea():
    
    print("\n### ISTRIZIONI COMANDI\n\n")
    
    print("cerca\t\t effetua ricerca del ticker IB")
    print("autore\t\t Riferimento e contatti autore")
    print("exit\t\t Per terminare il programma")    
    
    print("\n")

def autore():
    print("\n\n\nEnrico Alterani e.alterani@gmail.com\n\nSabino Delfino sabino.bt@gmail.com\n\n")

def cerca():
    print("funzione cerca non ancora implementata")


def main(val_input=""):
    
    printGui()
    
    print(str(connessione()) + "\n")
    
    if(val_input == "autore"):
        autore()
    elif(val_input == "cerca"):
       cerca()
    elif(val_input == "exit" or val_input == "" ):
        pass
    else:
        print("Il comando \"" + val_input +"\" non esiste!")
    
    
    disconnessione()
    
    
    if(val_input != "exit"):
        main(str(input("\n\n\n SCRIVI COMANDO....")))
    else:
        print("\n\n\nProgramma terminato correttamente!!\n\n\n")
        
    
        
   
     
if (__name__=='__main__'):
    
    main()
#printGui(str(sys.argv[1]))







    
    

