def sveSobe():
    file = open('sobe.txt','r')
    ceoFajl = file.readlines()
    for red in ceoFajl:
        a,b,c,d,e,f,g,h = red.strip().split(',')
        print(
        ' ', b, ' ' * (7 - len(b)),
        '|', c,   ' ' * (9-len(c)),
        '|', d,  ' ' * (12-len(d)),
        '|', e,  ' ' * (13-len(e)),
        ' |',f, ' ' * (5-len(f)),
        '|', g,   ' ' * (3-len(g)),
        '|', h, ' ' * (9-len(h)),'|')
    print('\n')
    file.close()

def zaglavlje():
    print('\n\n  ID sobe  | Broj Sobe  | Broj kreveta  | Tip             | Klima  | Tv   | Cena       |')
    print('  --------------------------------------------------------------------------------------')

def brojSobe(unos1):
    file = open('sobe.txt','r')
    ceoFajl = file.readlines()
    for red in ceoFajl:
        a,b,c,d,e,f,g,h = red.strip().split(',')
        if unos1 == c:
            print(
            ' ', b, ' ' * (7 - len(b)),
            '|', c,   ' ' * (9-len(c)),
            '|', d,  ' ' * (12-len(d)),
            '|', e,  ' ' * (13-len(e)),
            ' |',f, ' ' * (5-len(f)),
            '|', g,   ' ' * (3-len(g)),
            '|', h, ' ' * (9-len(h)),'|')
    file.close()

def brojKreveta(unos2):
    file = open('sobe.txt','r')
    ceoFajl = file.readlines()
    for red in ceoFajl:
        a,b,c,d,e,f,g,h = red.strip().split(',')
        if unos2 == d:
            print(
            ' ', b, ' ' * (7 - len(b)),
            '|', c,   ' ' * (9-len(c)),
            '|', d,  ' ' * (12-len(d)),
            '|', e,  ' ' * (13-len(e)),
            ' |',f, ' ' * (5-len(f)),
            '|', g,   ' ' * (3-len(g)),
            '|', h, ' ' * (9-len(h)),'|')
    file.close()

def tipSobe(unos3):
    file = open('sobe.txt','r')
    ceoFajl = file.readlines()
    for red in ceoFajl:
        a,b,c,d,e,f,g,h = red.strip().split(',')
        if unos3 == e:
            print(
            ' ', b, ' ' * (7 - len(b)),
            '|', c,   ' ' * (9-len(c)),
            '|', d,  ' ' * (12-len(d)),
            '|', e,  ' ' * (13-len(e)),
            ' |',f, ' ' * (5-len(f)),
            '|', g,   ' ' * (3-len(g)),
            '|', h, ' ' * (9-len(h)),'|')
    file.close()

def klima(unos4):
    file = open('sobe.txt','r')
    ceoFajl = file.readlines()
    for red in ceoFajl:
        a,b,c,d,e,f,g,h = red.strip().split(',')
        if unos4 == f:
            print(
            ' ', b, ' ' * (7 - len(b)),
            '|', c,   ' ' * (9-len(c)),
            '|', d,  ' ' * (12-len(d)),
            '|', e,  ' ' * (13-len(e)),
            ' |',f, ' ' * (5-len(f)),
            '|', g,   ' ' * (3-len(g)),
            '|', h, ' ' * (9-len(h)),'|')
    file.close()

def tv(unos5):
    file = open('sobe.txt','r')
    ceoFajl = file.readlines()
    for red in ceoFajl:
        a,b,c,d,e,f,g,h = red.strip().split(',')
        if unos5 == g:
            print(
            ' ', b, ' ' * (7 - len(b)),
            '|', c,   ' ' * (9-len(c)),
            '|', d,  ' ' * (12-len(d)),
            '|', e,  ' ' * (13-len(e)),
            ' |',f, ' ' * (5-len(f)),
            '|', g,   ' ' * (3-len(g)),
            '|', h, ' ' * (9-len(h)),'|')
    file.close()

def cena(unos6):
    file = open('sobe.txt','r')
    ceoFajl = file.readlines()
    for red in ceoFajl:
        a,b,c,d,e,f,g,h = red.strip().split(',')
        if unos6  == h:
            print(
            ' ', b, ' ' * (7 - len(b)),
            '|', c,   ' ' * (9-len(c)),
            '|', d,  ' ' * (12-len(d)),
            '|', e,  ' ' * (13-len(e)),
            ' |',f, ' ' * (5-len(f)),
            '|', g,   ' ' * (3-len(g)),
            '|', h, ' ' * (9-len(h)),'|')
    file.close()

