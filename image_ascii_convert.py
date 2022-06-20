import math
from PIL  import Image
import numpy as np


#############################################

reverse_colors=True
photo='''12.jpg'''

#############################################



def image_ascii_convert(photo,reverse):
    #seting up a greyscale with ascii signs that will later replace the number greyscale values with 
    grey_scale = " .:-=+*#%@"
    #setting up an empty string for making an reversed string with greyscale in ascii 
    reverse_greyscale=''
    
    #reversing the string of greyscale ascii by iterating on it from the very last one to the first one 
    #picking the reversed or the previous string of greyscale ascii is dependend on the value of reverse value in function which can either be true or false 
    #and by that switching between two grey scales and basically reversing colors 
    
    if reverse==True:
        for i in range(len(grey_scale)):
            reverse_greyscale=reverse_greyscale+grey_scale[(len(grey_scale))-(i+1)]
        grey_scale=reverse_greyscale
    #initialazing image to work with 
    image =Image.open(photo)

    #image.show()
    #making an array 3d array containing rgb values of every pixel
    final_list=[]
    np_image = np.asarray(image)
    
    #print(np_image)
   #now converting the rgb array that is 3D into the 2D array that have only greyscale values 
   
    for i in np_image:
        list_x=[]
        for j in i:
            
            c=int(j[0])+int(j[1])+int(j[2])
            list_x.append(c/3)

        final_list.append(list_x)
    #print(final_list)
    #now given the greyscale 2D matrix script converts the matrix's numerical values into ascii signs
    #numerical value can be anywere from 0 to 255 but there are  n numbers of ascii codes depending on the scale (in my case there are 9)
    #so to some how convert it with out making abnormal amount of if statments the program divide the 255 by the number of ascii signs 
    #then it rounds down the number and then it makes another  2D matrix containing  rounded down convertet to ascii signs 

    step = 255/len(grey_scale)
    final_matrix=[]
    for k in final_list:
        x_matrix=[]
        for s in k:
            k=math.floor((s/step))
            if k == len(grey_scale):
                k=len(grey_scale)-1
            #print(k)
            x_matrix.append(grey_scale[k])
        final_matrix.append(x_matrix)
    #print(final_matrix)
    return final_matrix

def write_file(matrix):
    #here it just writes the ascii line after line 
    my_file = open("matrix.txt","w+")
    x=0
    y=0
    while y< len(matrix):
        while x< len(matrix[y]):
            my_file.write(matrix[y][x])
            x=x+1
        x=0
        my_file.write("\n")
        y=y+1
        
    my_file.close()

matrix=image_ascii_convert(photo,reverse_colors)
write_file(matrix)