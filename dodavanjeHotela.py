def dodavanjeHotela():

    print(' Potrebno je uneti sledece podatke:\n')
    sifra = input(' ID u obliku sestocifrenog broja: ')
    naziv = input(' Naziv hotela: ')
    adresa = input(' Adresa: ')
    sobe = input(' Lista soba: ')
    bazen = input(' Bazen (da li postoji ili ne): ')
    restoran = input(' Restoran (da li postoji ili ne): ')
    prosecnaOcena = input(' Unesite prosecnu ocenu: ')
    obrisan = 'False'
    file = open('hoteli.txt','a') 
    noviHotel = sifra + ',' + naziv + ',' + adresa + ',' + sobe + ',' + bazen + ',' + restoran + ',' + prosecnaOcena + ',' + obrisan
    file.write('\n' + noviHotel) 
    file.close()
    print('\n\n Potrebno je dodati sobe u hotel!')
    while True:
        unos = input('\n Unesite DA za nastavak ili enter za izlaz: ')
        if unos == '':
            print('\n Uspesno ste dodali sobe!')
            print('\n Hotel je uspesno dodat. ')
            print(' \n Da li zelite:\n ')
            print(' 1. Dodate jos jedan hotel? \n 2. Izadjete? ')
            while True:
                x = input('\n Unesi broj 1 ili 2: ')
                if x == '1':
                    dodavanjeHotela()
                    break
                elif x == '2':
                    import administrator
                    administrator.administrator()
                    break
                else:
                    print('Uneli ste pogresan broj, pokusajte ponovo! ')
            break
        else:
            print('\n')
            idSobe = input(' Unesi ID sobe (u obliku sestocifrenog broja): ')
            brojSoba = input(' Unesi broj sobe: ')
            brojKreveta = input(' Unesi broj kreveta: ')
            tipSobe = input(' Unesi tip sobe: ')
            klima = input(' Unesi da li soba ima klimu (da ili ne): ')
            tv = input(' Unesi da li soba ima TV (da ili ne): ')
            cena = input(' Unesi cenu po nocenju: ')
            file = open('sobe.txt','a')
            noveSobe = sifra + ',' + idSobe + ',' + brojSoba + ',' + brojKreveta + ',' + tipSobe + ',' + klima + ',' + tv + ',' + cena
            file.write('\n' + noveSobe)
            file.close()

