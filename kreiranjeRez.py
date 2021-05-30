import datetime
import azuriranjeHotela
sviHoteli = []
sveSobe = []

#ucitavam hotele,prebacujem sve redove u recnik pa appendujem u listu i zatvaram ih pre glavne funkcije
def ucitavanjeHotela():
	file = open('hoteli.txt','r')
	ceoFajl = file.readlines()
	file.close()
	for red in ceoFajl:
		hoteli = string(red)
		sviHoteli.append(hoteli)
	return sviHoteli

#prebacivanje stringa u recnik hoteli={}
def string(red):
    sifra, naziv, adresa, listaSoba, bazen, restoran, ocena, obrisan = red.strip().split(',')
    hoteli = {
      'sifra': sifra,
      'naziv': naziv,
      'adresa': adresa,
      'listaSoba': listaSoba,
      'bazen': bazen,
      'restoran': restoran,
      'ocena': ocena,
      'obrisan': obrisan
    }
    return hoteli

#trazenje hotela po sifri
def findHotel(sifra):
    for hoteli in sviHoteli:
        if hoteli['sifra'] == sifra:
            return hoteli
    return None

#ucitavanje soba, prebacujem redove u recnik pa to appendujem u listu i zatvaram pre glavne funkcije
def ucitavanjeSoba():
    file = open('sobe.txt','r')
    ceoFajl = file.readlines()
    file.close()
    for red1 in ceoFajl:
        sobe = sobeString(red1)
        sveSobe.append(sobe)
    return sveSobe

#prebacivanje iz stringa u recnik sobe={}
def sobeString(red1):
    IDhotela, IDsobe, brojSobe, brojKreveta, tip, klima, tv, cena = red1.strip().split(',')
    sobe = {
      'IDhotela': IDhotela,
      'IDsobe': IDsobe,
      'brojSobe': brojSobe,
      'brojKreveta': brojKreveta,
      'tip': tip,
      'klima': klima,
      'tv': tv,
      'cena': cena,
    }
    return sobe

#formatiranje za zaglavlje()
def podaci(sobe):
    return '  {0:9}| {1:11}| {2:14}| {3:16}| {4:6} | {5:4} | {6:10} |'.format(
      sobe['IDsobe'],
      sobe['brojSobe'],
      sobe['brojKreveta'],
      sobe['tip'],
      sobe['klima'],
      sobe['tv'],
      sobe['cena'])

#zaglavlje za sobu
def zaglavlje():
    return \
        '\n\n  ID sobe  | Broj Sobe  | Broj kreveta  | Tip             | Klima  | Tv   | Cena       |\n' \
        '  --------------------------------------------------------------------------------------'

#trazenje sobe po ID-u
def findSobu(IDsobe):
    for sobe in sveSobe:
        if  IDsobe == sobe['IDsobe']:
            return sobe
    return None

def unosDatuma(sifra,IDsobe):
    
    #korisnicko ime
    file = open('promenljive.txt','r')
    ceoFajl = file.readlines()
    for red in ceoFajl:
        korisnik = red
    file.close
    #popunjavanje podataka
    print('\n\n Sada je potrebno da unesete datum prijave i odjave! \n')
    datumKreiranja = datetime.datetime.today().strftime('%Y-%m-%d %H:%M')
    datumPrijave = input(' Unesi datum prijave u hotel (yyyy-mm-dd): ')
    datumOdjave = input(' Unesi datum odjave iz hotela (yyyy-mm-dd): ')
    if datumKreiranja < datumPrijave:
        rezervacija = 'rezervacija jos uvek nije zapoceta'
    elif datumKreiranja > datumPrijave and datumKreiranja < datumOdjave:
        rezervacija = 'rezervacija je u toku'
    elif datumKreiranja > datumOdjave:
        rezervacija = 'rezervacija je zavrsena'
    #provera da li je soba slobodna?
    file = open('rezervacija.txt','r')
    ceoFajl = file.readlines()
    for red in ceoFajl:
        words = red.strip().split(',')
        if IDsobe == words[1]:
            if datumPrijave >= words[3] and datumOdjave <= words[4]:
                print('\n Soba je rezervisana u datom periodu! ')
                print('\n Pokusajte ponovo sa drugim datumom !')
                unosDatuma(sifra,IDsobe)
                exit() #prekid
            else: #nastavi
                pass 
    file.close()
    #upis podataka
    print('\n Uspesno ste rezervisali sobu! \n')
    file = open('rezervacija.txt','a')
    print('\n Sada je potrebno da ocenite hotel! ')
    ocena = input('\n Unesi ocenu (od 1 do 5): ')
    file.write('\n' + sifra + ',' + IDsobe + ',' + datumKreiranja + ',' + datumPrijave + ',' + datumOdjave + ',' + korisnik + ',' + rezervacija + ',' + ocena)
    file.close()
    #meni za korisnika
    import registrovanKorisnik
    registrovanKorisnik.registrovanKorisnik()

def kreiranjeRezervacije():

    #izbor hotela
    print('\n Sada je potrebno da izaberete hotel!\n ')
    sifra = input(' Unesite ID hotela: ')
    hoteli = findHotel(sifra)
    if hoteli == None:
        print('\n Uneli ste pogresan ID hotela! ')
        import registrovanKorisnik
        registrovanKorisnik.registrovanKorisnik()
    else:
        print(azuriranjeHotela.header())
        print(azuriranjeHotela.podaci(hoteli))
    #izbor soba
    print('\n\n Sada je potrebno da izaberete sobu koju hocete da rezervisete!\n ')
    IDsobe = input(' Unesi ID sobe koju hoces da rezervises: ')
    sobe = findSobu(IDsobe)
    if sobe == None:
        print('\n Uneli ste pogresan ID sobe! ')
        import registrovanKorisnik
        registrovanKorisnik.registrovanKorisnik() 
    else:
        print(zaglavlje())
        print(podaci(sobe))
    #unos datuma 
    unosDatuma(sifra,IDsobe)  

ucitavanjeHotela()
ucitavanjeSoba()
