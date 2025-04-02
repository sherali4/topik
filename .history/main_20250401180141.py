from docx import Document
from functions.asosiy import replace_text_in_doc

# Open the existing Word document
doc = Document("example.docx")

replace_text_in_doc('example.docx', '2025_raqam', )
# Add a new paragraph
# doc.add_paragraph("This is a newly added paragraph.")

# Save changes
doc.save("357.docx")

print("Text added successfully!")
