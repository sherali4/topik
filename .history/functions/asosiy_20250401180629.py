from docx import Document


def replace_text_in_doc(doc_path, file_path, old_text, new_text):
    doc = Document(doc_path)

    # Barcha paragraf ichidan qidirib, almashtirish
    for para in doc.paragraphs:
        if old_text in para.text:
            para.text = para.text.replace(old_text, new_text)

    # O'zgarishlarni saqlash
    doc.save(doc_path)
    print(f"'{file_path}' so'zi '{new_text}' ga almashtirildi!")


# Foydalanish:
# replace_text_in_doc("example.docx", "Eski so'z", "Yangi so'z")
