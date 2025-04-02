from docx import Document

from func import replace_text_in_doc, eng_katta, eng_kup_hudud, from_excel

# period
replace_text_in_doc("example.docx", "357.docx", "period_uz", "mart")
replace_text_in_doc("357.docx", "357.docx", "period_ru", "март")


# Foydalanish:
replace_text_in_doc("357.docx", "357.docx", "2025_raqam", "100")
replace_text_in_doc("357.docx", "357.docx", "2023_raqam", from_excel('B4'))
replace_text_in_doc("357.docx", "357.docx", "2024_raqam", from_excel('C4'))




# Foydalanish
# sorted_data = eng_kup_hudud("B", 5, 18, new_keys)
# print(sorted_data)

print(eng_katta(eng_kup_hudud("B", 5, 18, new_keys), 1, 1))
print(eng_katta(eng_kup_hudud("B", 5, 18, new_keys), 1, 2))
print(eng_katta(eng_kup_hudud("B", 5, 18, new_keys), 1, 3))