def poJednomKriterijumu():
    
    print(' 1. Po broju sobe')
    print(' 2. Po broju kreveta')
    print(' 3. Po tipu sobe')
    print(' 4. Klima (da li postoji ili ne)')
    print(' 5. TV (da li postoji ili ne)')
    print(' 6. Po ceni za jedno nocenje')
    print(' 7. Vratite se unazad')
    while True:
        izbor = input('\n Unesi broj od 1 do 8: ')
        if izbor == '1':
            print('\n Izabrali ste pretragu po broju sobe !\n ')
            unos1 = input(' Unesi broj soba: ')
            if unos1 == '':
                zaglavlje()
                sveSobe()
                poJednomKriterijumu()
            zaglavlje()
            brojSobe(unos1)
            break
        elif izbor == '2':
            print('\n Izabrali ste pretragu po broju kreveta !\n ')
            unos2 = input(' Unesi broj kreveta: ')
            if unos2 == '':
                zaglavlje()
                sveSobe()
                poJednomKriterijumu()
            zaglavlje() 
            brojKreveta(unos2)
            break
        elif izbor == '3':
            print('\n Izabrali ste pretragu po tipu sobe !\n ')
            unos3 = input(' Unesi tip sobe: ')
            if unos3 == '':
                zaglavlje()
                sveSobe()
                poJednomKriterijumu()
            zaglavlje()
            tipSobe(unos3)
            break
        elif izbor == '4':
            print('\n Izabrali ste pretragu po klimi (da li postoji ili ne) !\n ')
            unos4 = input(' Unesi klimu (da ili ne): ')
            if unos4 == '':
                zaglavlje()
                sveSobe()
                poJednomKriterijumu()
            zaglavlje()
            klima(unos4)
            break
        elif izbor == '5':
            print('\n Izabrali ste pretragu po TV-u (da li postoji ili ne) !\n ')
            unos5 = input(' Unesi TV (da ili ne): ')
            if unos5 == '':
                zaglavlje()
                sveSobe()
                poJednomKriterijumu()
            zaglavlje()
            tv(unos5)
            break
        elif izbor == '6':
            print('\n Izabrali ste pretragu po ceni ! \n')
            unos6 = input(' Unesi cenu po nocenju: ' )
            if unos6 == '':
                zaglavlje()
                sveSobe()
                poJednomKriterijumu()
            zaglavlje()
            cena(unos6)
            break
        elif izbor == '7':
            pretragaSobe()
            break
        else:
            print(' Greska, uneli ste pogresan broj! Molimo vas pokusajte ponovo! ')
    print('\n\n Da li zelite da: \n\n 1. Pokusate opet?\n 2. Izadjete?\n 3. Vratite se unazad? \n')
    while True:
        y = input(' Unesi broj od 1 do 3: ')
        if y == '1':
            poJednomKriterijumu()
            break
        elif y == '2':
            import recepcioner
            recepcioner.recepcioner() 
            break
        elif y == '3':
            pretragaSobe()
            break
        else:
            print('\n Uneli ste pogresan broj, molimo vas pokusajte ponovo!')


def poViseKriterijuma():
    
    print('\n Molimo vas popunite sledece podatke!\n ')
    unos1 = input(' Unesi broj soba: ')
    unos2 = input(' Unesi broj kreveta: ')
    unos3 = input(' Unesi tip sobe: ')
    unos4 = input(' Unesi klimu (da ili ne): ')
    unos5 = input(' Unesi TV (da ili ne): ')
    unos6 = input(' Unesi cenu po nocenju: ' )
    unos7 = input(' Unesi dostupnost sobe (datum od do): ')
    zaglavlje()
    brojSobe(unos1)
    brojKreveta(unos2)
    tipSobe(unos3)
    klima(unos4)
    tv(unos5)
    cena(unos6)
    if unos1 == '' and unos2 == '' and unos3 == '' and unos4 == '' and unos5 == '' and unos6 == '':
        sveSobe()
    print('\n')
    print('\n\n Da li zelite da: \n\n 1. Pokusate opet?\n 2. Izadjete?\n 3. Vratite se unazad? \n')
    while True:
        y = input(' Unesi broj od 1 do 3: ')
        if y == '1':
            poViseKriterijuma()
            break
        elif y == '2':
            import recepcioner
            recepcioner.recepcioner() 
            break
        elif y == '3':
            pretragaSobe()
            break
        else:
            print('\n Uneli ste pogresan broj, molimo vas pokusajte ponovo!')

def pretragaSobe():

    print('\n Sada je potrebno da izaberete:\n ')
    print(' 1. Pretraga soba po jednom kriterijumu \n 2. Visekriterijumska pretraga soba\n 3. Izlaz \n')
    while True:
        x = input(' Unesi broj od 1 do 3: ')
        if x == '1':
            print('\n*** Izabrali ste pretragu po jednom kriterijumu! ***\n')
            poJednomKriterijumu()
            break
        elif x == '2':
            print('\n*** Izabrali ste pretragu po vise kriterijuma! ***\n')
            poViseKriterijuma()
            break
        elif x == '3':
            import recepcioner
            recepcioner.recepcioner()
            break
        else:
            print('\n Uneli ste pogresan broj, pokusajte ponovo')

