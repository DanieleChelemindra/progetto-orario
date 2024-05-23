#moduli
import sys

"""
@author: Daniele Chelemindra
"""



def menu_main(Carattere_fine):
    """
    questa funzione serve per creare un menù nel main. 
    inoltre serve a poter utilizare le varie funzionalità del programma.
    
    Parametri (Carattere_fine):
        Carattere_fine: è il carattere che viene utilizato per uscire dal programma.

    Ritorna:
        le varie scelte dell'utente
    """
    gui = (
    "-" * 80,
    "inserisci 1 per avere i docenti di una classe inserita.(f1)",
    "inserisci 2 per avere l'orario di un proffessore scelto e le ore totali",
    "inserisci 3 per avere le ore a disposizione di un docente",
    "inserisci 4 per avere l'elenco dei professori occupati a una determinata ora scelta",
    "inserisci una delle opzioni o inserisci {} per terminare il programma".format(Carattere_fine))
    print("{:^80}\n{:^80}\n{:^80}\n{:^80}\n{:^80}\n{:^80}\n{:^80}".format(gui[0], gui[1], gui[2], gui[3], gui[4], gui[0], gui[5]))
    
    elenco = "1234"
    fine = False
    while not(fine):
        a = input(">>>")
        if a == Carattere_fine:
            sys.exit()
        elif a in elenco:
            break
        else:
            print("{:^80}".format("la scelta deve essere da 1 a 4 o {}".format(Carattere_fine)))

    scelta = a
    return scelta












def leggi_file_csv():
    """
    Legge il file csv e ritorna tutte le righe come liste di stringhe.
    
    Ritorna:
        righe: una lista di liste, dove ogni sottolista rappresenta una riga del file csv.
    """
    with open("OrarioTabellaGlobale.csv", "r") as filecsv:
        righe = [line.strip().split(",") for line in filecsv]
    return righe

def estrai_docenti():
    """
    Estrae la lista dei docenti dal file csv.
    
    Ritorna:
        lista_docenti: contiene la lista di tutti i nomi dei docenti nell'istituto.
    """
    righe = leggi_file_csv()
    lista_docenti = [riga[0].strip() for riga in righe[2:]]
    return lista_docenti

def estrai_orari():
    """
    Estrae la lista degli orari dei docenti dal file csv.
    
    Ritorna:
        lista_orari: contiene la lista degli orari di ogni professore.
    """
    righe = leggi_file_csv()
    lista_orari = [riga[1:] for riga in righe[2:]]
    return lista_orari


def f1(classe_input, orari, docenti):
    """
    Crea un file dove inserisce i nomi di tutti i docenti della classe selezzionata.
   
    parametri (classe_input, orari, docenti):
   
        classe_input = La classe data dall'utente che deve cercare.
       
        orari = lista di tutti gli orari dei docenti nell'istituto.
        
        docenti = lista di tutti i nomi dei docenti nell'istituto.
   
    Ritorna ():
   
    """
    nomefile = classe_input+"docenti.txt"
    file1 = open(nomefile,"a")
    file1.close()
    file1 = open(nomefile,"w")
    file1.write("Elenco docenti nella classe " + classe_input + ":\n\n")
    dizionario = {}
    lista_docenti = []
    for i in range(len(docenti)):
        dizionario[docenti[i]] = orari[i]
    for docente in dizionario:
        for ora in dizionario[docente]:
            if ora == classe_input:
                if docente in lista_docenti:
                    pass
                else:
                    file1.write(docente + "\n")
                    lista_docenti.append(docente)
    file1.close()
    print("Controlla il file", nomefile)
    return


def f2(docenti, orari, docente_input):
    """
    Cerca l'orario di un determinato docente e stampa le ore totali.
   
    Parametri (docenti, orari, docente):
   
        docenti = lista di tutti i nomi dei docenti nell'istituto.
       
        orari = lista di tutti gli orari dei docenti nell'istituto.
       
        docente_input = variabile che contiene il cognome e nome del docente da cercare.

    Ritorna ():

    """
    dizionario = {}
    nomefile = "orario", docente_input.lower() +".txt"
    file2 = open(nomefile,"a")
    file2.close()
    file2 = open(nomefile,"w")
    file2.write("Orario di", docente_input + ":\n\n")
    c = 0
    for i in range(len(docenti)):
        dizionario[docenti[i]] = orari[i]
    file2.write("Lu ,"*8 +"Ma ,"*8 +"Me ,"*8 +"Gi ,"*8 +"Ve ,"*8 +"\n")
    
    for ora in dizionario[docente_input]:
        file2.write(ora + " ")
        if ora != "   ":
            c += 1
    file2.write("\n\n" + docente_input.lower() ,"ha", str(c - 1) ,"ore di lezione.")
    file2.close()
    print("Controlla il file", nomefile)
    return

def f3(docenti, orari, docente_input):
    """
    Cerca il numero di ore D di un determinato docente dato dall'utente.
   
    parametri (docenti, orari, docente_input):
       
        docenti = lista di tutti i nomi dei docenti nell'istituto.
       
        orari = lista di tutti gli orari dei docenti nell'istituto.
       
        docente_input =variabile che contiene il cognome e nome del docente da cercare.
       
    Ritorna ():
   
    """
    nomefile = "disposizione " + docente_input.lower() +".txt"
    file3 = open(nomefile,"a")
    file3.close()
    file3 = open(nomefile,"w")
    file3.write("Ore a disposizioni di",docente_input+":\n\n")
    c = 0
    dizionario = {}
    for i in range(len(docenti)):
        dizionario[docenti[i]] = orari[i]
    for ora in dizionario[docente_input]:
        if ora == " D ":
            c += 1
    file3.write(docente_input,"ha",str(c)," ore in cui è a disposizione.")
    file3.close()
    print("Controlla il file", nomefile)
    return


def f4(ora_input, giorno_input , orari, docenti):
    """
    Cerca il docente di un determinato giorno a una determinata ora date dall'utente.
   
    Parametri (ora_input, giorno_input , orari, docenti):
       
        ora_input: variabile che contiene l'ora della giornata da cercare.
       
        giorno_input: variabile che contiene il giorno dato dall'utente.
     
        orari : lista di tutti gli orari dei docenti nell'istituto.
        
        docenti: lista di tutti i nomi dei docenti nell'istituto.
   
    Ritorna ():

    """
    nomefile = "elencodocentilezione.txt"
    file4 = open(nomefile,"a")
    file4.close()
    file4 = open(nomefile,"w")
    file4.write("Elenco dei docenti che hanno lezione il "+ giorno_input + " alla " + str(ora_input) + "° ora.\n\n")    
    c = 0
    dizionario = {}
    giorni = {"LUN" : 0,"MAR" : 8,"MER" : 16,"GIO" : 24,"VEN" : 32}
    for i in range(len(docenti)):
        dizionario[docenti[i]] = orari[i]
    for docente in dizionario:
        if dizionario[docente][(ora_input - 1) + (giorni[giorno_input])] != "   ":
            file4.write(docente + "\n")
            c += 1
    file4.write("\nIl", str(giorno_input),"alla",str(ora_input) + "° ora", str(c) ,"docenti hanno lezione.")
    file4.close()
    print("Controlla il file", nomefile)    
    return