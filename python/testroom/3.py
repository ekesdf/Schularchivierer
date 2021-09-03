# Python program to convert
# text file to pdf file


from fpdf import FPDF

# save FPDF() class into
# a variable pdf
pdf = FPDF(unit="cm",format="A4")

# Add a page
pdf.add_page()
pdf.set_margins(1.0,1.0,1.0)

# set style and size of font
# that you want in the pdf
pdf.set_font("Arial", size = 15)

# open the text file in read mode
f = open("test.txt", "r")

# insert the texts in pdf
for index, x in enumerate(f):

	pdf.write(0.5, txt = x)#, ln = 1, align = 'L')

# save the pdf with name .pdf
pdf.output("mygfg.pdf")
