import cv2
import numpy as np
import urllib
import glob
import os


def process(text,url):
    print (text,url)

    logo = cv2.imread(text)
    


# def url_to_image(url):
# 	# download the image, convert it to a NumPy array, and then read
# 	# it into OpenCV format
# 	resp = urllib.urlopen(url)
# 	image = np.asarray(bytearray(resp.read()), dtype="uint8")
# 	image = cv2.imdecode(image, cv2.IMREAD_COLOR)
# 	# return the image
# 	return image


    images_path = glob.glob(url)

    print("Adding watermark")
    for img_path in images_path:
        img = cv2.imread(img_path)
        h_img, w_img, _ = img.shape

        # Get the center of the original. It's the location where we will place the watermark
        center_y = int(h_img / 2)
        center_x = int(w_img / 2)
        top_y = center_y - int(logo / 2)
        left_x = center_x - int(logo / 2)
        bottom_y = top_y + logo
        right_x = left_x + logo

        # Get ROI
        roi = img[top_y: bottom_y, left_x: right_x]

        # Add the Logo to the Roi
        result = cv2.addWeighted(roi, 1, logo, 0.3, 0)

        # Replace the ROI on the image
        img[top_y: bottom_y, left_x: right_x] = result

        # Get filename and save the image
        filename = os.path.basename(img_path)
        cv2.imwrite("images/watermarked_" + filename, img)