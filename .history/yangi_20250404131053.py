
from functions import func


class Filltopic:

    def __init__(self, template_file, new_file, tarmoq, list_excel):
        self.template_file = template_file
        self.new_file = new_file
        self.tarmoq = tarmoq
        self.list_excel = list_excel
        self.birinchi_foydalanish = True


    def ustun_manzili(self):
        return func.ustun_nomi(self.tarmoq, '2025')


qurilish = Filltopic('example.docx', '400.docx', 'qurilish', 'ulush')
print(qurilish.ustun_manzili())
