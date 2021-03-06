import sys
sys.path.insert(0, "/home/yolo/Schreibtisch/Schularchivierer")


from python.utils.classes import Grid

grid = Grid(30,50)

def put_line(grid,text,start_col,row):
    
    if start_col + len(text) <= len(grid[0]): 
        
        for char_index in range(len(text)): grid[row-1][start_col-1+char_index] = text[char_index]


    if start_col +len(text) > len(grid[0]): return grid



def make_xpos_char_dictionary(liste_x_values,liste_chars):

    return {
        liste_x_values[index]: liste_chars[index]
        for index in range(len(liste_x_values))
    }

def formatter(liste_chars):

    liste_groups = []
    group = []

    text = ""
    old = "normalized 0.jpg"

    for char in liste_chars:

        if char.textregion != old:
            
            liste_groups.append(group)
            group = []
            old = char.textregion

        group.append(char)
    liste_groups.append(group)

    liste_x_values = [char.normalized_x1 for char in liste_groups[0]]
    dictionary = make_xpos_char_dictionary(liste_x_values,liste_groups[0])

    liste_x_values = sorted(liste_x_values)

    last_x = liste_x_values[0]

    for x in liste_x_values: 

        if abs(x-last_x) > 100: text  += " "

        text += dictionary[x].label
        last_x = x 

    start_x = dictionary[liste_x_values[0]].normalized_x1
    start_y = dictionary[liste_x_values[0]].normalized_y1

    return text ,start_x, start_y