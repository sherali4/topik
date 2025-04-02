from docx import Document


# Open the existing Word document
doc = Document("example.docx")

# Add a new paragraph
doc.add_paragraph("This is a newly added paragraph.")

# Save changes
doc.save("example.docx")

print("Text added successfully!")