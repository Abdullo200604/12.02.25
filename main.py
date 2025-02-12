class Basket:
    def __init__(self, sana, mahsulotlar=None):
        self.sana = sana
        self.mahsulotlar = mahsulotlar if mahsulotlar else {}

    def add(self, mahsulot, miqdor):
        if mahsulot in self.mahsulotlar:
            self.mahsulotlar[mahsulot] += miqdor
        else:
            self.mahsulotlar[mahsulot] = miqdor
        print(f"{mahsulot} savatga {miqdor} dona qo'shildi.")

    def remove(self, mahsulot, miqdor):
        if mahsulot in self.mahsulotlar:
            if self.mahsulotlar[mahsulot] > miqdor:
                self.mahsulotlar[mahsulot] -= miqdor
                print(f"{mahsulot} dan {miqdor} dona olib tashlandi.")
            else:
                del self.mahsulotlar[mahsulot]
                print(f"{mahsulot} butunlay olib tashlandi.")
        else:
            print(f"{mahsulot} savatda mavjud emas.")

    def show(self):
        if not self.mahsulotlar:
            print("Savat bo'sh.")
        else:
            print("Savat tarkibi:")
            for mahsulot, miqdor in self.mahsulotlar.items():
                print(f"- {mahsulot}: {miqdor} dona")

    def calc(self, narxlar):
        jami = 0
        for mahsulot, miqdor in self.mahsulotlar.items():
            if mahsulot in narxlar:
                jami += narxlar[mahsulot] * miqdor
        print(f"Jami summa: {jami} so'm")
        return jami

savat = Basket("2025-02-12")
savat.add("Olma", 3)
savat.add("Banan", 5)
savat.remove("Olma", 2)
savat.show()
narxlar = {"Olma": 5000, "Banan": 7000}
savat.calc(narxlar)
