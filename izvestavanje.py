from datetime import datetime , timedelta

def zaglavljeZaRez():

    print('\n ID Hotela | ID sobe  | Datum kreiranja rezervacije | Datum Prijave | Datum Odjave |')
    print(' -----------------------------------------------------------------------------------')

def prikazRez(a,b,c,d,e):

    print(
    '',a,  ' ' * (8-len(a)),
    '|', b , ' ' * (7-len(b)),
    '|', c,  ' ' * (26-len(c)), 
    '|', d,  ' ' * (12-len(d)),  '| '
         , e,  ' ' * (10-len(e)),  '|')

def listaRez():

    trenutniDatum = datetime.today().strftime('%Y-%m-%d')
    print('\n Za datum ***',trenutniDatum,'*** trenutno postoje sledece rezervacije: \n')
    file = open('rezervacija.txt','r')
    ceoFajl = file.readlines()
    zaglavljeZaRez()
    for red in ceoFajl:
        a,b,c,d,e,f,g,h = red.strip().split(',')
        if len(ceoFajl) > 1:
            if trenutniDatum in c:
                prikazRez(a,b,c,d,e)
    print('\n')
    file.close()

def brojRez():

    trenutniDatum = datetime.today().strftime('%Y-%m-%d')
    file = open('rezervacija.txt','r')
    ceoFajl = file.readlines()
    ukupno = 0
    for red in ceoFajl:
        a,b,c,d,e,f,g,h = red.strip().split(',')
        if len(ceoFajl) > 1:
            if trenutniDatum in c:
                red = 1
                ukupno += 1
    print(' Za datum ***',trenutniDatum,'*** broj realizovanih rezervacija ukupno je:','_',ukupno,'_')
    print('\n')
    file.close()

def zaglavljeZaSobe():
    print('\n\n ID sobe  | Broj Sobe  | Broj kreveta  | Tip             | Klima  | Tv   | Cena       |')
    print(' --------------------------------------------------------------------------------------')

def prikazSoba(b,c,d,e,f,g,h):

    print(
    '', b, ' ' * (7 - len(b)),
    '|', c,   ' ' * (9-len(c)),
    '|', d,  ' ' * (12-len(d)),
    '|', e,  ' ' * (13-len(e)),
    ' |',f, ' ' * (5-len(f)),
    '|', g,   ' ' * (3-len(g)),
    '|', h, ' ' * (9-len(h)),'|')

def izdateSobe():  

    trenutniDatum = datetime.today().strftime('%Y-%m-%d')
    file = open('rezervacija.txt','r')
    ceoFajl1 = file.readlines()
    ukupno1 = 0
    for red1 in ceoFajl1:
        a,b,c,d,e,f,g,h = red1.strip().split(',')
        IDsobe1 = b
        if len(ceoFajl1) > 1:
            if trenutniDatum in c:
                if IDsobe1 == b:
                    red1 = 1
                    ukupno1 += 1
    print('\n Za datum ***',trenutniDatum,'*** ukupan broj rezervisanih soba je:','_',ukupno1,'_','\n')
    file.close()
    print(' *** Lista rezervisanih soba ! ***')
    file = open('rezervacija.txt','r')
    ceoFajl2 = file.readlines()
    zaglavljeZaSobe()
    for red2 in ceoFajl2:
        a,b,c,d,e,f,g,h = red2.strip().split(',')
        if len(ceoFajl2) > 1:
            if trenutniDatum in c:
                IDsobe = b
                file = open('sobe.txt','r')
                ceoFajl3 = file.readlines()
                for red3 in ceoFajl3:
                    a,b,c,d,e,f,g,h = red3.strip().split(',')
                    if len(ceoFajl3) > 1:
                        if IDsobe == b:
                            prikazSoba(b,c,d,e,f,g,h)
                file.close()
    print('\n')
    file.close()

