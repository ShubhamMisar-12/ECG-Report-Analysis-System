from flask import Flask, render_template, request
import os
import tensorflow as tf
from tensorflow import keras
import cv2
from PIL import Image, ImageDraw
import pandas as pd
import numpy as np
from pylsd.lsd import lsd
import h5py



app = Flask(__name__)


UPLOAD_FOLDER = "static/"


def slice_image(image_path, cols=1, rows=1):
    # Load the image
    image = Image.open(image_path)

    # Get the size of the image
    width, height = image.size

    # Calculate the width and height of each slice
    slice_width = width // cols
    slice_height = height // rows

    # Iterate over the rows and columns to slice the image
    sliced_images = []
    for row in range(rows):
        for col in range(cols):
            # Calculate the coordinates for cropping
            left = col * slice_width
            upper = row * slice_height
            right = (col + 1) * slice_width
            lower = (row + 1) * slice_height

            # Crop the image
            slice_image = image.crop((left, upper, right, lower))

            # Append the sliced image to the list
            sliced_images.append(slice_image)

    return sliced_images


def unsharp_mask(image, kernel_size=(5, 5), sigma=1.0, amount=1.0, threshold=0):
    blurred = cv2.GaussianBlur(image, kernel_size, sigma)
    sharpened = float(amount + 1) * image - float(amount) * blurred
    sharpened = np.maximum(sharpened, np.zeros(sharpened.shape))
    sharpened = np.minimum(sharpened, 255 * np.ones(sharpened.shape))
    sharpened = sharpened.round().astype(np.uint8)
    if threshold > 0:
        low_contrast_mask = np.absolute(image - blurred) < threshold
        np.copyto(sharpened, image, where=low_contrast_mask)
    return sharpened

def example(image):
    '''RESIZE THE IMAGE
    '''
    r = 500.0/image.shape[1]
    dim = (500, int(image.shape[0] * r))
    img_sharp = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    sharpened_image = unsharp_mask(img_sharp)
    return sharpened_image

def Sort_Tuple(tup):
    lst = len(tup)
    for i in range(0, lst):
        for j in range(0, lst - i - 1):
            if tup[j][0] > tup[j + 1][0]:
                temp = tup[j]
                tup[j] = tup[j + 1]
                tup[j + 1] = temp
    return tup


@app.route("/")
def model():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():
    image_file = request.files['image']
    if image_file:

        image_location = os.path.join(UPLOAD_FOLDER,image_file.filename)
        image_file.save(image_location)
        fullName = image_location
               
        parts = slice_image(fullName, cols=1, rows=2)
       
        np_image = np.array(parts[1])
        bimg= cv2.cvtColor(np_image, cv2.COLOR_RGB2BGR)
        gray = cv2.cvtColor(bimg, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(gray, 100, 200, cv2.THRESH_BINARY)
        corners = cv2.goodFeaturesToTrack(thresh, 100, 0.01, 55)
        corners = np.int0(corners)
        #columns = len(corners)
        
        waves = slice_image(fullName, cols=4, rows=1)

        segt = []
        for wv in waves:
            seg = cv2.cvtColor(np.array(wv), cv2.COLOR_RGB2BGR)
            segt.append(seg)

        allpoints = []

        for seg in segt:
            points = []
            corners = None
            sharpen = example(seg)
            gray = cv2.cvtColor(sharpen, cv2.COLOR_BGR2GRAY)
            ret, thresh = cv2.threshold(gray, 100, 200, cv2.THRESH_BINARY)
            corners = cv2.goodFeaturesToTrack(thresh, 186, 0.01, 5)
            corners = np.int0(corners)
            for corner in corners:
                x, y = corner.ravel()
                point = tuple((x,y))
                points.append(point)
            allpoints.append(points)


        points = []
        sorted_points = []
        for points in allpoints:
            points = Sort_Tuple(points) 
            sorted_points.append(points)                    
        
        for tup in sorted_points:
            input = []
            output = []
            for i in range(0,len(tup)):
                input.append(float(tup[i][1])/500)
            while(len(input)<187):
                    input.append(0)    
            inpt_data = pd.DataFrame(data = [input])
            new_model = tf.keras.models.load_model('ecg_model.h5') 
            predictions = new_model.predict([inpt_data])
            ypred = np.argmax(predictions, axis=1)
            ans = 0
            print(ypred)
            for y in ypred:
                if( y == 1 or y == 2 or y == 3 or y == 4):
                    ans = y
                    break

        return render_template('index.html',label = ans)

    return render_template('index.html')


# Run Flask application 
if __name__ == '__main__':
    app.run(port=9091, debug= True)
