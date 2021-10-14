# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 09:38:22 2021

@author: s2123958
"""

# Images_01_Starting_Code
# Engineer Your World

import cv2
import numpy
import os.path

def newTrackbarPos(trackbar_name, trackbar_window, min_val, max_val):
    current_pos = cv2.getTrackbarPos(trackbar_name, trackbar_window)
    if current_pos < min_val:
        cv2.setTrackbarPos(trackbar_name, trackbar_window, min_val)
        print("thats too low")
    
        return min_val 
    elif current_pos > max_val:
        print("thats too high")
        cv2.setTrackbarPos(trackbar_name, trackbar_window, max_val)
        return max_val
    else:
        return current_pos




print ("Save your original image in the same folder as this program.")
filename_valid = False
while filename_valid == False:
    filename = input("Enter the name of your file, including the "\
                                 "extension, and then press 'enter': ")
    if os.path.isfile(filename) == True:
        filename_valid = True
    else:
        print ("Something was wrong with that filename. Please try again.")

original_image = cv2.imread(filename,1)

#takes image specified"

grayscale_image_simple = cv2.imread(filename, 0)

#takes image and stores greyscale of it"

grayscale_image = cv2.cvtColor(grayscale_image_simple, cv2.COLOR_GRAY2BGR)

#Takes greyscale and makes a copy htat repeats each pixels grayscale value 3 times"

cv2.namedWindow('Original Image')
cv2.namedWindow('Grayscale Image')
#cv2.namedWindow('Red Parts of Image')
#cv2.namedWindow('Yellow Parts of Image')
cv2.namedWindow('Customized Image')
cv2.namedWindow('sliders2')
cv2.namedWindow('sliders3')


#creates five display windows"

image_height = original_image.shape[0]
image_width = original_image.shape[1]
image_channels = original_image.shape[2]

#returns three values to the origional image dimentions"

color_one_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
color_two_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
color_three_paper = numpy.zeros((image_height, image_width, image_channels), numpy.uint8)
color_four_paper = numpy.zeros((image_height, image_width, image_channels), numpy.uint8)
color_five_paper = numpy.zeros((image_height, image_width, image_channels), numpy.uint8)
color_six_paper = numpy.zeros((image_height, image_width, image_channels), numpy.uint8)
color_seven_paper = numpy.zeros((image_height, image_width, image_channels), numpy.uint8)

cv2.imshow('Original Image', original_image)
cv2.imshow('Grayscale Image',grayscale_image)

cv2.createTrackbar('cyan', 'sliders2', 1, 255, lambda x:None)
cv2.createTrackbar('green', 'sliders2', 37,255, lambda x:None)
cv2.createTrackbar('blue', 'sliders2', 73, 255, lambda x:None)
cv2.createTrackbar('yellow', 'sliders2', 109, 255, lambda x:None)
cv2.createTrackbar('white', 'sliders2', 145, 255, lambda x:None)
cv2.createTrackbar('brown', 'sliders2', 181, 255, lambda x:None)
cv2.createTrackbar('purple', 'sliders2', 217, 255, lambda x:None)
cv2.createTrackbar('reset', 'sliders3', 0, 1, lambda x:None)
#makes sure all of the images are a commmon size"


color_one_paper[0:image_height,0:image_width, 0:image_channels] = [255,255,0]
color_two_paper[0:image_height,0:image_width, 0:image_channels] = [0,255,0]
color_three_paper[0:image_height,0:image_width, 0:image_channels] = [255,0,0]
color_four_paper[0:image_height,0:image_width, 0:image_channels] = [0,255,255]
color_five_paper[0:image_height,0:image_width, 0:image_channels] = [255,255,255]
color_six_paper[0:image_height,0:image_width, 0:image_channels] = [0,75, 150]
color_seven_paper[0:image_height,0:image_width, 0:image_channels] = [128, 0, 128]
#yellow

#gives color to all of the papers"


keypressed = 1
while (keypressed != 27 and keypressed != ord('s')):
        
    
    
    grayscale_break = newTrackbarPos('cyan', 'sliders2', 0, 36)
    color_two_break = newTrackbarPos('green', 'sliders2', 37, 72)
    color_three_break = newTrackbarPos('blue', 'sliders2', 73, 108)
    color_four_break = newTrackbarPos('yellow','sliders2', 109, 144)
    color_five_break = newTrackbarPos('white', 'sliders2', 145, 180)
    color_six_break = newTrackbarPos('brown', 'sliders2', 181, 216)
    color_seven_break = newTrackbarPos('purple', 'sliders2', 217, 253)
   
    reset_pos = cv2.getTrackbarPos('reset', 'sliders3')
   
    
    if reset_pos > 0:
        cv2.setTrackbarPos('cyan', 'sliders2', 0) 
        cv2.setTrackbarPos('green', 'sliders2', 37) 
        cv2.setTrackbarPos('blue', 'sliders2', 73) 
        cv2.setTrackbarPos('yellow','sliders2', 109) 
        cv2.setTrackbarPos('white', 'sliders2', 145)
        cv2.setTrackbarPos('brown', 'sliders2', 181)
        cv2.setTrackbarPos('purple', 'sliders2', 217)
        cv2.setTrackbarPos('reset', 'sliders3', 0)
    """else:
        cv2.getTrackbarPos('reset', 'sliders3', 0, 255)"""
        
    #"sets point where we divide light from dark"
    
    min_grayscale_for_color_one = [0,0,0]
    max_grayscale_for_color_one = [grayscale_break, grayscale_break,grayscale_break]
    
    min_grayscale_for_color_two = [color_two_break+1,color_two_break+1, color_two_break+1]
    max_grayscale_for_color_two = [color_three_break, color_three_break,color_three_break]
    
    min_grayscale_for_color_three = [color_three_break+1,color_three_break+1,color_three_break+1]
    max_grayscale_for_color_three = [109, 109, 109]
    
    min_grayscale_for_color_four =[color_four_break+1, color_four_break+1, color_four_break+1]
    max_grayscale_for_color_four = [color_five_break, color_five_break, color_five_break]
    
    min_grayscale_for_color_five =[color_five_break+1, color_five_break+1, color_five_break+1]
    max_grayscale_for_color_five = [color_six_break, color_six_break, color_six_break]
    
    min_grayscale_for_color_six = [color_six_break+1, color_six_break+1, color_six_break+1]
    max_grayscale_for_color_six = [color_seven_break, color_seven_break, color_seven_break]
    
    min_grayscale_for_color_seven = [color_seven_break+1, color_seven_break+1, color_seven_break+1]
    max_grayscale_for_color_seven = [253]
    
    #print(min_grayscale_for_red, max_grayscale_for_red)
    #"values in between 1 and 100 wil become red, 101 - 255 will become yellow"
    
    
    
    
    
        
  
    
    min_grayscale_for_color_one = numpy.array(min_grayscale_for_color_one, dtype = "uint8")
    max_grayscale_for_color_one = numpy.array(max_grayscale_for_color_one, dtype = "uint8")
    min_grayscale_for_color_two = numpy.array(min_grayscale_for_color_two, dtype = "uint8")
    max_grayscale_for_color_two = numpy.array(max_grayscale_for_color_two, dtype = "uint8")
    min_grayscale_for_color_three = numpy.array(min_grayscale_for_color_three, dtype = "uint8")
    max_grayscale_for_color_three = numpy.array(max_grayscale_for_color_three, dtype = "uint8")    
    min_grayscale_for_color_four = numpy.array(min_grayscale_for_color_four, dtype = "uint8")
    max_grayscale_for_color_four = numpy.array(max_grayscale_for_color_four, dtype = "uint8")
    min_grayscale_for_color_five = numpy.array(min_grayscale_for_color_five, dtype = "uint8")
    max_grayscale_for_color_five = numpy.array(max_grayscale_for_color_five, dtype = "uint8")
    min_grayscale_for_color_six = numpy.array(min_grayscale_for_color_six, dtype = "uint8")
    max_grayscale_for_color_six = numpy.array(max_grayscale_for_color_six, dtype = "uint8")
    min_grayscale_for_color_seven = numpy.array(min_grayscale_for_color_seven, dtype = "uint8")
    max_grayscale_for_color_seven = numpy.array(max_grayscale_for_color_seven, dtype = "uint8")
    
    #force the arrays that we just created to have the right data type or format"
    
    block_all_but_the_color_one_parts = cv2.inRange(grayscale_image, min_grayscale_for_color_one, max_grayscale_for_color_one)
    block_all_but_the_color_two_parts = cv2.inRange(grayscale_image, min_grayscale_for_color_two, max_grayscale_for_color_two)
    block_all_but_the_color_three_parts = cv2.inRange(grayscale_image, min_grayscale_for_color_three, max_grayscale_for_color_three)
    block_all_but_the_color_four_parts = cv2.inRange(grayscale_image, min_grayscale_for_color_four, max_grayscale_for_color_four)
    block_all_but_the_color_five_parts = cv2.inRange(grayscale_image, min_grayscale_for_color_five, max_grayscale_for_color_five)
    block_all_but_the_color_six_parts = cv2.inRange(grayscale_image, min_grayscale_for_color_six, max_grayscale_for_color_six)
    block_all_but_the_color_seven_parts = cv2.inRange(grayscale_image, min_grayscale_for_color_seven, max_grayscale_for_color_seven)

    #tells the computer to cut out pixels that arent in a range of values. only includes values in said range"
    
    color_one_parts_of_image = cv2.bitwise_or(color_one_paper, color_one_paper, mask = block_all_but_the_color_one_parts)
    color_two_parts_of_image = cv2.bitwise_or(color_two_paper, color_two_paper, mask = block_all_but_the_color_two_parts)
    color_three_parts_of_image = cv2.bitwise_or(color_three_paper, color_three_paper, mask = block_all_but_the_color_three_parts)
    color_four_parts_of_image = cv2.bitwise_or(color_four_paper, color_four_paper, mask = block_all_but_the_color_four_parts)
    color_five_parts_of_image = cv2.bitwise_or(color_five_paper, color_five_paper, mask = block_all_but_the_color_five_parts)
    color_six_parts_of_image = cv2.bitwise_or(color_six_paper, color_six_paper, mask = block_all_but_the_color_six_parts)
    color_seven_parts_of_image = cv2.bitwise_or(color_seven_paper, color_seven_paper, mask = block_all_but_the_color_seven_parts)
    #cuts out from the red paper all of the parts that should be colored"
    
    
    customized_image = cv2.bitwise_or(color_one_parts_of_image, color_two_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, color_three_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, color_four_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, color_five_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, color_six_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, color_seven_parts_of_image)
    #combines red and yellow parts to create a two color image"
    
   
 
    #cv2.imshow('Yellow Parts of Image',yellow_parts_of_image)
    cv2.imshow('Customized Image',customized_image)
    #cv2.namedWindow('sliders')
    
    
    keypressed = cv2.waitKey(1)
if keypressed == 27:
    cv2.destroyAllWindows()
elif keypressed == ord('s'): 
    cv2.imwrite('photo_GS_1.jpg',grayscale_image)
    cv2.imwrite('photo_RY_1.jpg',customized_image)
    cv2.destroyAllWindows()
