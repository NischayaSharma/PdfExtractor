from PyPDF2 import PdfFileWriter, PdfFileReader;

inputpdf = PdfFileReader(open("Basix.pdf", "rb"));

for i in range(inputpdf.numPages):
    output = PdfFileWriter();
    page = inputpdf.getPage(i);
    output.addPage(page);
    print page.extractText();
    with open("./pdfs/Basix_page_%s.pdf" % i, "wb") as outputStream:
        output.write(outputStream);
