#New function HOW TO MERGE FILES IN PYTHON
from PyPDF2 import PdfMerger

merger = PdfMerger()
merger.append("file1.pdf")
merger.append("file2.pdf")

with open("merged15.pdf", "wb") as f:
    merger.write(f)

    merger.close()

#/////////////////////////////////////////////
merger = PdfMerger()
merger.append("file1.pdf", pages=(0,3))
merger.append("file2.pdf", pages=(2,4))

with open("merged25.pdf", "wb") as f:
    merger.write(f)

    merger.close()
