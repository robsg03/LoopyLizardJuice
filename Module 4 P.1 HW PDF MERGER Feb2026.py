from PyPDF2 import PdfReader, PdfWriter
pdf_file_path = 'Learning to Read and Write.pdf'
pdf = PdfReader(pdf_file_path)

writer = PdfWriter()

pages = [0, 2] #Highlighting only Page 1 and Page 3 to copy to output

print(len(pdf.pages)) #Tells the user how many pages are in the PDF

for page_num in pages:
    writer.add_page(pdf.pages[page_num])

with open ('output.pdf', 'wb') as out:
    writer.write(out)

print('PDF file has been split')

