from docx import Document
from functions.asosiy import replace_text_in_doc

# Open the existing Word document
# doc = Document("example.docx")

replace_text_in_doc('example.docx', '2025_raqam', '100')


print("Text added successfully!")
