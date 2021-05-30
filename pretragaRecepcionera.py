def sviRecepcioneri():
    uloga = 'RECEPCIONER'
    obrisan = 'False'
    file = open('korisnici.txt','r')
    ceoFajl = file.readlines()
    for red in ceoFajl:
        a,b,c,d,e,f,g,h,i = red.strip().split(',')
        if uloga == h and obrisan == i:
            print(
            ' ', a, ' ' * (11 - len(a)),
            '|', b,   ' ' * (11-len(b)),
            '|', c,  ' ' * (8-len(c)),
            '|', d,  ' ' * (10-len(d)),
            ' |',e, ' ' * (13-len(e)),
            '|', f,   ' ' * (17-len(f)),
            '|', h, ' ' * (9-len(h)),'|')
    print('\n\n')
    file.close()

def zaglavlje():
    print('\n\n  Username     | Password     | Ime       | Prezime      | Broj telefona  | Email              | Uloga        |')
    print('  -------------------------------------------------------------------------------------------------------------')

def ime(unos1):
    uloga = 'RECEPCIONER'
    obrisan = 'False'
    file = open('korisnici.txt','r')
    ceoFajl = file.readlines()
    for red in ceoFajl:
        a,b,c,d,e,f,g,h,i = red.strip().split(',')
        if unos1 == c and uloga == h and obrisan == i:
            print(
            ' ', a, ' ' * (11 - len(a)),
            '|', b,   ' ' * (11-len(b)),
            '|', c,  ' ' * (8-len(c)),
            '|', d,  ' ' * (10-len(d)),
            ' |',e, ' ' * (13-len(e)),
            '|', f,   ' ' * (17-len(f)),
            '|', h, ' ' * (9-len(h)),'|')
    file.close()

def prezime(unos2):
    uloga = 'RECEPCIONER'
    obrisan = 'False'
    file = open('korisnici.txt','r')
    ceoFajl = file.readlines()
    for red in ceoFajl:
        a,b,c,d,e,f,g,h,i = red.strip().split(',')
        if unos2 == d and uloga == h and obrisan == i:
            print(
            ' ', a, ' ' * (11 - len(a)),
            '|', b,   ' ' * (11-len(b)),
            '|', c,  ' ' * (8-len(c)),
            '|', d,  ' ' * (10-len(d)),
            ' |',e, ' ' * (13-len(e)),
            '|', f,   ' ' * (17-len(f)),
            '|', h, ' ' * (9-len(h)),'|')
    file.close()

def korisnickoIme(unos3):
    uloga = 'RECEPCIONER'
    obrisan = 'False'
    file = open('korisnici.txt','r')
    ceoFajl = file.readlines()
    for red in ceoFajl:
        a,b,c,d,e,f,g,h,i = red.strip().split(',')
        if unos3 == a and uloga == h and obrisan == i:
            print(
            ' ', a, ' ' * (11 - len(a)),
            '|', b,   ' ' * (11-len(b)),
            '|', c,  ' ' * (8-len(c)),
            '|', d,  ' ' * (10-len(d)),
            ' |',e, ' ' * (13-len(e)),
            '|', f,   ' ' * (17-len(f)),
            '|', h, ' ' * (9-len(h)),'|')
    file.close()

def email(unos4):
    uloga = 'RECEPCIONER'
    obrisan = 'False'
    file = open('korisnici.txt','r')
    ceoFajl = file.readlines()
    for red in ceoFajl:
        a,b,c,d,e,f,g,h,i = red.strip().split(',')
        if unos4 == f and uloga == h and obrisan == i:
            print(
            ' ', a, ' ' * (11 - len(a)),
            '|', b,   ' ' * (11-len(b)),
            '|', c,  ' ' * (8-len(c)),
            '|', d,  ' ' * (10-len(d)),
            ' |',e, ' ' * (13-len(e)),
            '|', f,   ' ' * (17-len(f)),
            '|', h, ' ' * (9-len(h)),'|')
    file.close()

def hotel(unos5):
    uloga = 'RECEPCIONER'
    obrisan = 'False'
    file = open('korisnici.txt','r')
    ceoFajl = file.readlines()
    for red in ceoFajl:
        a,b,c,d,e,f,g,h,i = red.strip().split(',')
        if unos5 == g and uloga == h and obrisan == i:
            print(
            ' ', a, ' ' * (11 - len(a)),
            '|', b,   ' ' * (11-len(b)),
            '|', c,  ' ' * (8-len(c)),
            '|', d,  ' ' * (10-len(d)),
            ' |',e, ' ' * (13-len(e)),
            '|', f,   ' ' * (17-len(f)),
            '|', h, ' ' * (9-len(h)),'|')
    file.close()

