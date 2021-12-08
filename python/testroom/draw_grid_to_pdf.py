from fpdf import FPDF

pdf_w = 210
pdf_h = 297

row_count = 29
col_count = 21

row_height = pdf_h / row_count
col_width = pdf_w / col_count

pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", size=15)

pdf.text(col_width, row_height - (row_height / 2), "a")

for row_index in range(row_count): pdf.line(0, row_height * row_index, pdf_w, row_height * row_index)

for col_index in range(col_count): pdf.line(col_width * col_index, 0, col_width * col_index, pdf_h)

pdf.output('test.pdf', 'F')
