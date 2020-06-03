import numpy as np
import cv2
import glob,os
import os, subprocess

pdf_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(pdf_dir)


#Parameters of the affine transform:
angle = 15; #Angle in degrees.
shear = 0.3;
translation = 5;

type_border = cv2.BORDER_CONSTANT;
color_border = (255,255,255);

for jpg_file in glob.glob(os.path.join(pdf_dir, "*.jpg")):

    number = 1

    original_image = cv2.imread(jpg_file);
    rows,cols,ch = original_image.shape;
    
    #First: Necessary space for the rotation
    M = cv2.getRotationMatrix2D((cols/2,rows/2), angle, 1);
    cos_part = np.abs(M[0, 0]); sin_part = np.abs(M[0, 1]);
    new_cols = int((rows * sin_part) + (cols * cos_part)); 
    new_rows = int((rows * cos_part) + (cols * sin_part));
    
    #Second: Necessary space for the shear
    new_cols += (shear*new_cols);
    new_rows += (shear*new_rows);
    
    #Calculate the space to add with border
    up_down = int((new_rows-rows)/2); left_right = int((new_cols-cols)/2);
    
    final_image = cv2.copyMakeBorder(original_image, up_down, up_down,left_right,left_right,type_border, value = color_border);
    rows,cols,ch = final_image.shape;
    
    #Application of the affine transform.
    M_rot = cv2.getRotationMatrix2D((cols/2,rows/2),angle,1);
    translat_center_x = -(shear*cols)/2;
    translat_center_y = -(shear*rows)/2;
    
    M = M_rot + np.float64([[0,shear,translation + translat_center_x], [shear,0,translation + translat_center_y]]);
    final_image  = cv2.warpAffine(final_image , M, (cols,rows),borderMode = type_border, borderValue = color_border);
    
    cv2.imwrite(jpg_file+'shear.jpg', final_image)
    