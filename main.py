import uuid


class Basket:
    def __init__(self, sana):
        self.id = str(uuid.uuid4())[:8]
        self.sana = sana
        self.mahsulotlar = {}

    def add(self, product_id, nomi, miqdor):
        if product_id in self.mahsulotlar:
            self.mahsulotlar[product_id] = (nomi, self.mahsulotlar[product_id][1] + miqdor)
        else:
            self.mahsulotlar[product_id] = (nomi, miqdor)
        print(f"{nomi} ({product_id}) savatga {miqdor} dona qo'shildi.")

    def remove(self, product_id, miqdor):
        if product_id in self.mahsulotlar:
            nomi, mavjud_miqdor = self.mahsulotlar[product_id]
            if mavjud_miqdor > miqdor:
                self.mahsulotlar[product_id] = (nomi, mavjud_miqdor - miqdor)
                print(f"{nomi} ({product_id}) dan {miqdor} dona olib tashlandi.")
            else:
                del self.mahsulotlar[product_id]
                print(f"{nomi} ({product_id}) butunlay olib tashlandi.")
        else:
            print(f"Mahsulot ID {product_id} savatda mavjud emas.")

    def show(self):
        if not self.mahsulotlar:
            print("Savat bo'sh.")
        else:
            print("Savat tarkibi:")
            for product_id, (nomi, miqdor) in self.mahsulotlar.items():
                print(f"- {nomi} ({product_id}): {miqdor} dona")

    def calc(self, narxlar):
        jami = 0
        for product_id, (nomi, miqdor) in self.mahsulotlar.items():
            if product_id in narxlar:
                jami += narxlar[product_id] * miqdor
        print(f"Jami summa: {jami} so'm")
        return jami


def main():
    savat = Basket("2025-02-12")
    narxlar = {"1": 5000, "2": 7000}

    while True:
        print("\n1. Mahsulot qo'shish")
        print("2. Mahsulot olib tashlash")
        print("3. Savatni ko'rish")
        print("4. Jami hisoblash")
        print("5. Chiqish")
        tanlov = input("Tanlovingiz: ")

        if tanlov == "1":
            product_id = input("Mahsulot ID: ")
            nomi = input("Mahsulot nomi: ")
            miqdor = int(input("Miqdor: "))
            savat.add(product_id, nomi, miqdor)
        elif tanlov == "2":
            product_id = input("Mahsulot ID: ")
            miqdor = int(input("Olib tashlanadigan miqdor: "))
            savat.remove(product_id, miqdor)
        elif tanlov == "3":
            savat.show()
        elif tanlov == "4":
            savat.calc(narxlar)
        elif tanlov == "5":
            break
        else:
            print("Noto'g'ri tanlov, qayta urinib ko'ring!")


if __name__ == "__main__":
    main()
