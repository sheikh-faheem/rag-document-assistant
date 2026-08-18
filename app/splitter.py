from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter


# 1. Read the PDF
pdf_path = "data\document\Sheikh Faheem Ahmed offer letter.pdf"

reader = PdfReader(pdf_path)

text = ""

for page in reader.pages:
    page_text = page.extract_text()

    if page_text:
        text += page_text


# 2. Create the text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)


# 3. Split the text
chunks = text_splitter.split_text(text)


# 4. Display results
print("Total characters:", len(text))
print("Total chunks:", len(chunks))

print("\n--- FIRST CHUNK ---\n")
print(chunks[0])