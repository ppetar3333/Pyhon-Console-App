def sveRezervacije():
    file = open('rezervacija.txt','r')
    ceoFajl = file.readlines()
    for red in ceoFajl:
        a,b,c,d,e,f,g,h = red.strip().split(',')
        print(
        ' ',a,  ' ' * (8-len(a)),
        '|', b , ' ' * (7-len(b)),
        '|', c,  ' ' * (26-len(c)), 
        '|', d,  ' ' * (12-len(d)),  '| '
             , e,  ' ' * (10-len(e)),  '|')
    file.close()
    print('\n')

def zaglavlje():
    print('\n  ID Hotela | ID sobe  | Datum kreiranja rezervacije | Datum Prijave | Datum Odjave |')
    print('  -----------------------------------------------------------------------------------')

def kreiranjeRez(unos1):
    file = open('rezervacija.txt','r')
    ceoFajl = file.readlines()
    for red in ceoFajl:
        a,b,c,d,e,f,g,h = red.strip().split(',')
        if unos1 == c:
            print(
            ' ',a,  ' ' * (8-len(a)),
            '|', b , ' ' * (7-len(b)),
            '|', c,  ' ' * (26-len(c)), 
            '|', d,  ' ' * (12-len(d)),  '| '
                 , e,  ' ' * (10-len(e)),  '|')
    file.close()


def datumPrijave(unos2):
    file = open('rezervacija.txt','r')
    ceoFajl = file.readlines()
    for red in ceoFajl:
        a,b,c,d,e,f,g,h = red.strip().split(',')
        if unos2 == d:
            print(
            ' ',a,  ' ' * (8-len(a)),
            '|', b , ' ' * (7-len(b)),
            '|', c,  ' ' * (26-len(c)), 
            '|', d,  ' ' * (12-len(d)),  '| '
                 , e,  ' ' * (10-len(e)),  '|')
    file.close()

def datumOdjave(unos3):
    file = open('rezervacija.txt','r')
    ceoFajl = file.readlines()
    for red in ceoFajl:
        a,b,c,d,e,f,g,h = red.strip().split(',')
        if unos3 == e:
            print(
            ' ',a,  ' ' * (8-len(a)),
            '|', b , ' ' * (7-len(b)),
            '|', c,  ' ' * (26-len(c)), 
            '|', d,  ' ' * (12-len(d)),  '| '
                 , e,  ' ' * (10-len(e)),  '|')
    file.close()

def korisnik(unos4):
    file = open('rezervacija.txt','r')
    ceoFajl = file.readlines()
    for red in ceoFajl:
        a,b,c,d,e,f,g,h = red.strip().split(',')
        if unos4 == f:
            print(
            ' ',a,  ' ' * (8-len(a)),
            '|', b , ' ' * (7-len(b)),
            '|', c,  ' ' * (26-len(c)), 
            '|', d,  ' ' * (12-len(d)),  '| '
                 , e,  ' ' * (10-len(e)),  '|')
    file.close()

def statusRez(unos5):
    file = open('rezervacija.txt','r')
    ceoFajl = file.readlines()
    for red in ceoFajl:
        a,b,c,d,e,f,g,h = red.strip().split(',')
        if unos5 == g:
            print(
            ' ',a,  ' ' * (8-len(a)),
            '|', b , ' ' * (7-len(b)),
            '|', c,  ' ' * (26-len(c)), 
            '|', d,  ' ' * (12-len(d)),  '| '
                 , e,  ' ' * (10-len(e)),  '|')
    file.close()

