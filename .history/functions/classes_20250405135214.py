from functions import func
from lugat import viloyatlar
from docx import Document


class Filltopic:

    def __init__(self, template_file, new_file, tarmoq, list_excel):
        self.template_file = template_file
        self.new_file = new_file
        self.tarmoq = tarmoq
        self.yil = '2025'
        self.dan = 5
        self.gacha = 5+13
        self.list_excel = list_excel
        self.birinchi_foydalanish = True
        self.ustun1 = func.ustun_nomi(self.tarmoq, str('2025'))

    def ustun(self, yil):
        self.yil = yil
        return func.ustun_nomi(self.tarmoq, str(self.yil))

    def respublika(self, tag, yil):
        ustun_manzili = self.ustun(yil)
        birinchi = self.birinchi_foydalanish
        self.birinchi_foydalanish = False
        yacheyka = ustun_manzili + '4'
        value = func.from_excel(self.list_excel, yacheyka)
        if birinchi:
            tempfile = self.template_file
        else:
            tempfile = self.new_file
        return func.replace_text_in_doc(tempfile, self.new_file, tag, value)

    def matn(self, tag, matn):
        birinchi = self.birinchi_foydalanish
        self.birinchi_foydalanish = False
        if birinchi:
            tempfile = self.template_file
        else:
            tempfile = self.new_file
        return func.replace_text_in_doc(tempfile, self.new_file, tag, matn)

    def hudud(self, tag, urin):
        birinchi = self.birinchi_foydalanish
        self.birinchi_foydalanish = False
        if birinchi:
            tempfile = self.template_file
        else:
            tempfile = self.new_file

        kursatkich = func.eng_kup_hudud(
            self.ustun1, self.dan, self.gacha, viloyatlar.viloyatlar_uz, self.list_excel)
        kursatkich2 = func.eng_katta(kursatkich, 1, urin=urin)
        func.replace_text_in_doc(tempfile, self.new_file,
                                 tag, kursatkich2)

    def hudud_ru(self, tag, urin):
        birinchi = self.birinchi_foydalanish
        self.birinchi_foydalanish = False
        if birinchi:
            tempfile = self.template_file
        else:
            tempfile = self.new_file

        kursatkich = func.eng_kup_hudud(
            self.ustun1, self.dan, self.gacha, viloyatlar.viloyatlar_uz, self.list_excel)
        kursatkich2 = func.eng_katta(kursatkich, 1, urin=urin)
        kursatkich2 = viloyatlar.viloyatlar_ru[kursatkich2]
        func.replace_text_in_doc(tempfile, self.new_file,
                                 tag, kursatkich2)

    def kursatkich(self, tag, urin):
        birinchi = self.birinchi_foydalanish
        self.birinchi_foydalanish = False
        if birinchi:
            tempfile = self.template_file
        else:
            tempfile = self.new_file
        kursatkich = func.eng_kup_hudud(
            self.ustun1, self.dan, self.gacha, viloyatlar.viloyatlar_uz, self.list_excel)
        kursatkich2 = func.eng_katta(kursatkich, 0, urin=urin)
        func.replace_text_in_doc(tempfile, self.new_file,
                                 tag, kursatkich2)

    def get_style(self, tag):
        doc = Document(self.template_file)
        source_style = None  # To store the style from "@hudud"
        # Step 1: Find "@hudud" and save its style
        for para in doc.paragraphs:
            for run in para.runs:
                if tag in run.text:
                    source_style = {
                        "bold": run.bold,
                        "italic": run.italic,
                        "underline": run.underline,
                        "font_name": run.font.name,
                        "font_size": run.font.size,
                        "font_color": run.font.color.rgb if run.font.color else None
                    }
                    return source_style
                    # break

            if source_style:
                break
    def set_style