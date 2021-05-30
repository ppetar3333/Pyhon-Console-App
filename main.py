# aplikacija za rezervaciju soba u hotelu

def izbor():
    
    print('\n\n\n************ Dobro dosli ************ \n\n') 
    print(' Da li zelite da se:\n')
    print(' 1. Registrujete?')  
    print(' 2. Ulogujete?') 
    print(' 3. Izadjete? \n')

def main():

    izbor()
    while True:
        x = input(' Unesite broj od 1 do 3: ')
        #korisnik, recepcioner (register)
        if x == '1':
            print('\n*** Izabrali ste da zelite da se regisistrujete! ***')
            import registrujSe
            registrujSe.registrujSe()
            break
        #korisnik, recepcioner, administrator (login)
        elif x == '2':
            print('\n*** Izabrali ste da zelite da se ulogujete! *** \n')
            import ulogujSe
            ulogujSe.ulogujSe()
            break
        elif x == '3':
            print('\n Uspesno ste izasli iz aplikacije.\n')   
            exit()
            break
        else:
            print('\n Uneli ste pogresan broj, molim vas pokusajte ponovo.\n')

main()






