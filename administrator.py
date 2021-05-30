def uvod():

    print('\n Zbog vas pozicije, mozete da obavljate sledece funkcije:\n ')
    print(' 1. Dodavanje novih hotela')
    print(' 2. Dodavanje recepcionera u hotele')
    print(' 3. Azuriranje hotela')
    print(' 4. Pretraga recepcionera')
    print(' 5. Brisanje hotela') 
    print(' 6. Brisanje recepcionera')
    print(' 7. Izadjite iz aplikacije')
    print(' 8. Odjavite se')

def administrator():

    uvod()
    while True:
        x = input('\n Unesite broj od 1 do 8: ')
        if x == '1': #DODAVANJEhotela
            print('\n *** Izabrali ste da zelite da dodate novi hotel! ***\n')
            import dodavanjeHotela
            dodavanjeHotela.dodavanjeHotela()
            break
        elif x == '2': #DODAVANJErecepcionera
            print('\n *** Izabrali ste da zelite da dodate novog recepcionera u hotel! ***\n')
            import dodavanjeRecepcionera
            dodavanjeRecepcionera.dodavanje()
            break   
        elif x == '3': #AZURIRANJEhotela
            print('\n *** Izabrali ste da zelite da azurirate hotel! ***\n')
            import azuriranjeHotela
            azuriranjeHotela.azuriranje()
            break
        elif x == '4': #PRETRAGArecepcionera
            print('\n *** Izabrali ste da hocete da pretrazite recepcionera! ***\n')
            import pretragaRecepcionera 
            pretragaRecepcionera.pretragaRec()
            break
        elif x == '5': #BRISANJEhotela
            print('\n *** Izabrali ste da zelite da izbrisete hotel! ***\n')
            import brisanjeHotela 
            brisanjeHotela.brisanjeJednogHotela()
            break
        elif x == '6': #BRISANJErecepcionera
            print('\n *** Izabrali ste da zelite da izbrisete recepcionera! ***\n')
            import brisanjeRecepcionera 
            brisanjeRecepcionera.brisanjeRec()
            break
        elif x == '7':
            print('\n*** Uspesno ste izasli iz aplikacije! ***\n')
            exit()
            break
        elif x == '8':
            print('\n*** Uspesno ste se odjavili sa aplikacije! ***\n')
            import main
            main.main()
            break
        else:
            print(' Uneli ste pogresan broj, molim vas ponovo unesite broj. ')

