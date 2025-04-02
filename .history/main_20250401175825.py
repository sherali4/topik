from docx import Document
from functions.asosiy import replace_text_in_doc

# Open the existing Word document
doc = Document("example.docx")

# Add a new paragraph
# doc.add_paragraph("This is a newly added paragraph.")

# Save changes
doc.save("example.docx")

print("Text added successfully!")
