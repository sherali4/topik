
from functions import func


class Filltopic:

    def __init__(self, template_file, new_file, tarmoq, list_excel):
        self.template_file = template_file
        self.new_file = new_file
        self.tarmoq = tarmoq
        self.yil = '2025'
        self.list_excel = list_excel
        self.birinchi_foydalanish = True
        self.ustun_shu_yil = self.ustun_shu_yil()
        self.ustun_utgan_yil = self.ustun_utgan_yil()
        self.ustun_utgan_yildan_oldin = self.ustun_utgan_yildan_oldin()

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

    def hudud(self):
        kursatkich = func.eng_kup_hudud(
            self.ustun, self.dan, self.gacha, self.hududlar, self.kitob)
        kursatkich2 = eng_katta(kursatkich, 1, urin=self.urin)
        func.replace_text_in_doc(self.file_nomi, self.file_nomi,
                                 self.uzgarmas, kursatkich2)

    def hudud_ru(self):
        kursatkich = func.eng_kup_hudud(
            self.ustun, self.dan, self.gacha, self.hududlar, self.kitob)
        kursatkich2 = eng_katta(kursatkich, 1, urin=self.urin)
        kursatkich2 = self.hududlar_ru[kursatkich2]
        replace_text_in_doc(self.file_nomi, self.file_nomi,
                            self.uzgarmas, kursatkich2)

    @property
    def kursatkich(self):
        kursatkich = eng_kup_hudud(
            self.ustun, self.dan, self.gacha, self.hududlar, self.kitob)
        kursatkich2 = eng_katta(kursatkich, 0, urin=self.urin)
        replace_text_in_doc(self.file_nomi, self.file_nomi,
                            self.uzgarmas, kursatkich2)


qurilish = Filltopic('example.docx', '400.docx', 'qurilish', 'ulush')
qurilish.matn('period_uz', 'mart')
qurilish.matn('period_ru', 'март')
qurilish.respublika('2023_raqam', '2023')
qurilish.respublika('2024_raqam', '2024')
qurilish.respublika('2025_raqam', '2025')
