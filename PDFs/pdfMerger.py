import sys

import PyPDF2
import sys

inputs = sys.argv[1:]


def pdfMerger(pdfFiles):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdfFiles:
        merger.append(pdf)
    merger.write('super.pdf')


pdfMerger(inputs)
