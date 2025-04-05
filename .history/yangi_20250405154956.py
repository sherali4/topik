from functions.classes import Filltopic
# sozlamalar


# qurilish
qurilish = Filltopic('example.docx', '400.docx', 'sanoat', 'ulush')
qurilish.matn('period_uz', 'mart')
qurilish.matn('period_ru', 'март')
qurilish.respublika('2023_raqam', '2023')
qurilish.respublika('2024_raqam', '2024')
qurilish.respublika('2025_raqam', '2025')
qurilish.kursatkich('@k1', 1)
qurilish.kursatkich('@k2', 2)
qurilish.hudud('@h1', 1)
qurilish.hudud('@h2', 2)
qurilish.hudud_ru('@hr1', 1)
qurilish.hudud_ru('@hr2', 2)
# run.add_break(WD_BREAK.LINE)
qurilish = Filltopic('shablon/qurilish_1.docx',
                     'yangi/qurilish1.docx', 'qurilish', 'ulush')

qurilish.matn('period_uz', 'mart')
qurilish.matn('period_ru', 'март')
qurilish.respublika('2025_raqam', '2025')

for i in range(15):
    qurilish.hudud('@h'+str(i) + '@', i)
    qurilish.hudud_ru('@hr'+str(i) + '@', i)
    qurilish.kursatkich('@k'+str(i) + '@', i)
# doc = Document('shablon/qurilish_1.docx')
