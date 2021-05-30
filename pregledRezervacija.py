rezervacija = []

def ucitavanjeRezervacije():
    file = open('rezervacija.txt','r')
    ceoFajl1 = file.readlines()
    file.close()
    for red1 in ceoFajl1:
        rezervacijaPodaci = podaci(red1)
        rezervacija.append(rezervacijaPodaci)

def podaci(red1):
	podaci1 = red1.strip().split(',')
	rezervacijaPodaci = {'idhotela': podaci1[0],
		'idsobe': podaci1[1],
		'datumKreiranja': podaci1[2],
		'datumPrijave': podaci1[3],
		'datumOdjave': podaci1[4],
		'username': podaci1[5],
		'statusRez': podaci1[6],
        'ocenaHotela': podaci1[7]}
	return rezervacijaPodaci

def header():
    print('\n  ID Hotela | Status rezervacije                  | Datum kreiranja rezervacije | Datum Prijave | Datum Odjave |')
    print('  --------------------------------------------------------------------------------------------------------------')

def prikazPodataka(linija):
    print(
    ' ',linija['idhotela'],  ' ' * (8-len(linija['idhotela'])),
    '|',linija['statusRez'], ' ' * (34-len(linija['statusRez'])),
    '|',linija['datumKreiranja'],  ' ' * (26-len(linija['datumKreiranja'])), 
    '|',linija['datumPrijave'],  ' ' * (12-len(linija['datumPrijave'])),  '| '
       ,linija['datumOdjave'],  ' ' * (10-len(linija['datumOdjave'])),  '|')

def prethodneRez():
    status = 'rezervacija je zavrsena'
    file = open('promenljive.txt','r')
    ceoFajl = file.readlines()
    for red in ceoFajl:
        korisnik = red
    file.close
    header()
    for rezervacijaPodaci in rezervacija:
        if korisnik == rezervacijaPodaci['username'] and status == rezervacijaPodaci['statusRez']:
            linija = rezervacijaPodaci
            prikazPodataka(linija)
    print('\n\n')

def nezapoceteRez():
    status = 'rezervacija jos uvek nije zapoceta'
    file = open('promenljive.txt','r')
    ceoFajl = file.readlines()
    for red in ceoFajl:
        korisnik = red
    file.close
    header()
    for rezervacijaPodaci in rezervacija:
        if korisnik == rezervacijaPodaci['username'] and status == rezervacijaPodaci['statusRez']:
            linija = rezervacijaPodaci
            prikazPodataka(linija)
    print('\n\n')

def rezUtoku():
    status = 'rezervacija je u toku'
    file = open('promenljive.txt','r')
    ceoFajl = file.readlines()
    for red in ceoFajl:
        korisnik = red
    file.close
    header()
    for rezervacijaPodaci in rezervacija:
        if korisnik == rezervacijaPodaci['username'] and status == rezervacijaPodaci['statusRez']:
            linija = rezervacijaPodaci
            prikazPodataka(linija)
    print('\n\n')

def pregledSvihRezervacija():

    print('\n Potrebno je izabrati koje rezervazije hocete da pregledate. \n')
    print(' 1. Prethodne rezervacije \n 2. Rezervacije koje nisu zapocete \n 3. Rezervacije koje su u toku\n 4. Izadji \n')
    while True:
        izbor = input(' Unesi broj od 1 do 3: ')
        if izbor == '1':
            print('\n *** Izabrali ste da hocete da pregledate prethodne rezervacije! *** \n')
            prethodneRez()
            break
        elif izbor == '2':
            print('\n *** Izabrali ste da hocete da pregledate rezervacije koje nisu zapocete! *** \n')
            nezapoceteRez()
            break
        elif izbor == '3':
            print('\n *** Izabrali ste da hocete da pregledate rezervacije koje su u toku! *** \n')
            rezUtoku()
            break
        elif izbor == '4':
            import registrovanKorisnik
            registrovanKorisnik.registrovanKorisnik() 
            break
        else:
            print('\n Greska, molimo vas pokusajte ponovo! ')

    print(' Da li zelite da: \n\n 1. Pogledate druge rezervacije? \n 2. Izadjete?\n')
    while True:
        x = input(' Unesi broj od 1 do 2: ')
        if x == '1':
            pregledSvihRezervacija()
            break
        elif x == '2':
            import registrovanKorisnik
            registrovanKorisnik.registrovanKorisnik()
            break
        else:
            print('\n Greska, molimo vas pokusajte ponovo! ')

ucitavanjeRezervacije()
