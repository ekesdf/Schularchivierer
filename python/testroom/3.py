# Python program to convert
# text file to pdf file

from fpdf import FPDF

# save FPDF() class into
# a variable pdf
pdf = FPDF(unit="pt", format="A4")

# Add a page
pdf.add_page()
pdf.set_margins(0.5, 1.0, 0.5)
# pdf.set_auto_page_break(False)

# set style and size of font
# that you want in the pdf
pdf.set_font("Courier", size=14)

# open the text file in read mode
f = open("test.txt", "r")

# insert the texts in pdf
for x in f:
    pdf.write(14, txt=x)  #, ln = 1, align = 'L')

# save the pdf with name .pdf
pdf.output("mygfg.pdf")
