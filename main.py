import PyPDF2

pdf_file = '1711423095898.pdf'
a = PyPDF2.PdfReader(pdf_file)

text = ""

for i, page in enumerate(a.pages):
    try:
        text += page.extract_text()
    except Exception as e:
        print(f"Error extracting text from page {i+1}: {e}")

if text:
    with open("text.txt", "w", encoding='utf-8') as f:
        f.write(text)
        print("Text extracted successfully and saved to text.txt")
else:
    print("No text extracted from the PDF.")
