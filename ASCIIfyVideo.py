# Importing all necessary libraries
import cv2
import os
import numpy as np
import glob
from PIL import Image, ImageDraw, ImageOps, ImageFont 

Character = {
    "standard": "@%#*+=-:. ",
    "complex": "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
}


def get_data(mode):
    font = ImageFont.truetype("fonts/DejaVuSansMono-Bold.ttf", size=20)
    scale = 2
    char_list = Character[mode]
    return char_list, font, scale


# Making Background Black or White
bg="white"
if (bg=="white"):
    bg_code=(255,255,255)
elif (bg=="black"):
    bg_code=(0,0,0)
    

# Getting the character List, Font and Scaling characters for square Pixels
char_list,font,scale=get_data("complex")
num_chars=len(char_list)
num_cols=300

#Enter the path to your desired video here 
cap = cv2.VideoCapture("./data/Wanna see my kitties_ animation by telepurte.mp4")
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH ))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT ))
fps =  int(cap.get(cv2.CAP_PROP_FPS))
size = (width,height)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output3.avi', fourcc, fps, size)

flag=0

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        # Converting Color Image to Grayscale
        #image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

        # Extracting height and width from Image

        # Defining height and width of each cell==pixel
        cell_w=width/num_cols
        cell_h=scale*cell_w
        num_rows=int(height/cell_h)

        # Calculating Height and Width of the output Image
        char_width,char_height=font.getsize("A")
        out_width=char_width*num_cols
        out_height=scale*char_height*num_rows

        # Making a new Image using PIL
        out_image=Image.new("RGB",(out_width,out_height),bg_code)
        draw=ImageDraw.Draw(out_image)

        # Mapping the characters for GRAYSCALE

        # for i in range(num_rows):
        #     min_h = min(int((i + 1) * cell_h), height)
        #     row_pix = int(i * cell_h)
        #     # lst = [i for i in range(5)] => We can make strings/lists/tuples in this way => lst = [0, 1, 2, 3, 4]
        #     # lst[first:last] gives us a sublist from the first index to the last index excluding the last index => lst[1:4]==[1, 2, 3]
        #     line = "".join([char_list[
        #         min(int(
        #             np.mean(image[row_pix:min_h, int(j*cell_w)
        #                     :min(int((j + 1) * cell_w), width)]) / 255 * num_chars
        #         ), num_chars - 1)]
        #         for j in range(num_cols)]) + "\n"

        #     # Draw string at a given position (x,y)
        #     draw.text((0, i * char_height), line, fill=255-bg_code, font=font)

        # Mapping the characters for RGB

        for i in range(num_rows):
            for j in range(num_cols):
                partial_image=frame[int(i*cell_h):min(int((i+1)*cell_h),height),int(j*cell_w):min(int((j+1)*cell_w),width),:]
                partial_average_color=np.sum(np.sum(partial_image,axis=0),axis=0)/(cell_h*cell_w)
                partial_average_color=tuple(partial_average_color.astype(np.int32).tolist())
                c=char_list[min(int(np.mean(partial_image)*num_chars/255),num_chars-1)]
                draw.text((j*char_width,i*char_height),c,fill=partial_average_color,font=font)

        # Inverting Image and removing excess borders
        if(bg=="white"):
            cropped_image=ImageOps.invert(out_image).getbbox()
        elif(bg=="black"):
            cropped_image=out_image.getbbox()

        # Saving the new Image
        out_image = out_image.crop(cropped_image)
        out_image_numpyarr=np.array(out_image)
        out_image_numpyarr_resized=cv2.resize(out_image_numpyarr,size)
    
        out.write(out_image_numpyarr_resized)

        print("Added frame "+str(flag+1)+" to the video")
        flag=flag+1

    else:
        print()
        print("Your video is ASCIIfyed!")
        break
cap.release()

out.release()

cv2.destroyAllWindows()