from typing import List


class Obserwator:
    def aktualizuj(self, pacjent: 'Pacjent'):
        raise NotImplementedError("Metoda aktualizuj musi być zaimplementowana")


class Pacjent:
    def __init__(self, nazwisko: str):
        self.obserwatorzy: List[Obserwator] = []
        self.stan: str = ""
        self.nazwisko: str = nazwisko

    def dodaj(self, obserwator: Obserwator):
        if obserwator not in self.obserwatorzy:
            self.obserwatorzy.append(obserwator)

    def usun(self, obserwator: Obserwator):
        if obserwator in self.obserwatorzy:
            self.obserwatorzy.remove(obserwator)

    def powiadom(self):
        for obserwator in self.obserwatorzy:
            obserwator.aktualizuj(self)

    def zmienStan(self, stan: str):
        self.stan = stan
        self.powiadom()


class Stomatolog(Obserwator):
    def aktualizuj(self, pacjent: Pacjent):
        print(f"Stomatolog został powiadomiony o zmianie stanu pacjenta {pacjent.nazwisko} na: {pacjent.stan}")


class Chirurg(Obserwator):
    def aktualizuj(self, pacjent: Pacjent):
        print(f"Chirurg został powiadomiony o zmianie stanu pacjenta {pacjent.nazwisko} na: {pacjent.stan}")


pacjent1 = Pacjent("Kowalski")
pacjent2 = Pacjent("Nowak")

stomatolog = Stomatolog()
chirurg = Chirurg()

pacjent1.dodaj(stomatolog)
pacjent1.dodaj(chirurg)

pacjent2.dodaj(stomatolog)
pacjent2.dodaj(chirurg)

pacjent1.zmienStan("Stan krytyczny")
pacjent2.zmienStan("Stan stabilny")