def ukupnaZarada():

    trenutniDatum = datetime.today().strftime('%Y-%m-%d')
    file = open('rezervacija.txt','r')
    ceoFajl = file.readlines()
    zarada = 0
    for red in ceoFajl:
        a,b,c,d,e,f,g,h = red.strip().split(',')
        if len(ceoFajl) > 1:
            if trenutniDatum in c:
                IDsobe = b
                file = open('sobe.txt','r')
                ceoFajl1 = file.readlines()
                for red1 in ceoFajl1:
                    a,b,c,d,e,f,g,h = red1.strip().split(',')
                    if len(ceoFajl1) > 1:
                        if IDsobe == b:
                            zarada +=  int(h)
                file.close()
    print(' Ukupna zarada od rezervisanih soba je:','_',zarada,'rsd','_')
    print('\n')
    file.close()

def prosecnaOcena():

    trenutniDatum = datetime.today().strftime('%Y-%m-%d')
    file = open('rezervacija.txt','r')
    ceoFajl = file.readlines()
    ukupno = 0
    brojOcena = 0
    for red in ceoFajl:
        a,b,c,d,e,f,g,h = red.strip().split(',')
        if len(ceoFajl) > 1:
            if trenutniDatum in c:
                    ukupno += float(h)
                    red = 1
                    brojOcena += 1
    print('\n Prosecna ocena za hotel je:','_',round(ukupno/brojOcena,1),'_')
    print('\n')
    file.close()

def dnevniIzvestaj():

    print(' *** Ukupan broj realizovanih rezervacija ! ***\n')
    brojRez()
    print(' *** Lista realizovanih rezervacija ! ***')
    listaRez()
    print(' *** Ukupan broj izdatih soba ! ***')
    izdateSobe()
    print(' *** Ukupna zarada ! ***\n')
    ukupnaZarada()
    print(' *** Prosecna ocena hotela ! ***')
    prosecnaOcena()


def nedeljniIzvestaj():

    print(' *** Ukupan broj realizovanih rezervacija ! ***')
    # brojRez()
    print(' *** Lista realizovanih rezervacija ! ***')
    # listaRez()
    print(' *** Ukupan broj izdatih soba ! ***')
    # izdateSobe()
    print(' *** Ukupna zarada ! ***')
    # ukupnaZarada()
    print(' *** Prosecna ocena hotela ! ***')
    # prosecnaOcena()

def mesecniIzvestaj():

    print(' *** Ukupan broj realizovanih rezervacija ! ***')
    # brojRez()
    print(' *** Lista realizovanih rezervacija ! ***')
    # listaRez()
    print(' *** Ukupan broj izdatih soba ! ***')
    # izdateSobe()
    print(' *** Ukupna zarada ! ***')
    # ukupnaZarada()
    print(' *** Prosecna ocena hotela ! ***')
    # prosecnaOcena()

def izvestavanje():

    print('\n Potrebno je izabrati kako zelite da kreirate izvestaj.\n ')
    print(' 1. Na dnevnom nivou')
    print(' 2. Na nedeljnom nivou')
    print(' 3. Na mesecnom nivou\n')
    while True:
        izbor = input(' Unesi broj od 1 do 3: ')
        if izbor == '1':
            print('\n *** Izabrali ste prikaz izvestaja na dnevnom nivou! ***\n\n\n')
            dnevniIzvestaj()
            break
        elif izbor == '2':
            print('\n *** Izabrali ste prikaz izvestaja na nedeljnom nivou! ***\n')
            nedeljniIzvestaj()
            break
        elif izbor == '3':
            print('\n *** Izabrali ste prikaz izvestaja na mesecnom nivou! ***\n')
            mesecniIzvestaj()
            break
        else:
            print('\n Greska! Molimo vas pokusajte ponovo! ')
    print('\n Da li zelite da:\n')
    print(' 1. Pogledate drugi izvestaj?')
    print(' 2. Izadjete\n')
    while True:
        unos = input(' Unesite broj od 1 do 2: ')
        if unos == '1':
            izvestavanje()
            break
        elif unos == '2':
            import recepcioner
            recepcioner.recepcioner()
            break
        else:
            print('\n Uneli ste pokresan broj, molimo vas pokusajte ponovo! ')

