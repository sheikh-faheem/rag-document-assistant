from pypdf import PdfReader

pdf_path = "data\document\Sheikh Faheem Ahmed offer letter.pdf"

reader = PdfReader(pdf_path)

text = ""

for page in reader.pages:
    page_text = page.extract_text()

    if page_text:
        text += page_text

print("PDF loaded successfully!")
print("Number of pages:", len(reader.pages))
print("Number of characters:", len(text))

print("\n--- PDF CONTENT ---\n")
print(text)