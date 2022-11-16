from flask import Flask

#To render templates 
from flask import render_template
import os
from flask import request
import tensorflow as tf
from tensorflow import keras
import cv2
from PIL import Image, ImageDraw
import pandas as pd
import numpy as np
import os
from pylsd.lsd import lsd
import image_slicer
import h5py

#instantiating Flask application into variable **app** 
app = Flask(__name__)


UPLOAD_FOLDER = "static/"

@app.route("/model")
def model():
    return render_template("model.html")

#Root page of the website
@app.route('/', methods=['GET', 'POST'])

def upload_predict():
    if request.method == 'POST':
        image_file = request.files['image']
        if image_file:
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
                #RESIZE THE IMAGE
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

            image_location = os.path.join(UPLOAD_FOLDER,image_file.filename)
            image_file.save(image_location)
            fullName = image_location
            (folder, imgName) = os.path.split(fullName)
            print(fullName)
            img = cv2.imread(fullName)
            parts = image_slicer.slice(fullName,col=1,row=2, save = False)
            print(parts)
            bimg= cv2.cvtColor(np.array(parts[1].image), cv2.COLOR_RGB2BGR)
            gray = cv2.cvtColor(bimg, cv2.COLOR_BGR2GRAY)
            ret, thresh = cv2.threshold(gray, 100, 200, cv2.THRESH_BINARY)
            corners = cv2.goodFeaturesToTrack(thresh, 100, 0.01, 55)
            corners = np.int0(corners)
            columns = len(corners)
            


            #SLICE IMAGES
            waves = image_slicer.slice(fullName,col=columns,row=1, save = False)


            segt = []
            for wv in waves:
                seg = cv2.cvtColor(np.array(wv.image), cv2.COLOR_RGB2BGR)
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
                new_model = new_model = tf.keras.models.load_model('C:/Users/Shubham/ecg_model.h5') 
                ypred = new_model.predict_classes([inpt_data])
                ans = 0
                print(ypred)
                for y in ypred:
                    if( y == 1 or y == 2 or y == 3 or y == 4):
                        ans = y
                        break

            return render_template('model.html',prediction = ans)

    return render_template('index.html')


# Run Flask application 
if __name__ == '__main__':
    app.run(port=9091, debug= True)
