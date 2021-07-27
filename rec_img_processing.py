import cv2
import numpy as np
sample_img = cv2.imread("imgs/rec_002.bmp")
sobel = np.array([[],[],[]])
"""
with_rect = cv2.rectangle(img=sample_img, pt1=(0,142),pt2=(4200, 165),color=[0,255,0],thickness=2)
cv2.imshow("select_rec", with_rect)
cv2.waitKey(0)
"""
wo_rect = sample_img[122:185, 0:4200]
resized_img = cv2.resize(wo_rect,(400,400))
#cv2.imwrite("imgs/test_img.bmp", resized_img)
cv2.imshow("resized_img", resized_img)
cv2.imshow("cut_image",wo_rect)
cv2.waitKey(0)