from fpdf import FPDF

class PDF(FPDF):

    def write_char(self,label,x,y):
       
        self.set_xy(x,y)    
        self.set_text_color(76.0, 32.0, 250.0)
        self.set_font('helvetica', '', 12)
        self.multi_cell(0,10,label)



