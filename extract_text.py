import PyPDF2

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text += page.extract_text()
    return text

# Example usage:
pdf_path = 'your_file.pdf'
raw_text = extract_text_from_pdf(pdf_path)
print(raw_text)
