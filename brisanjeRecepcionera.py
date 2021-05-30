recepcioneri = []
def ucitaj():
    file = open('korisnici.txt','r')
    ceoFajl = file.readlines()
    for red in ceoFajl:
        recepcioner = red_u_recnik(red.strip())
        if not recepcioner['obrisan']:
            recepcioneri.append(recepcioner)
    return recepcioneri 
    
def str_to_bool(x):
    if x == 'True':
        return True
    else:
        return False

def red_u_recnik(red):
    recPodaci = red.split(',')
    recepcioner = {'username': recPodaci[0], 'password': recPodaci[1], 'ime': recPodaci[2],'prezime': recPodaci[3], 'brojTel': recPodaci[4], 'email': recPodaci[5], 'sifra': recPodaci[6], 'uloga' : recPodaci[7], 'obrisan': str_to_bool(recPodaci[8])}
    return recepcioner

def upisIzmena(recepcioner):
    podaci = recepcioner['username']+','+recepcioner['password']+','+recepcioner['ime']+','+recepcioner['prezime'] + ',' + recepcioner['brojTel'] + ',' + recepcioner['email']+','+recepcioner['sifra'] + ','+recepcioner['uloga'] + ',' + str(recepcioner['obrisan'])
    return podaci

def snimi(recepcioneri):
    file = open('korisnici.txt', 'w')
    for recepcioner in recepcioneri:
        file.write(upisIzmena(recepcioner))
        file.write('\n')
    file.close()

def brisanjeRec():
    username = input('\n Unesi username Recepcionera: ')
    for recepcioner in recepcioneri:
        if recepcioner['username'] == username:
            recepcioner['obrisan'] = True
    snimi(recepcioneri)
    print('\n Recepcioner je uspesno obrisan! \n')
    while True:
        print(' Da li zelite da: \n')
        print(' 1. Obrisete jos jednog recepcionera? \n 2. Izadjete? \n')
        izbor = input(' Unesite broj od 1 do 2: ')
        if izbor == '1':
            brisanjeRec()
            break
        elif izbor == '2':
            import administrator
            administrator.administrator()
            break
        else:
            print(' Uneli ste pogresan broj! Molimo vas pokusajte ponovo! ')
ucitaj()
