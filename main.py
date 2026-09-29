class Katta_son:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def natija(self):
        katta = self.a
        if self.b > katta:
            katta = self.b
        if self.c > katta:
            katta = self.c
        if self.d > katta:
            katta = self.d
        return katta

class Ismlar:
    def __init__(self):
        self.ismlar = []

    def malumot_olish(self):
        for i in range(1, 6):
            ism = input(f"{i}-ismni kiriting: ")
            self.ismlar.append(ism)

    def natija(self):
        print(self.ismlar)

son1 = 11
son2 = 33
son3 = 86
son4 = 100

obyekt1 = Katta_son(son1, son2, son3, son4)
print("Eng katta son", obyekt1.natija())

obyekt2 = Ismlar()
obyekt2.malumot_olish()
obyekt2.natija()


 