def poJednomKriterijumu():

    print(' 1. Po datumu i vremenu kreiranja rezervacije')
    print(' 2. Po datumu prijave')
    print(' 3. Po datumu odjave')
    print(' 4. Po korisniku koji je izvrsio rezervaciju')
    print(' 5. Po statusu rezervacije')
    print(' 6. Vratite se unazad')
    while True:
        izbor = input('\n Unesi broj od 1 do 5: ')
        if izbor == '1':
            print('\n Izabrali ste pretragu po datumu i vremenu kreiranja rezervacije ! \n')
            unos1 = input(' Unesi datum kreiranja rezervacije: ' )
            if unos1 == '':
                zaglavlje()
                sveRezervacije()
                poJednomKriterijumu()
            zaglavlje()
            kreiranjeRez(unos1)
            break
        elif izbor == '2':
            print('\n Izabrali ste pretragu po datumu prijave ! \n')
            unos2 = input(' Unesi datum prijave u hotel: ' )
            if unos2 == '':
                zaglavlje()
                sveRezervacije()
                poJednomKriterijumu()
            zaglavlje()
            datumPrijave(unos2)
            break
        elif izbor == '3':
            print('\n Izabrali ste pretragu po datumu odjave ! \n')
            unos3 = input(' Unesi datum odjave iz hotela: ' )
            if unos3 == '':
                zaglavlje()
                sveRezervacije()
                poJednomKriterijumu()
            zaglavlje()
            datumOdjave(unos3)
            break
        elif izbor == '4':
            print('\n Izabrali ste pretragu po korisniku koji je izvrsio rezervaciju ! \n')
            unos4 = input(' Unesi username korisnika: ' )
            if unos4 == '':
                zaglavlje()
                sveRezervacije()
                poJednomKriterijumu()
            zaglavlje()
            korisnik(unos4)
            break
        elif izbor == '5':
            print('\n Izabrali ste pretragu po statusu rezervacije ! \n')
            unos5 = input(' Unesi status rezervacije: ' )
            if unos5 == '':
                zaglavlje()
                sveRezervacije()
                poJednomKriterijumu()
            zaglavlje()
            statusRez(unos5)
            break
        elif izbor == '6':
            pretragaRezervacija()
            break
        else:
            print(' Greska, uneli ste pogresan broj! Molimo vas pokusajte ponovo! ')
    print('\n\n Da li zelite da: \n\n 1. Pokusate opet?\n 2. Izadjete?\n 3. Vratite se unazad? \n')
    while True:
        y = input(' Unesi broj od 1 do 3: ')
        if y == '1':
            poJednomKriterijumu()
            break
        elif y == '2':
            import recepcioner
            recepcioner.recepcioner() 
            break
        elif y == '3':
            pretragaRezervacija()
            break
        else:
            print('\n Uneli ste pogresan broj, molimo vas pokusajte ponovo!')


def poViseKriterijuma():

    print('\n Molimo vas popunite sledece podatke!\n ')
    unos1 = input(' Unesi datum kreiranja rezervacije: ' )
    unos2 = input(' Unesi datum prijave u hotel: ' )
    unos3 = input(' Unesi datum odjave iz hotela: ' )
    unos4 = input(' Unesi username korisnika: ' )
    unos5 = input(' Unesi status rezervacije: ' )
    zaglavlje()
    kreiranjeRez(unos1)
    datumPrijave(unos2)
    datumOdjave(unos3)
    korisnik(unos4)
    statusRez(unos5)
    if unos1 == '' and unos2 == '' and unos3 == '' and unos4 == '' and unos5 == '':
        sveRezervacije()
    print('\n')
    print('\n\n Da li zelite da: \n\n 1. Pokusate opet?\n 2. Izadjete?\n 3. Vratite se unazad? \n')
    while True:
        y = input(' Unesi broj od 1 do 3: ')
        if y == '1':
            poViseKriterijuma()
            break
        elif y == '2':
            import recepcioner
            recepcioner.recepcioner() 
            break
        elif y == '3':
            pretragaRezervacija()
            break
        else:
            print('\n Uneli ste pogresan broj, molimo vas pokusajte ponovo!')


def pretragaRezervacija():

    print('\nSada je potrebno da izaberete:\n ')
    print(' 1. Pretraga soba po jednom kriterijumu \n 2. Visekriterijumska pretraga soba\n 3. Izlaz \n')
    while True:
        x = input(' Unesi broj 1 ili 2: ')
        if x == '1':
            print('\n*** Izabrali ste pretragu po jednom kriterijumu! ***\n')
            poJednomKriterijumu()
            break
        elif x == '2':
            print('\n*** Izabrali ste pretragu po vise kriterijuma! ***\n')
            poViseKriterijuma()
            break
        elif x == '3':
            import recepcioner
            recepcioner.recepcioner()
            break
        else:
            print('\n Uneli ste pogresan broj, pokusajte ponovo')

