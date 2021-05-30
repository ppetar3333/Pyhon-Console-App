#korisnik
def registracijaKaoKorisnik():

    tipNaloga = 'KORISNIK'
    korisnickoIme = input(' Korisnicko ime: ')
    file = open('korisnici.txt','r')
    ceoFajl = file.readlines()
    for red in ceoFajl:
        a,b,c,d,e,f,g,h,i = red.strip().split(',')
        if korisnickoIme == a:
            print('\n Korisnik sa unetim username-om vec postoji, molimo vas pokusajte ponovo da se registrujete! ')
            registrujSe()
            exit()
    file.close()
    lozinka = input(' Lozinka: ')
    ime = input(' Ime: ')
    prezime = input(' Prezime: ')
    kontaktTelefon = input(' Kontakt telefon: ')
    email = input(' Email adresa: ')
    obrisan = 'False'
    file = open('korisnici.txt','a') 
    noviKORISNIK = korisnickoIme + ',' + lozinka + ',' + ime + ',' + prezime + ',' + kontaktTelefon + ',' + email + ',' + ',' + tipNaloga + ',' + obrisan
    file.write('\n' + noviKORISNIK) #ispisuje novog korosnika u novom redu
    file.close()
    print('\nCestitam uspesno ste se registrovali kao korisnik na nasu aplikaciju! \n')

#recepcioner
def registracijaKaoRecepcioner():

    tipNaloga = 'RECEPCIONER'
    korisnickoIme = input(' Korisnicko ime: ')
    file = open('korisnici.txt','r')
    ceoFajl = file.readlines()
    for red in ceoFajl:
        a,b,c,d,e,f,g,h,i = red.strip().split(',')
        if korisnickoIme == a:
            print('\n Korisnik sa unetim username-om vec postoji, molimo vas pokusajte ponovo da se registrujete! ')
            registrujSe()
            exit()
    file.close()
    lozinka = input(' Lozinka: ')
    ime = input(' Ime: ')
    prezime = input(' Prezime: ')
    kontaktTelefon = input(' Kontakt telefon: ')
    email = input(' Email adresa: ')
    sifra = input(' Sifra hotela u kojem ste zaposleni: ')
    obrisan = 'False'
    file = open('korisnici.txt','a') 
    noviKORISNIK = korisnickoIme + ',' + lozinka + ',' + ime + ',' + prezime + ',' + kontaktTelefon + ',' + email + ',' + sifra + ',' + tipNaloga+ ',' + obrisan
    file.write('\n' + noviKORISNIK) 
    file.close()
    print('\nCestitam uspesno ste se registrovali kao recepcioner na nasu aplikaciju! \n')

#glavni meni
def registrujSe():

    print('\nSada morate izabrati kako zelite da obavite registraciju: \n')
    print(' 1. Korisnik\n 2. Recepcioner \n')
    while True:
        x1 = input(' Unesite broj 1 ili 2: ')
        if x1 == '1':
            print('\n*** Izabrali ste da hocete da se registrujete kao korisnik! ***\n ')
            registracijaKaoKorisnik()
            break
        elif x1 == '2':
            print('\n*** Izabrali ste da hocete da se registrujete kao recepcioner! *** \n')
            registracijaKaoRecepcioner()
            break
        else:
            print('\n Uneli ste pogresan broj, molimo vas pokusajte ponovo.')

    #po zavrsetku registracije potrebno je da se korisnik uloguje
    print('\nSada je potrebno da se ulogujete. \n')
    import ulogujSe
    ulogujSe.ulogujSe()


