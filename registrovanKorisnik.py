def mogucnostiKorisnika():

    print('\nPosto ste korisnik imate sledece opcije: \n')
    print(' 1. Pregled Hotela')
    print(' 2. Pretraga Hotela')
    print(' 3. Prikaz Najbolje Ocenjenih Hotela')
    print(' 4. Pregled rezervacije')
    print(' 5. Kreiranje rezervacije')
    print(' 6. Odjavite se')

#glavni
def registrovanKorisnik():

    mogucnostiKorisnika()
    while True:
        x = input('\nIzaberite broj od 1 do 6: ')
        if x == '1':
            print('\n*** Izabrali ste pregeled hotela! ***\n')
            import pregledHotela 
            pregledHotela.pregled()
            break
        elif x == '2': 
            print('\n*** Izabrali ste pretragu hotela! *** \n')
            import pretragaHotela 
            pretragaHotela.pretraga()
            break
        elif x == '3': 
            print('\n*** Izabrali ste prikaz najbolje ocenjenih hotela! *** \n')
            import oceneHotela 
            oceneHotela.najboljeOceneHotela()
            break
        elif x == '4': 
            print('\n*** Izabrali ste pregled rezervacije! *** \n')
            import pregledRezervacija
            pregledRezervacija.pregledSvihRezervacija()
            break
        elif x == '5': 
            print('\n*** Izabrali ste da zelite da kreirate rezervaciju! *** \n')
            import kreiranjeRez
            kreiranjeRez.kreiranjeRezervacije()
            break
        elif x == '6': 
            print('\n** Uspesno ste se odjavili! ***\n')
            import main
            main.main()
            break
        else:
            print('Uneli ste pogresan broj, molim vas pokusajte ponovo.')

