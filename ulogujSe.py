korisnici = [] #lista
# otvaranje fajla u read modu, citanje svih podataka
# svaki red konvertujem u recnik
# svaki recnik dodam u listu
def ucitavanjeKorisnika():
    file = open('korisnici.txt','r')
    ceoFajl = file.readlines()
    for red in ceoFajl:
        korisniciPodaci = podaci(red)
        korisnici.append(korisniciPodaci)
    file.close()

# korisniciPodaci{} recnik, prebacivanje iz stringa u korisniciPodaci(recnik)
def podaci(red):
    username, password, ime, prezime, brojTelefona, email, sifra, uloga, obrisan = red.strip().split(',')
    korisniciPodaci = {
        'username': username,
        'password': password,
        'ime': ime,
        'prezime': prezime,
        'brojTelefona': brojTelefona,
        'email': email,
        'sifra': sifra,
        'uloga': uloga,
        'obrisan': obrisan
    }
    return korisniciPodaci

def unos():
    username = input('\n Korisnicko ime: ')
    password = input(' Lozinka: ')
    file = open('promenljive.txt','w') #upisujem username u promenljive.txt da bi posle znao ko je ulogovan
    file.write(username)
    file.close()
    return provera(username, password) #proveravam unos

def provera(username, password):
    recepcioner = 'RECEPCIONER'
    administrator = 'ADMINISTRATOR'
    korisnik = 'KORISNIK'
    for korisniciPodaci in korisnici:
        if korisniciPodaci['username'] == username and korisniciPodaci['password'] == password:
            if korisniciPodaci['uloga'] == recepcioner:
                print(' \n * Dobrodosli,',korisniciPodaci['ime'],'*')
                print('\n*** Ulogovani ste da kao recepcioner! ***')
                import recepcioner
                recepcioner.recepcioner()
            elif korisniciPodaci['uloga'] == administrator:
                print(' \n * Dobrodosli,',korisniciPodaci['ime'],'*')
                print('\n*** Ulogovani ste da kao administrator! ***')
                import administrator
                administrator.administrator()
            elif korisniciPodaci['uloga'] == korisnik:
                print(' \n * Dobrodosli,',korisniciPodaci['ime'],'*')
                print('\n*** Ulogovani ste da kao korisnik! ***')
                import registrovanKorisnik
                registrovanKorisnik.registrovanKorisnik()
            return True
    return False

def ulogujSe():

    print('\n * Molimo vas popunite sledece zahteve *')
    while not unos(): #vrti petlju dok ne unese tacan username i password
        print('\n Greska, molimo vas pokusajte ponovo ili se registrujte!\n ')
        print(' 1. Pokusaj ponovo \n 2. Registruj se \n ')
        while True:
            izbor = input(' Unesi broj od 1 do 2: ')
            if izbor == '1':
                ulogujSe()
                break
            elif izbor == '2':
                import registrujSe
                registrujSe.registrujSe()
                break
            else:
                print('\n Uneli ste pogresan broj, unesite broj od 1 do 2!')

ucitavanjeKorisnika()



