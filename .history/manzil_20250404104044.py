from pprint import pprint
from openpyxl.utils import get_column_letter


def manzil(name, period):
    # Ko‘rsatkichlar ro‘yxati
    korsatkichlar = [
        'yaim', 'sanoat', 'qishloq_xujaligi', 'investitsiya',
        'qurilish', 'chakana_savdo', 'xizmat', 'yuk_tashish',
        'yuk_aylanmasi', 'yulovchi_tashish', 'yulovchi_aylanmasi',
        'eksport', 'import'
    ]

    # Yillar
    yillar = ['2023', '2024', '2025']

    # Lug'atni yaratamiz
    manzil = {}

    # A dan boshlab barcha ustunlarni belgilang
    start_index = 2  # A = 1

    for i, nom in enumerate(korsatkichlar):
        manzil[nom] = {}
        for j, yil in enumerate(yillar):
            col_index = start_index + i * len(yillar) + j
            col_letter = get_column_letter(col_index)
            manzil[nom][yil] = col_letter

    # Natijani chiqarish
    # pprint(manzil)
    return manzil[name][period]


printmanzil('qurilish', '2024')
