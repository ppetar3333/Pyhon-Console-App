sviHoteli = []
def ucitavanjeHotela():
	file = open('hoteli.txt','r')
	ceoFajl = file.readlines()
	file.close()
	for red in ceoFajl:
		hoteli = string(red)
		sviHoteli.append(hoteli)
	return sviHoteli

def string(red):
	podaci = red.strip().split(',')
	hoteli = {'sifra': podaci[0],
		'naziv': podaci[1],
		'adresa': podaci[2],
		'brojSoba': podaci[3],
		'bazen': podaci[4],
		'restoran': podaci[5],
		'ocena': podaci[6]}
	return hoteli

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

def formatHotel(sviHoteli):
    result = ''
    for hoteli in sviHoteli:
        result = result +  podaci(hoteli) + '\n'
    return result[:390]


def najboljeOceneHotela():

    print('\n\n\n             *** Ispod se nalaze 5 najbolje ocenjenih hotela! ***') 
    sviHoteli.sort(key=lambda x : x['ocena'],reverse=True) # lambda argument (koliko god moze 1 a moze i vise) : izraz (samo jedan) i po tome sortira
    print(header())
    print(formatHotel(sviHoteli))
    print('\n\n')
    import registrovanKorisnik
    registrovanKorisnik.registrovanKorisnik()

ucitavanjeHotela()