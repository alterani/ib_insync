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

    
    
def formatta_istruzioni_parametro(codice, comando, descrizione):
    
    
    stringa_istruzione = str(codice) + '\t' + str(comando) + '\t\t'  + str(descrizione) + '\n'
    
    return stringa_istruzione


def printGui(messaggio = "", altezza_logo = 25):
    
    print('\n' * (altezza_logo * 2))
    print('##############################################################################')
    print('#####         I N T E R A C T I V E   B R O K E R   C L I E N T          #####')
    print('##############################################################################')
    print(('\n' * 2) + messaggio )
    print("\n" * (altezza_logo - len(messaggio.split('\n'))))

    

def main():
    #printGui("1) - Test Connessione alla TWS")
    if len(sys.argv) == 1 and tagSviluppo == 'NO':
        messaggio = formatta_istruzioni_parametro('\t-------------', '\t---------------------------------------------','')
        messaggio += formatta_istruzioni_parametro('', '  COMANDO','\t       DESCRIZIONE') 
        messaggio += formatta_istruzioni_parametro('\t-------------', '\t---------------------------------------------','')
        messaggio += formatta_istruzioni_parametro('', '','') 
        messaggio += formatta_istruzioni_parametro(1,'-testConn', 'Fa una connessione di test alla TWS')
        messaggio += formatta_istruzioni_parametro(2,'-autore', '\tContatti dello sviluppatore')        
        printGui(messaggio)
        #cancellare la condizione tag sviluppo
    elif ( tagSviluppo == 'SI' or str(sys.argv[1]) == '-testConn'  or (str(sys.argv[1]) == '1')):    
        messaggio = formatta_istruzioni_parametro('\t-------------', '\t---------------------------------------------','')
        messaggio += formatta_istruzioni_parametro('', '  AZIONE','\t       DESCRIZIONE') 
        messaggio += formatta_istruzioni_parametro('\t-------------', '\t---------------------------------------------','')
        messaggio += formatta_istruzioni_parametro('','CONNESSIONE', 'Connessione alla TWS in corso')
        messaggio += formatta_istruzioni_parametro('','Risposta', str(connessione()))
        messaggio += formatta_istruzioni_parametro('','DISCONNESSIONE', 'Disconnessione dlla TWS in corso')
        messaggio += formatta_istruzioni_parametro('','Risposta', str(disconnessione()))
        
        

        printGui(messaggio)
        
    elif ((str(sys.argv[1]) == '-autore') or(str(sys.argv[1]) == '2')):
        messaggio = '* * *  A U T O R E  * * *\n\n\n \nNOME:   ENRICO ALTERANI \n\nMAIL:   e.alterani@gmail.com\n\nTEL:   +39 329 88.37.557\n\nGitHub:   https://github.com/alterani'
        printGui(messaggio)
    else:
        messaggio = formatta_istruzioni_parametro('\t-------------', '\t---------------------------------------------','')
        messaggio += formatta_istruzioni_parametro('', '  ERRORE','\t       DESCRIZIONE') 
        messaggio += formatta_istruzioni_parametro('\t-------------', '\t---------------------------------------------','')
        messaggio += formatta_istruzioni_parametro('','NO PARAM', 'Parametro  "' + str(sys.argv[1]) + '"  non è valido. Inserisci un parametro cotrretto' )
        
        printGui(messaggio)
     
if (__name__=='__main__'):
    main()
#printGui(str(sys.argv[1]))







    
    

