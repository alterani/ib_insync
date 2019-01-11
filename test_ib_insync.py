#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sviluppo di test

NOTA:
    Per funzionare è necessario che ci sia installata la libreria delle API ufficiali IB nella stessa directory.

Created on Fri Nov 23 21:03:22 2018

@author: enricoalterani
"""

from ib_insync import *
util.startLoop()
import pandas as pd
import numpy as np

#PARAMETRI CONNESSIONE
accountName = "DU247692"
# host = "151.80.45.44"                     
host = "" # Se vuoi usare local host lascia il campo vuoto
port = 7496
clientId = 8

#CONNESSIONE
ib = IB()
ib.connect(host,port,clientId)



############### ORDINE STANDARD ########################

#PREPARO IL CONTRATTO
contract = Stock('G','SMART','EUR')
ib.qualifyContracts(contract)

#PREPARO L'ORDINE
order = MarketOrder('BUY',100)

#PIAZZO L'ORDINE
trade = ib.placeOrder(contract,order)

#VISUALIZZO ORDINE PIAZZATO
trade
#######################################################



############ LEGGI CATENA OOZIONI #####################
# spx = Index('SPX', 'CBOE')
spx = Stock('AAPL','SMART','USD')
ib.qualifyContracts(spx)

chains = ib.reqSecDefOptParams(spx.symbol, '', spx.secType, spx.conId)



util.df(chains)

##############à SEZIONE PANDAS #####################################
# Colonne oggetto
#exchange, underlyingConId, tradingClass, multiplier, expirations, strikes

dataframePandas = pd.DataFrame(chains)

dataframePandas[0:1]


#FILTRA SUGLI EXCHANGE E PRENDE SOLO SMART SE ESISTE OPPURE L'UNICA CATENA SE NE ABBIAMO UNA SOLO
if dataframePandas.exchange.count() == 1:
    catena_opzioni = dataframePandas
else:  
    catena_opzioni = dataframePandas [dataframePandas.exchange == 'SMART']

#GENERA MATRICE CONTRATTI
if catena_opzioni.exchange.count():
    
    #Valorizzo Borsa, idSottostante, trading Class e Moltiplicatore
    for a, c in catena_opzioni[0:1].iterrows():
        borsa = c.exchange
        idSottostante = c.underlyingConId
        cod_tradingClass = c.tradingClass
        motliplicatore = c.multiplier
    
    #Creo elenco di tutte le scadenze e di tutte gli strikes
    elenco_scadenze = set()  
    elenco_strikes = set()  
    
    
    
    # catena_opzioni.expirations
    for a, c in dataframePandas.iterrows():
        for valore in c.expirations:
            elenco_scadenze.add(valore)
        for strike in c.strikes:
            elenco_strikes.add(strike)
    
    #Creo matrice contratti vuota
    matrice_contratti = pd.DataFrame(columns=('borsa', 'idSottostante', 'cod_TradingClass','moltiplicatore', 'scadenza','strike'))
    for scadenza in elenco_scadenze:
        for strike in elenco_strikes:
            matrice_contratti = matrice_contratti.append({'borsa': borsa, 'idSottostante': str(idSottostante), 'cod_tradingClass': str(cod_tradingClass), 'motliplicatore': motliplicatore, 'scadenza': scadenza, 'strike': strike  }, ignore_index=True)
   
    matrice_contratti.to_html('matrice_contratti.html')
else:
    print("Nessuna catena opzioni trovata")


for a in elenco_scadenze:
    print(a)





print("La borsa è: {}\nIl id del sottostante è: {}\nIl codice trading class è: {}\n Il moltiplicatore é: {}".format(borsa, idSottostante,cod_tradingClass,motliplicatore))


print("ciao {}, {}, {}".format('enrico', 'test', 'test4'))

print (elenco_strikes)



            

        
        
print(np.random.randn(4))
        

#Visualizza nomi colonne
for col in dataframePandas:
    print(col)
    
# visualizza nome colone e valore
for key, value in dataframePandas.iteritems():
    print(key, value)

for row_index, row in dataframePandas.iterrows():
    print(row_index, row)

riga = next(dataframePandas.iterrows())
print(riga)
    
    

print(expirations)

len(chains) 

i=13
print(chains[i].exchange)

print()
print(chains[i].strikes)
print()
print(chains[i].expirations)






######################################################



#DISCONNESSIONE
ib.disconnect()
