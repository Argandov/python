#!/usr/bin/python
import pdfx
import pprint
from PyPDF2 import PdfFileReader, PdfFileWriter
import sys


# reading pdf file
try:
    file_in = sys.argv[1]
    pdf = pdfx.PDFx(file_in)
except:
    print(f"[X] Usage: {sys.argv[0]} my_pdf.pdf")
    sys.exit(1)
delimiter = "*"*10 + str(pdf) + "*"*10

banner='''
WHAT THIS DOES:
    This script has 2 parts: One, it reads the metadata of any pdf file
    if "Y" is chosen when prompted, it will create a new pdf file with
    the new metadata (Generated when prompted)
'''
print(banner)

def _outfile_process(file_in):
    # converts input_file.pdf into input_fileNEW.pdf
    root_filename = file_in.split(".")
    out_root_filename = root_filename[0] + "NEW"
    return out_root_filename + "." + root_filename[1]

def _read_metadata(file, pdf):
    meta = pdf.get_metadata()
    return meta

def _write_metadata(file, pdf):
    file_in = open(file, 'rb')
    pdf_reader = PdfFileReader(file_in)
    metadata = pdf_reader.getDocumentInfo()
    print("[i] OLD METADATA: " + "*"*20)
    pprint.pprint(metadata)
    print("******** END ***********")    
    if input("Write new file and override metadata? (Y/N)") != "Y":
        sys.exit("Exiting...")

    pdf_writer = PdfFileWriter()
    pdf_writer.appendPagesFromReader(pdf_reader)
    author = input("> Author: ")
    title = input("> Title: ")
    producer = input("> producer: ")
    pdf_writer.addMetadata({
        '/Author': author,
        '/Title': title,
        '/Producer': producer
    })
    # New key/values for metadata apart from the default ones given by this script
    # It loops just for fun, adding more metadata key pairs
    while input("[++] Custom new fields? (Y)") == "Y":
        custom_key = input("> Field name (One word): ")
        if len(custom_key.split(" ")) > 1:
            print("EXITING!")
        custom_value = input(str(custom_key) + ": ")
        custom_key = "/" + custom_key
        custom_value = "/" + custom_value
        # Append custom key/values
        pdf_writer.addMetadata({
            str(custom_key): str(custom_value)
            })
    # Prepares new name for new file
    file_out_name = _outfile_process(file)
    # Opens new file
    file_out = open(file_out_name, 'wb')
    pdf_writer.write(file_out)

    file_in.close()
    file_out.close()

_write_metadata(file_in, pdf)
