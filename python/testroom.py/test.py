from fpdf import FPDF


pdf_w=210
pdf_h=297

class PDF(FPDF):

    def write_char(self,label):
       
        self.set_xy(50,80.0)    
        self.set_text_color(76.0, 32.0, 250.0)
        self.set_font('Arial', '', 12)
        self.multi_cell(0,10,label)


pdf=PDF()
pdf.add_page()
pdf.write_char("A")
pdf.output('test.pdf','F')