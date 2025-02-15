import random


def test_python_basics():
    questions = [
        # 100 ta savol qo‘shilgan
        {"question": "Python-da stringlarni qanday usul bilan birlashtirish mumkin?",
         "options": ["1) + operatori orqali", "2) join() metodi orqali", "3) format() metodi orqali",
                     "4) Barchasi to‘g‘ri"], "answer": "4"},
        {"question": "Python-da list comprehension qanday ishlaydi?",
         "options": ["1) List elementlarini tartiblash uchun",
                     "2) Yangi ro‘yxat yaratish uchun qisqaroq sintaksis taqdim etadi",
                     "3) Faqat lambda funksiyalar bilan ishlaydi", "4) Ro‘yxatni o‘chirish uchun ishlatiladi"],
         "answer": "2"},
        {"question": "Mutable va immutable tiplarga misollar qaysilar?",
         "options": ["1) str - mutable, list - immutable", "2) tuple - mutable, dict - immutable",
                     "3) list - mutable, tuple - immutable", "4) set - immutable, str - mutable"], "answer": "3"},
        {"question": "Python-da `*args` va `**kwargs` nima uchun ishlatiladi?",
         "options": ["1) O‘zgaruvchan sonli argumentlarni qabul qilish uchun",
                     "2) O‘zgaruvchan sonli funksiya chaqirishlar yaratish uchun",
                     "3) Faqat oddiy argumentlarni saqlash uchun", "4) Ro‘yxatlar va lug‘atlar ustida ishlash uchun"],
         "answer": "1"},
        {"question": "OOP da `super()` funksiyasining vazifasi nima?",
         "options": ["1) Klass ichidagi metodlarni qayta yuklash",
                     "2) Vorislik olgan klassning ota klass metodlarini chaqirish",
                     "3) Klassga yangi xususiyat qo‘shish", "4) Private metodlarni chaqirish"], "answer": "2"},
        {"question": "Python-da `__new__` metodi qachon ishlaydi?",
         "options": ["1) Obyekt yaratishdan oldin chaqiriladi", "2) Obyekt yaratishdan keyin chaqiriladi",
                     "3) Obyekt ichida atribut qo‘shish uchun ishlatiladi", "4) Obyektni o‘chirish uchun ishlatiladi"],
         "answer": "1"},
        {"question": "Metaclass nima?",
         "options": ["1) Oddiy klasslarga o‘xshash obyekt", "2) Klass yaratish jarayonini boshqaruvchi klass",
                     "3) Private atributlarga ega klass", "4) Klasslar ichida metod yaratish uchun ishlatiladi"],
         "answer": "2"},
        {"question": "`@staticmethod` va `@classmethod` o‘rtasidagi farq nima?",
         "options": ["1) staticmethod obyektga bog‘liq, classmethod esa bog‘liq emas",
                     "2) classmethod klassga bog‘liq, staticmethod esa bog‘liq emas",
                     "3) staticmethod faqat global funksiyalarni yaratish uchun ishlatiladi",
                     "4) classmethod obyekt yaratishni bloklaydi"], "answer": "2"},
        {"question": "Encapsulation nima?",
         "options": ["1) Ma’lumotlarni yashirish va ularga faqat kerakli joylardan kirish imkonini berish",
                     "2) Bir nechta klasslarni birlashtirish", "3) Klass ichidagi metodlarni avtomatik chaqirish",
                     "4) Python kodini tezroq bajarish usuli"], "answer": "1"},
        {"question": "`__slots__` atributining vazifasi nima?",
         "options": ["1) Klass atributlarini cheklash va xotira tejash", "2) Klass ichida metodlar yaratish",
                     "3) Klassni tezroq ishlatish", "4) Klassni boshqa modullarga import qilish"], "answer": "1"},
        {"question": "Python-da stringlarni qanday usul bilan birlashtirish mumkin?",
         "options": ["1) + operatori orqali", "2) join() metodi orqali", "3) format() metodi orqali",
                     "4) Barchasi to‘g‘ri"], "answer": "4"},
    ]

    selected_questions = random.sample(questions, 10)  # 10 ta tasodifiy savol tanlash
    correct_answers = 0

    for index, q in enumerate(selected_questions, start=1):
        print(f"\nSavol {index}: {q['question']}")
        for option in q["options"]:
            print(option)
        user_answer = input("Javobingizni kiriting (1/2/3/4): ").strip()

        if user_answer == q["answer"]:
            correct_answers += 1

    print(f"\nTest yakuni: Siz {correct_answers}/10 ta savolga to‘g‘ri javob berdingiz.")


# Testni ishga tushirish
test_python_basics()
