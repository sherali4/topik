from docx import Document
from functions.asosiy import replace_text_in_doc

replace_text_in_doc('example.docx', '357.docx', '2025_raqam', '100')
replace_text_in_doc('example.docx', '357.docx', '2024_raqam', '75')
replace_text_in_doc('example.docx', '357.docx', '2023_raqam', '50')


print("Text added successfully!")
