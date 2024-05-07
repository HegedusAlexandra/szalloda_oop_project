from datetime import datetime

""" _____________Szálloda,Szoba,Egyágyas,Kétágyas,Foglalás Osztályok létrehozása___________"""
today = datetime.today().date()

class Szoba :
    def __init__ (self,szoba_szam,szoba_ar,szoba_tipus):
        self.szoba_szam = szoba_szam
        self.szoba_ar = szoba_ar
        self.szoba_tipus = szoba_tipus

    def __str__(self):
        return f"Szobaszám: {self.szoba_szam}, Ár: {self.szoba_ar} Ft Tipus: {self.szoba_tipus}"

class EgyagyasSzoba(Szoba):
    def __init__(self, szoba_szam):
        super().__init__(szoba_ar=10000, szoba_szam=szoba_szam ,szoba_tipus='egyágyas szoba')

class KetagyasSzoba(Szoba):  
    def __init__(self, szoba_szam):
        super().__init__(szoba_ar=20000, szoba_szam=szoba_szam ,szoba_tipus='kétágyas szoba')

class Szalloda :
    group_name = 'GDE PROJECT EVENT GROUP'
    def __init__(self,hotel_name,hotel_szobak,hotel_foglalasok):
        self.hotel_name = hotel_name
        self.hotel_szobak = hotel_szobak
        self.hotel_foglalasok = hotel_foglalasok

    def hozzaadas_szoba (self,szoba):
        self.hotel_szobak.append(szoba)


    def hozzaadas_foglalas(self, uj_foglalas, isIncoming):
        for foglalas in self.hotel_foglalasok:
            if foglalas.foglalt_szoba_szam == uj_foglalas.foglalt_szoba_szam and foglalas.foglalt_datum == uj_foglalas.foglalt_datum:
                print('*********************************')
                print("A szoba már foglalt ezen a napon.")
                print('*********************************')
                return
        for szoba in self.hotel_szobak:
            if szoba.szoba_szam == uj_foglalas.foglalt_szoba_szam:
                self.hotel_foglalasok.append(uj_foglalas)
                if not isIncoming:
                    print('*********************************')
                    print(f"Sikeres foglalás! A szoba ára a kért napra : {szoba.szoba_ar} Ft.")
                    print('*********************************')
                    self.mutasd_foglalasok()
                return
        
        print('*********************************')
        print("A megadott szobaszám nem létezik a szállodában.")
        print('*********************************')

    def torles_foglalas(self, szoba_szam_torles, foglalas_datum_torles, foglalo_nev_torles):
        for foglalas in self.hotel_foglalasok:
            if foglalas.foglalt_szoba_szam == szoba_szam_torles and foglalas.foglalt_datum == foglalas_datum_torles and foglalas.foglalo_neve == foglalo_nev_torles:
                self.hotel_foglalasok.remove(foglalas)
                print('*********************************')
                print("A foglalás sikeresen törölve lett.")
                print('*********************************')
                self.mutasd_foglalasok()
                return
        print('*********************************')
        print("A megadott foglalás nem található.")
        print('*********************************')

    def mutasd_szobak(self):
        if len(self.hotel_szobak) > 0 : 
            print('*********************************')
            for szoba in self.hotel_szobak:            
                print(szoba)
            print('*********************************')
        else:
            print('*********************************')
            print('Jövőre építünk szobákat,nézz vissza akkor')
            print('*********************************')
            

    def mutasd_foglalasok(self):
        if len(self.hotel_foglalasok) > 0:
            print('*********************************')
            for foglalas in self.hotel_foglalasok:            
                print(foglalas)
            print('*********************************')
        else:
             print('*********************************')
             print('Még rengeteg lehetőség közül választhatsz') 
             print('*********************************')
            
class Foglalas:
    def __init__ (self,datum,szoba_szam,kinek):
          self.foglalt_datum = datum
          self.foglalt_szoba_szam = szoba_szam
          self.foglalo_neve = kinek  

    def __str__(self):
        return f"Szobaszám: {self.foglalt_szoba_szam}, Foglalás időpontja: {self.foglalt_datum}, Foglaló neve: {self.foglalo_neve},"

