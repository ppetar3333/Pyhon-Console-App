sviHoteli = []

def ucitavanjeHotela():
	file = open('hoteli.txt','r')
	ceoFajl = file.readlines()
	file.close()
	for red in ceoFajl:
		hoteli = string(red)
		sviHoteli.append(hoteli)
	return sviHoteli

def upisIzmena(hoteli): 
    return ','.join([hoteli['sifra'], hoteli['naziv'], hoteli['adresa'], 
    hoteli['listaSoba'], hoteli['bazen'], hoteli['restoran'], hoteli['ocena'], hoteli['obrisan']]) 



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


def findHotel(naziv):
    for hoteli in sviHoteli:
        if hoteli['naziv'] == naziv:
            return hoteli
    return None

def header():
    return \
      '\n\n  Naziv             | Adresa                 | Bazen   | Restoran  | Ocena  |\n' \
      '  ---------------------------------------------------------------------------'
def podaci(hoteli):
    return '  {0:18}| {1:23}| {2:8}| {3:10}| {4:6} |'.format(
      hoteli['naziv'],
      hoteli['adresa'],
      hoteli['bazen'],
      hoteli['restoran'],
      hoteli['ocena'])

def saveHotels():
    file = open('hoteli.txt', 'w')
    for hoteli in sviHoteli:
        file.write(upisIzmena(hoteli))
        file.write('\n')
    file.close()


def azuriranje():

    import brisanjeHotela
    brisanjeHotela.sviHoteli()

    naziv = input(' Unesite naziv hotela: ')
    hoteli = findHotel(naziv)
    if hoteli == None:
        print('\n Uneli ste pogresan naziv hotela! ')
        import administrator
        administrator.administrator()
    else:
        print(header())
        print(podaci(hoteli))
        print('\n Izaberite sta hocete da azurirate: \n\n 1. Broj soba \n 2. Bazen \n 3. Restoran \n 4. Izadji\n' )
        while True:
            x = input(' Upisi broj od 1 do 4: ')
            if x == '1':
                print('\n Broj soba u hotelu', hoteli['naziv'],'je:',hoteli['listaSoba'])
                hoteli['listaSoba'] = input('\n Unesite nove sobe: ')
                break
            elif x == '2':
                print('\n Bazen u hotelu', hoteli['naziv'],'(da ili ne):',hoteli['bazen'])
                hoteli['bazen'] = str(input(' Unesite bazen (da ili ne): '))
                break
            elif x == '3':
                print('\n Restoran u hotelu', hoteli['naziv'],'(da ili ne):',hoteli['restoran'])
                hoteli['restoran'] = str(input(' Unesite restoran (da ili ne): '))
                break
            elif x == '4':
                import administrator
                administrator.administrator()
                break
            else:
                print('\n Greska, molimo vas pokusajte ponovo')
        print('\n Izmena sacuvana! \n')
        saveHotels()

        import administrator
        administrator.administrator()

ucitavanjeHotela()

