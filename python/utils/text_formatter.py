import sys
sys.path.insert(0, "/home/yolo/Schreibtisch/Schularchivierer")


from python.utils.classes import Grid

grid = Grid(30,50).grid

def put_line(grid,text,start_col,row):
    
    if start_col +len(text) > len(grid[0]): return grid

    else: 
        
        for char_index in range(len(text)): grid[row-1][start_col-1+char_index] = text[char_index]

        return grid



def formatter(liste_chars):

    liste_groups = []
    
    group = []

    old = "normalized 0.jpg"

    for char in liste_chars:

        if char.textregion != old:
            
            liste_groups.append(group)
            group = []
            group.append(char)
            old = char.textregion

        else: group.append(char)

    liste_groups.append(group)
