import re
from func import replace_text_in_doc, eng_katta, eng_kup_hudud, from_excel, eng_kup

# period
# replace_text_in_doc("example.docx", "357.docx", "period_uz", "mart")
# replace_text_in_doc("357.docx", "357.docx", "period_ru", "март")
#
#
# Foydalanish:
# replace_text_in_doc("357.docx", "357.docx", "2025_raqam", "100")
# replace_text_in_doc("357.docx", "357.docx", "2023_raqam", from_excel('B4'))
# replace_text_in_doc("357.docx", "357.docx", "2024_raqam", from_excel('C4'))


# Yangi kalitlar ro‘yxati (agar kerak bo‘lsa, uzunligini o‘zgartirish)
new_keys = ['Andijon viloyati', 'Buxoro viloyati', 'Jizzax viloyati', 'Qashqadaryo viloyati', 'Navoiy viloyati', 'Namangan viloyati',
            'Samarqand viloyati', 'Surxondaryo viloyati', 'Sirdaryo viloyati', 'Toshkent shahri', 'Toshkent viloyati', "Farg'ona viloyati", 'Xorazm viloyati', "Qoraqalpog'iston Respublikasi"]

# Foydalanish
# sorted_data = eng_kup_hudud("B", 5, 18, new_keys)
# print(sorted_data)

# print(eng_katta(eng_kup_hudud("B", 5, 18, new_keys), 1, 1))
# print(eng_katta(eng_kup_hudud("B", 5, 18, new_keys), 1, 2))
# print(eng_katta(eng_kup_hudud("B", 5, 18, new_keys), 1, 3))
#
#
# print(eng_kup('C', 5, 18, new_keys, 1, hudud=0))
# print(eng_kup('C', 5, 18, new_keys, 2, hudud=1))
# print(eng_kup('C', 5, 18, new_keys, 3, hudud=1))


class Engkup:

    def __init__(self, ustun, urin):
        self.ustun = ustun.upper()
        self.urin = urin
        self.dan = 5
        self.gacha = self.dan + 13
        self.hududlar = ['Andijon viloyati', 'Buxoro viloyati', 'Jizzax viloyati', 'Qashqadaryo viloyati', 'Navoiy viloyati', 'Namangan viloyati',
                         'Samarqand viloyati', 'Surxondaryo viloyati', 'Sirdaryo viloyati', 'Toshkent shahri', 'Toshkent viloyati', "Farg'ona viloyati", 'Xorazm viloyati', "Qoraqalpog'iston Respublikasi"]

    @property
    def hudud(self):
        kursatkich = eng_kup_hudud(
            self.ustun, self.dan, self.gacha, self.hududlar)
        # kursatkich2 = eng_kup('C', self.dan, self.gacha, self.hududlar, 1, hudud=0)
        kursatkich2 = eng_katta(kursatkich, 1, urin=self.urin)
        return kursatkich2

    @property
    def kursatkich(self):
        kursatkich = eng_kup_hudud(
            self.ustun, self.dan, self.gacha, self.hududlar)
        kursatkich2 = eng_katta(kursatkich, 0, urin=self.urin)
        return kursatkich2


print(Engkup('c', 1).kursatkich)

name = 'ш'

# Kiril harflarini qidirish
if isinstance(name, str) and re.search(r'[а-яА-Я]', value):
    print(f"O'zgaruvchi nomi: {name}, Qiymati: {value}")
