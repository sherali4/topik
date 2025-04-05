
from functions import func


class Filltopic:

    def __init__(self, template_file, new_file, tarmoq, list_excel):
        self.template_file = template_file
        self.new_file = new_file
        self.tarmoq = tarmoq
        self.list_excel = list_excel
        self.birinchi_foydalanish = True
        self.ustun_shu_yil = self.ustun_shu_yil()
        self.ustun_utgan_yil. 

    def ustun_shu_yil(self):
        return func.ustun_nomi(self.tarmoq, '2025')

    def ustun_utgan_yil(self):
        return func.ustun_nomi(self.tarmoq, '2024')

    def ustun_uttgan_yildan_oldin(self):
        return func.ustun_nomi(self.tarmoq, '2023')


qurilish = Filltopic('example.docx', '400.docx', 'qurilish', 'ulush')
print(qurilish.ustun_manzili())
