from PyPDF2 import PdfReader, PdfWriter
pdf_file_path = 'Newman, J. Case Study Final Draft.docx.pdf'
pdf = PdfReader(pdf_file_path)

writer = PdfWriter()

print(len(pdf.pages)) #Tells the user how many pages are in the PDF

for page_num in range(11,18): #Pulls the certain selected range of pages only - in this case: 12 - 18
    writer.add_page(pdf.pages[page_num])

with open ('newoutput.pdf', 'wb') as out:
    writer.write(out)

print('PDF file has been split')

