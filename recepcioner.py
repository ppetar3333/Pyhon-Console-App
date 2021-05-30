def recepcioner():

    print('\nZbog vase pozicije recepcionera, imate sledece mogucnosti: \n')
    print(' 1. Pretraga soba ') 
    print(' 2. Pretraga rezervacija') 
    print(' 3. Izvestavanje')
    print(' 4. Odjavite se')
    while True:
        x = input('\nIzaberite broj od 1 do 3: ')
        if x == '1':
            print('\n*** Izabrali ste pretragu soba! ***\n')
            import pretragaSoba 
            pretragaSoba.pretragaSobe()
            break
        elif x == '2':
            print('\n*** Izabrali ste da zelite da pretrazite rezervacije! ***\n')
            import pretragaRezervacija 
            break
        elif x == '3':
            print('\n*** Izabrali ste izvestavanje! ***\n')
            import izvestavanje 
            izvestavanje.izvestavanje()
            break
        elif x == '4':
            print('\n*** Uspesno ste se odjavili! ***\n')
            import main
            main.main()
            break
        else:
            print('Uneli ste pogresan broj, molim vas pokusajte ponovo.')

        
