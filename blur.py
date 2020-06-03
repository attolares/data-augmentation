import numpy as np
import cv2
import glob,os
import os, subprocess

pdf_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(pdf_dir)


for jpg_file in glob.glob(os.path.join(pdf_dir, "*.jpg")):

    original_image = cv2.imread(jpg_file);
    # ksize 
    ksize = (10, 10) 
      
    # Using cv2.blur() method  
    image = cv2.blur(original_image, ksize)  
    
    cv2.imwrite(pdf_dir+'/blur/'+os.path.basename(jpg_file), final_image)
    