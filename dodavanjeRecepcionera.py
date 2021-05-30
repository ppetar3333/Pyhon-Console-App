def prikazHotela():

    print('\n Ispod se nalazi spisak hotela po ID-u \n')
    file = open('hoteli.txt','r')
    ceoFajl = file.readlines()
    print(' | ID Hotela  |')
    print(' --------------')
    for red in ceoFajl:
        a,b,c,d,e,f,g,h = red.strip().split(',')
        print( ' |', a,  ' ' * (10-len(a)) + '|')
    file.close()
    print('\n Potrebno je uneti i sifru hotela u kojem ste zaposleni! \n')
    
def dodavanjeRec():

    prikazHotela()
    sifraHotela = input(' Sifra hotela: ') 
    print('\n Sada je potrebno da popunite sledece zahteve! ')
    tipNaloga = 'RECEPCIONER'
    korisnickoIme = input(' Korisnicko ime: ')
    lozinka = input(' Lozinka: ')
    ime = input(' Ime: ')
    prezime = input(' Prezime: ')
    kontaktTelefon = input(' Kontakt telefon: ')
    email = input(' Email adresa: ')
    obrisan = 'False'
    file = open('korisnici.txt','a') 
    noviKORISNIK = korisnickoIme + ',' + lozinka + ',' + ime + ',' + prezime + ',' + kontaktTelefon + ',' + email + ',' + sifraHotela  + ',' + tipNaloga + ',' + obrisan
    file.write('\n' + noviKORISNIK)
    file.close()
    print('\nCestitam, uspesno ste se dodali novog recepcionera! \n')
    import administrator
    administrator.administrator()

def dodavanje():

    print('\n Da li zelite da dodate novog recepcionera? \n')
    print(' 1. Da \n 2. Ne \n')
    while True:
        izbor = input(' Unesite broj od 1 do 2: ')
        if izbor == '1':
            dodavanjeRec()
            break
        elif izbor == '2':
            import administrator
            administrator.administrator()
            break
        else:
            print('\n Uneli ste pogresan broj, molimo vas pokusajte ponovo! ')

