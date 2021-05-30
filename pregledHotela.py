
def pregled():

    file = open('hoteli.txt','r')
    ceoFajl = file.readlines()
    print('\n\n\n                          *** Spisak svih hotela! *** ')
    print('\n\n  Naziv            | Adresa                 | Bazen   | Restoran  | Ocena  |')
    print('  --------------------------------------------------------------------------')
    for red in ceoFajl:
        a,b,c,d,e,f,g,h = red.strip().split(',')
        print(
        ' ', b,   ' ' * (15-len(b)), # ime moze da ima max 15 slova
        '|', c,  ' ' * (21-len(c)),
        '|', e,  ' ' * (5-len(e)),
        ' |',f, ' ' * (8-len(f)),
        '|', g,   ' ' * (5-len(g)),'|')
    print('\n\n')
    file.close()

    import registrovanKorisnik
    registrovanKorisnik.registrovanKorisnik()

