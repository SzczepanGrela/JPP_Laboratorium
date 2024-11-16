# problem podziału paczek
# programowanie proceduralne

def podziel_paczki(wagi, max_waga):

    #sortowanie paczek malejąco
    wagi_sort = sorted(wagi, reverse = True)
    kursy = []

    # sprawdzenie czy paczka nie przekroczy wartosci max
    for waga in wagi_sort:
        if waga > max_waga:
            raise ValueError(f"Paczka o wadze {waga} przekracza maksymalną dozwoloną wagę kursu {max_waga} kg")


    # iteracja po dostępnych paczkach
    for waga in wagi_sort:
        dodano = False
        for kurs in kursy:
            if sum(kurs) + waga <= max_waga:
                kurs.append(waga)
                dodano = True
                break
        # jesli nie mozna dodac paczki do kursu utworz nowy kurs
        if not dodano:
            kursy.append([waga])

    return len(kursy), kursy


if __name__ == "__main__":

    wagi = [5,5,5,5,5,2]
    max_waga = 10

    liczba_kursow, kursy = podziel_paczki(wagi, max_waga)
    print(f"Liczba kursów: {liczba_kursow}")
    for i, kurs in enumerate(kursy,1):
        print(f"Kursu {i}: {kurs} - suma wag: {sum(kurs)} kg")