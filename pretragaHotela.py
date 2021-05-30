#prikaz svih hotela
def svihoteli():
    file = open('hoteli.txt','r')
    ceoFajl = file.readlines()
    for red in ceoFajl:
        a,b,c,d,e,f,g,h = red.strip().split(',')
        print(
        ' ', b,   ' ' * (15-len(b)),
        '|', c,  ' ' * (21-len(c)),
        '|', e,  ' ' * (5-len(e)),
        ' |',f, ' ' * (8-len(f)),
        '|', g,   ' ' * (5-len(g)),'|')
    print('\n\n')
    file.close()

#zaglavlje pri prikazu
def zaglavlje():
    print('\n\n  Naziv            | Adresa                 | Bazen   | Restoran  | Ocena  |')
    print('  --------------------------------------------------------------------------')

def poNazivu(unos1):
    file = open('hoteli.txt','r')
    ceoFajl = file.readlines()
    for red in ceoFajl:
        a,b,c,d,e,f,g,h = red.strip().split(',')
        if unos1 == b:
            print(
            ' ', b,   ' ' * (15-len(b)),
            '|', c,  ' ' * (21-len(c)),
            '|', e,  ' ' * (5-len(e)),
            ' |',f, ' ' * (8-len(f)),
            '|', g,   ' ' * (5-len(g)),'|')
    file.close()

def poAdresi(unos2):
    file = open('hoteli.txt','r')
    ceoFajl = file.readlines()
    for red in ceoFajl:
        a,b,c,d,e,f,g,h = red.strip().split(',')
        if unos2 == c:
            print(
            ' ', b,   ' ' * (15-len(b)),
            '|', c,  ' ' * (21-len(c)),
            '|', e,  ' ' * (5-len(e)),
            ' |',f, ' ' * (8-len(f)),
            '|', g,   ' ' * (5-len(g)),'|')
    file.close()

def poOceni(unos3):
    file = open('hoteli.txt','r')
    ceoFajl = file.readlines()
    for red in ceoFajl:
        a,b,c,d,e,f,g,h = red.strip().split(',')
        if unos3 == g:
            print(
            ' ', b,   ' ' * (15-len(b)),
            '|', c,  ' ' * (21-len(c)),
            '|', e,  ' ' * (5-len(e)),
            ' |',f, ' ' * (8-len(f)),
            '|', g,   ' ' * (5-len(g)),'|')
    file.close()

def poJednomKriterijumu():
    print(' Izaberite kako zelite da izvrsite pretragu ! \n')
    print(' 1. Po nazivu')
    print(' 2. Po adresi')
    print(' 3. Po oceni')
    print(' 4. Vratite se unazad')
    while True:
        izbor = input('\n Unesi broj od 1 do 4: ')
        if izbor == '1':
            print('\n Izabrali ste pretragu po nazivu !\n ')
            unos1 = input(' Unesi naziv hotela: ')
            if unos1 == '': # == enteru
                zaglavlje()
                svihoteli()
                poJednomKriterijumu()
            zaglavlje()
            poNazivu(unos1)
            break
        elif izbor == '2':
            print('\n Izabrali ste pretragu po adresi !\n ')
            unos2 = input(' Unesi adresu hotela: ')
            if unos2 == '':
                zaglavlje()
                svihoteli()
                poJednomKriterijumu()
            zaglavlje()
            poAdresi(unos2)
            break
        elif izbor == '3':
            print('\n Izabrali ste pretragu po oceni !\n ')
            unos3 = input(' Unesi ocenu hotela: ')
            if unos3 == '':
                zaglavlje()
                svihoteli()
                poJednomKriterijumu()
            zaglavlje()
            poOceni(unos3)
            break
        elif izbor == '4':
            pretraga()
            break
        else:
            print(' Greska, molimo vas pokusajte ponovo! ')
    print('\n\n Da li zelite da: \n\n 1. Pokusate opet?\n 2. Izadjete?\n 3. Vratite se unazad? \n')
    while True:
        y = input(' Unesi broj od 1 do 3: ')
        if y == '1':
            poJednomKriterijumu()
            break
        elif y == '2':
            import registrovanKorisnik
            registrovanKorisnik.registrovanKorisnik() 
            break
        elif y == '3':
            pretraga()
            break
        else:
            print('\n Uneli ste pogresan broj, molimo vas pokusajte ponovo!')

def visekriterijumska():

    print('\n Molimo vas popunite sledece podatke!\n ')
    unos1 = input(' Unesi naziv: ')
    unos2 = input(' Unesi adresu: ')
    unos3 = input(' Unesi ocenu: ')
    zaglavlje()
    poNazivu(unos1)
    poNazivu(unos2)
    poOceni(unos3)
    if unos1 == '' and unos2 == '' and unos3 == '':
        svihoteli()
    print('\n')
    print('\n\n Da li zelite da: \n\n 1. Pokusate opet?\n 2. Izadjete?\n 3. Vratite se unazad? \n')
    while True:
        y = input(' Unesi broj od 1 do 3: ')
        if y == '1':
            visekriterijumska()
            break
        elif y == '2':
            import registrovanKorisnik
            registrovanKorisnik.registrovanKorisnik() 
            break
        elif y == '3':
            pretraga()
            break
        else:
            print('\n Uneli ste pogresan broj, molimo vas pokusajte ponovo!')

#glavni meni
def pretraga():

    print('\nSada je potrebno da izaberete:\n ')
    print(' 1. Pretraga hotela po jednom kriterijumu \n 2. Visekriterijumska pretraga hotela\n 3. Izlaz \n')
    while True:
        x = input('Unesi broj od 1 do 3: ')
        if x == '1':
            print('\n*** Izabrali ste pretragu po jednom kriterijumu! ***\n')
            poJednomKriterijumu()
            break
        elif x == '2':
            print('\n*** Izabrali ste pretragu po vise kriterijuma! ***\n')
            visekriterijumska()
            break
        elif x == '3':
            import registrovanKorisnik
            registrovanKorisnik.registrovanKorisnik()
            break
        else:
            print('\nUneli ste pogresan broj, pokusajte ponovo')

