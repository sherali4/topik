from transliterate import translit
from func import replace_text_in_doc, eng_katta, eng_kup_hudud, from_excel, eng_kup, kiril_to_latin

# period
replace_text_in_doc("example.docx", "357.docx", "period_uz", "mart")
replace_text_in_doc("357.docx", "357.docx", "period_ru", "март")
# Foydalanish:
replace_text_in_doc("357.docx", "357.docx", "2025_raqam", "100")
replace_text_in_doc("357.docx", "357.docx", "2023_raqam", from_excel('B4'))
replace_text_in_doc("357.docx", "357.docx", "2024_raqam", from_excel('C4'))


# Yangi kalitlar ro‘yxati (agar kerak bo‘lsa, uzunligini o‘zgartirish)
new_keys = ['Andijon viloyati', 'Buxoro viloyati', 'Jizzax viloyati', 'Qashqadaryo viloyati', 'Navoiy viloyati', 'Namangan viloyati',
            'Samarqand viloyati', 'Surxondaryo viloyati', 'Sirdaryo viloyati', 'Toshkent shahri', 'Toshkent viloyati', "Farg'ona viloyati", 'Xorazm viloyati', "Qoraqalpog'iston Respublikasi"]



Engkup('357.docx', '357.docx', '@h1', 'C', 1).hudud
Engkup('357.docx', '357.docx', '@k1', 'C', 1).kursatkich
Engkup('357.docx', '357.docx', '@h2', 'C', 2).hudud
Engkup('357.docx', '357.docx', '@k2', 'C', 2).kursatkich
