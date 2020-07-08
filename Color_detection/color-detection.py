
#------------------------ Input Image From User---------------------------#
# For command line options 
import argparse
import cv2
import numpy as np
import pandas as pd

# Object for adding an argument for image from User
ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required=True, help="Image Path")
args = vars(ap.parse_args())
img_path = args['image']
img = cv2.imread(img_path)
#------------------------ Input Image From User Ends Here------------------#

clicked = False
r = g = b = xpos = ypos = 0

#------------------------ Reading CSV file with Pandas --------------------#
index = ["colors",'color_name','hex','R','G','B']
csv = pd.read_csv('colors.csv',names=index,header=None)
#------------------------ Reading CSV file with Pandas Ends ---------------#

#---------------------- Calculate distance to get color name --------------#

def getColorName(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R-int(csv.loc[i,"R"])) + abs(G-int(csv.loc[i,"G"])) + abs(B-int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname
#------------------- Calculate distance to get color name Ends-------------#

#---------------------------------draw_fun Starts -------------------------#

def draw_fun(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos,clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)

#--------------------------------- draw_fun Ends --------------------------#

#------------------------------- Mouse Click Evets ------------------------#
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_fun)
# we named our window as ‘image’ and set a callback function 
# which will call the draw_fun() whenever a mouse event occurs.
#------------------------------- Mouse Click Evets Ends -------------------#



#---------------------- Display the Image on screen -----------------------#
# Whenever a double click event occurs, it will update the color name and RGB 
# values on the window.
# Using the cv2.imshow() function, we draw the image on the window. When the 
# user double clicks the window, we draw a rectangle and get the color name to 
# draw text on the window using cv2.rectangle and cv2.putText() functions.

while(1):
    cv2.imshow("image",img)
    if (clicked):
        #cv2.rectangle(image, startpoint, endpoint, color, thickness) -1 thickness fills rectangle entirely
        cv2.rectangle(img,(20,20), (750,60), (b,g,r), -1)
        #Creating text string to display ( Color name and RGB values )
        text = getColorName(r,g,b) + ' R='+ str(r) + ' G='+ str(g) + ' B='+ str(b)
        #cv2.putText(img,text,start,font(0-7), fontScale, color, thickness, lineType, (optional bottomLeft bool) )
        cv2.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)
  #For very light colours we will display text in black colour
        if(r+g+b>=600):
            cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
        clicked=False
    #Break the loop when user hits 'esc' key 
    if cv2.waitKey(20) & 0xFF ==27:
        break

cv2.destroyAllWindows()
#-------------------- Display the Image on screen Ends --------------------#


#By Mohammad Farukh 