def jedanKriterijum():

    print(' 1. Po imenu')
    print(' 2. Po prezimenu')
    print(' 3. Po korisnickom imenu')
    print(' 4. Po email-u')
    print(' 5. Po hotelu u kojem je zaposlen')
    print(' 6. Vratite se unazad')
    while True:
        izbor = input('\n Unesi broj od 1 do 6: ')
        if izbor == '1':
            print('\n Izabrali ste pretragu po imenu ! \n')
            unos1 = input(' Unesi ime recepcionera: ' )
            if unos1 == '':
                zaglavlje()
                sviRecepcioneri()
                jedanKriterijum()
            zaglavlje()
            ime(unos1)
            break
        elif izbor == '2':
            print('\n Izabrali ste pretragu po prezimenu ! \n')
            unos2 = input(' Unesi prezime recepcionera: ' )
            if unos2 == '':
                zaglavlje()
                sviRecepcioneri()
                jedanKriterijum()
            zaglavlje()
            prezime(unos2)
            break
        elif izbor == '3':
            print('\n Izabrali ste pretragu po korisnickom imenu ! \n')
            unos3 = input(' Unesi korisnicko ime recepcionera: ' )
            if unos3 == '':
                zaglavlje()
                sviRecepcioneri()
                jedanKriterijum()
            zaglavlje()
            korisnickoIme(unos3)
            break
        elif izbor == '4':
            print('\n Izabrali ste pretragu po email-u ! \n')
            unos4 = input(' Unesi email recepcionera: ' )
            if unos4 == '':
                zaglavlje()
                sviRecepcioneri()
                jedanKriterijum()
            zaglavlje()
            email(unos4)
            break
        elif izbor == '5':
            print('\n Izabrali ste pretragu po hotelu u kojem radi recepcioner ! \n')
            unos5 = input(' Unesi ID hotela: ' )
            if unos5 == '':
                zaglavlje()
                sviRecepcioneri()
                jedanKriterijum()
            zaglavlje()
            hotel(unos5)
            break
        elif izbor == '6':
            pretragaRec()
            break
        else:
            print(' Greska, uneli ste pogresan broj! Molimo vas pokusajte ponovo! ')
    print('\n\n Da li zelite da: \n\n 1. Pokusate opet?\n 2. Izadjete?\n 3. Vratite se unazad? \n')
    while True:
        y = input(' Unesi broj od 1 do 3: ')
        if y == '1':
            jedanKriterijum()
            break
        elif y == '2':
            import administrator
            administrator.administrator() 
            break
        elif y == '3':
            pretragaRec()
            break
        else:
            print('\n Uneli ste pogresan broj, molimo vas pokusajte ponovo!')

def viseKriterijuma():
    
    print('\n Molimo vas popunite sledece podatke!\n ')
    unos1 = input('\n Unesi ime recepcionera: ' )
    unos2 = input(' Unesi prezime recepcionera: ' )
    unos3 = input(' Unesi korisnicko ime recepcionera: ' )
    unos4 = input(' Unesi email recepcionera: ' )
    unos5 = input(' Unesi ID hotela: ' )
    zaglavlje()
    ime(unos1)
    prezime(unos2)
    korisnickoIme(unos3)
    email(unos4)
    hotel(unos5)
    if unos1 == '' and unos2 == '' and unos3 == '' and unos4 == '' and unos5 == '':
        sviRecepcioneri()
    print('\n')
    print('\n\n Da li zelite da: \n\n 1. Pokusate opet?\n 2. Izadjete?\n 3. Vratite se unazad? \n')
    while True:
        y = input(' Unesi broj od 1 do 3: ')
        if y == '1':
            viseKriterijuma()
            break
        elif y == '2':
            import administrator
            administrator.administrator() 
            break
        elif y == '3':
            pretragaRec()
            break
        else:
            print('\n Uneli ste pogresan broj, molimo vas pokusajte ponovo!')

def pretragaRec():

    print('\n Sada je potrebno da izaberete:\n ')
    print(' 1. Pretraga soba po jednom kriterijumu \n 2. Visekriterijumska pretraga soba\n 3. Izlaz \n')
    while True:
        x = input(' Unesi broj od 1 do 3: ')
        if x == '1':
            print('\n*** Izabrali ste pretragu po jednom kriterijumu! ***\n')   
            jedanKriterijum()
            break
        elif x == '2':
            print('\n*** Izabrali ste pretragu po vise kriterijuma! ***\n')   
            viseKriterijuma()
            break
        elif x == '3':
            import administrator
            administrator.administrator()
            break
        else:
            print('\n Uneli ste pogresan broj, pokusajte ponovo')

