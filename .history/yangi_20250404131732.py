
from functions import func


class Filltopic:

    def __init__(self, template_file, new_file, tarmoq, list_excel):
        self.template_file = template_file
        self.new_file = new_file
        self.tarmoq = tarmoq
        self.joriy_yil = 2025
        self.list_excel = list_excel
        self.birinchi_foydalanish = True
        self.ustun_shu_yil = self.ustun_shu_yil()
        self.ustun_utgan_yil = self.ustun_utgan_yil()
        self.ustun_utgan_yildan_oldin = self.ustun_utgan_yildan_oldin()

    def ustun_shu_yil(self):
        return func.ustun_nomi(self.tarmoq, str(self.joriy_yil))

    def ustun_utgan_yil(self):
        return func.ustun_nomi(self.tarmoq, str(self.joriy_yil-1))

    def ustun_utgan_yildan_oldin(self):
        return func.ustun_nomi(self.tarmoq, )


qurilish = Filltopic('example.docx', '400.docx', 'qurilish', 'ulush')
