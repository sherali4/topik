
from fu
class Filltopic:

    def __init__(self, template_file, new_file, tarmoq, list_excel):
        self.template_file = template_file
        self.new_file = new_file
        self.tarmoq = tarmoq
        self.list_excel = list_excel
        self.birinchi_foydalanish = True

    def ustun_manzili(self):
        pass


qurilish = Filltopic('example.docx', '400.docx', 'qurilish', 'ulush')
