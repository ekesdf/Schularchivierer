from fpdf import FPDF

pdf_w = 210
pdf_h = 297

pdf = FPDF()
pdf.add_page()

pdf.set_font("helvetica", style="U")
pdf.cell(50, 40, txt="Hallo")
pdf.set_font("helvetica")
pdf.cell(80, 40, txt="Hallo")

pdf.output('test.pdf', 'F')
