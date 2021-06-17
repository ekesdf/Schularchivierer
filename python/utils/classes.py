class Image: 

    def __init__(self,image_name,shape,liste_textregions): 
        
        self.textregions        = liste_textregions
        self.number_textregions = len(self.textregions)
        self.name               = image_name
        self.width              = shape[0]
        self.height             = shape[1]

class Textregion:

    def __init__(self,image_name,textregion_name,textregion_bbox,scale,dist):

        self.chars        = []
        self.number_chars = len(self.chars)
        self.image_name   = image_name
        self.name         = textregion_name
        self.scale        = scale
        self.width_scale  = scale[0]
        self.height_scale = scale[1]
        self.dist         = dist
        self.dist_left    = dist[0]
        self.dist_top     = dist[1]
        self.x1           = textregion_bbox[0]
        self.y1           = textregion_bbox[1]
        self.x2           = textregion_bbox[2]
        self.y2           = textregion_bbox[3]
        self.bbox         = textregion_bbox

class Char:

    def __init__(self,image_name,textregion_name,textregion_bbox,textregion_scale,dist,char_bbox,label):

        self.image_name = image_name
        self.textregion = textregion_name
        self.label      = label
        self.scale      = textregion_scale
        self.textregion_bbox = textregion_bbox

        if self.scale[0] <= 1.0 and self.scale[1] <= 1.0:

            self.normalized_x1 = char_bbox[0]-dist[0]+textregion_bbox[0]
            self.normalized_y1 = char_bbox[1]-dist[1]+textregion_bbox[1]
            self.normalized_x2 = char_bbox[2]-dist[0]+textregion_bbox[0]
            self.normalized_y2 = char_bbox[3]-dist[1]+textregion_bbox[1]

        elif self.scale[0] > 1.0 and self.scale[1] <= 1.0:

            self.normalized_x1 = ((char_bbox[0]-dist[0])*self.scale[0])+textregion_bbox[0]
            self.normalized_y1 = char_bbox[1]-dist[1]+textregion_bbox[1]
            self.normalized_x2 = ((char_bbox[2]-dist[0])*self.scale[0])+textregion_bbox[0]
            self.normalized_y2 = char_bbox[3]-dist[1]+textregion_bbox[1]

        elif self.scale[0] <= 1.0 and self.scale[1] > 1.0:

            self.normalized_x1 = char_bbox[0]-dist[0]+textregion_bbox[0]
            self.normalized_y1 = ((char_bbox[1]-dist[1])*self.scale[1])+textregion_bbox[1]
            self.normalized_x2 = char_bbox[2]-dist[0]+textregion_bbox[0]
            self.normalized_y2 = ((char_bbox[3]-dist[1])*self.scale[1])+textregion_bbox[1]

        elif self.scale[0] > 1.0 and self.scale[1] > 1.0:

            self.normalized_x1 = ((char_bbox[0]-dist[0])*self.scale[0])+textregion_bbox[0]
            self.normalized_y1 = ((char_bbox[1]-dist[1])*self.scale[1])+textregion_bbox[1]
            self.normalized_x2 = ((char_bbox[2]-dist[0])*self.scale[0])+textregion_bbox[0]
            self.normalized_y2 = ((char_bbox[3]-dist[1])*self.scale[1])+textregion_bbox[1]

        if self.normalized_x1 < 0: self.normalized_x1 = 0
        if self.normalized_y1 < 0: self.normalized_y1 = 0
        if self.normalized_x2 < 0: self.normalized_x2 = 0
        if self.normalized_y2 < 0: self.normalized_y2 = 0

        self.bbox = [self.normalized_x1, self.normalized_y1, self.normalized_x2, self.normalized_y2]

class Grid:

    def __init__(self,rows,cols,cell_w,cell_h):

        self.number_rows = rows
        self.number_cols = cols
        self.grid  = []

    def make_grid(self):

        for _ in range(self.number_rows):
            
            row = []
        
            for _ in range(self.number_cols): row.append(" ")

            self.grid.append(row)
        
        return self.grid

class Cell:

    def __init__(self,char,row,col):

        self.Char = char
        self.row  = row
        self.col  = col