""" ________Szálloda rendszer inicializálása__________"""    
            
def sys_initialization():
    szalloda_kek_hexagon = Szalloda('Kék Hexagon',[],[])
    szalloda_kek_hexagon.hozzaadas_szoba(EgyagyasSzoba(1))
    szalloda_kek_hexagon.hozzaadas_szoba(KetagyasSzoba(3))
    szalloda_kek_hexagon.hozzaadas_szoba(KetagyasSzoba(6))
    szalloda_kek_hexagon.hozzaadas_foglalas(Foglalas(datetime.strptime('2024-06-22', "%Y-%m-%d").date(),3,'Bulgakov'),True)
    szalloda_kek_hexagon.hozzaadas_foglalas(Foglalas(datetime.strptime('2024-07-12', "%Y-%m-%d").date(),1,'Lovecraft'),True)
    szalloda_kek_hexagon.hozzaadas_foglalas(Foglalas(datetime.strptime('2024-08-18', "%Y-%m-%d").date(),3,'Herbert'),True)
    szalloda_kek_hexagon.hozzaadas_foglalas(Foglalas(datetime.strptime('2024-06-22', "%Y-%m-%d").date(),6,'Vonnegut'),True)
    szalloda_kek_hexagon.hozzaadas_foglalas(Foglalas(datetime.strptime('2024-08-17', "%Y-%m-%d").date(),6,'Marquez'),True)
    return szalloda_kek_hexagon

szalloda_kek_hexagon = sys_initialization()

def main(inOrOut):
    

    print(f"\n1. Foglalás\n2. Lemondás\n3. Foglalások listázása\n4. Szobák listázása\n5. {inOrOut}")
    try:
        choice = int(input("Válassz egy műveletet: "))  
    except:
        print('wrong key')
        main('Belépés')           

    if inOrOut == 'Belépés':
        if choice == 5 :
            print('Köszönjük! Viszontlátásra!' if inOrOut == 'Kilépés' else 'Isten Hozott!')
            main('Belépés' if inOrOut == 'Kilépés' else 'Kilépés')
        else:
            print('*********************************')
            print('Kérlek lépj be a rendszerbe')
            print('*********************************')
            main('Belépés')        
    else:
        if choice == 1:
                datum_str = input('Adjon meg egy dátumot (YYYY-MM-DD formátumban): ')
                szoba_szam = int(input('Adja meg a szobaszámot: '))
                nev = input('Adja meg a nevét: ')
                
                try:
                    datum = datetime.strptime(datum_str, "%Y-%m-%d").date()
                    if datum < today:
                        print('*********************************')
                        print("A foglalás dátuma nem lehet a múltban.")
                        print('*********************************')
                    else:
                        szalloda_kek_hexagon.hozzaadas_foglalas(Foglalas(datum, szoba_szam, nev), False)
                except ValueError:
                    print("Hibás dátum formátum.")

                main('Kilépés')
        elif choice == 2:
                datum_str_tor = input('Adjon meg egy dátumot (YYYY-MM-DD formátumban) amit törölni szeretne: ')
                szoba_szam = int(input('Adja meg a szobaszámot amit törölni szeretne: '))
                nev = input('Adja meg a nevét: ')

                try:
                    datum = datetime.strptime(datum_str_tor, "%Y-%m-%d").date()
                    if datum < today:
                        print('*********************************')
                        print("A foglalás dátuma nem lehet a múltban.")
                        print('*********************************')
                    else:
                        szalloda_kek_hexagon.torles_foglalas(szoba_szam,datum,nev)
                except ValueError:
                    print("Hibás dátum formátum.")
                
                main('Kilépés')
        elif choice == 3:
                szalloda_kek_hexagon.mutasd_foglalasok()
                main('Kilépés')
        elif choice == 4:
                szalloda_kek_hexagon.mutasd_szobak()
                main('Kilépés')
        else:
            print('Köszönjük! Viszontlátásra!' if inOrOut == 'Kilépés' else 'Isten Hozott!')
            main('Belépés' if inOrOut == 'Kilépés' else 'Kilépés')

if __name__ == "__main__":
    main('Belépés')

