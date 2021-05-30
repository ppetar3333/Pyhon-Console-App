import os

#prikaz svih hotela
def sviHoteli():

    file = open('hoteli.txt','r')
    ceoFajl = file.readlines()
    print('\n\n  Naziv            | Adresa                 | Bazen   | Restoran  | Ocena  |')
    print('  --------------------------------------------------------------------------')
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

#brisanje i prikaz
def brisanje():

    file_r = open('hoteli.txt','r')
    file_w = open('pomoc.txt','w')
    unos = input(' \n Unesite ime hotela koji hoces da obrises: ')
    s = ' '
    while (s):
        s = file_r.readline()
        L = s.split(',')
        if len(s) > 0:
            if L[1] != unos:
                file_w.write(s)
    file_w.close()
    file_r.close()
    os.remove('hoteli.txt')
    os.rename('pomoc.txt','hoteli.txt')
    print('\n *** Hotel je uspesno obrisan! *** \n')
    print(' Da li hocete da: \n\n 1. Izbrisete neki drugi hotel? \n 2. Izadjete? \n')
    while True:
        x = input(' Unesi broj od 1 do 2: ')
        if x == '1':
            brisanje()
            break
        elif x == '2':
            import administrator
            administrator.administrator()
            break
        else:
            print('\n Uneli ste pogresan broj! Pokusajte ponovo.')
            
def brisanjeJednogHotela():
    print('\n ***** Ispod mozete pogledati sve hotele. ***** \n')
    sviHoteli()
    brisanje()
