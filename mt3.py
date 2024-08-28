import os
from tensorflow.keras.preprocessing import image
from PIL import Image
import numpy as np
import tensorflow as tf
import keras
import sys
import time
import RPi.GPIO as GPIO
import photo_on_sound

buzzer=12
relay=18

GPIO.setmode(GPIO.BCM)

GPIO.setup(buzzer, GPIO.OUT)
GPIO.setwarnings(False)
#GPIO.cleanup()

#on sound
import onsound


# get the list of categories :
categories = os.listdir("/home/student/Desktop/datahelmet/train")
categories.sort()

# # load the saved model :
modelSavedPath = "/home/student/Desktop/HelmetV3.keras"
model = keras.models.load_model(modelSavedPath)

# # predict the image
def classify_image(imageFile):
    x= []

    img = Image.open(imageFile)
    img.load()
    img = img.resize((224, 224), resample=Image.LANCZOS)

    x = image.img_to_array(img)
    x= np.expand_dims(x, axis=0)

    #print(x.shape)
    pred = model.predict(x)
    #print(pred)

    # get the higest prediction value
    categoryValue = np.argmax(pred, axis=1)
    categoryValue = categoryValue[0]

    print(categoryValue)

    result = categories[categoryValue]
    
    return result

#photobuzzer

#take photo func
def take_photo():
    ''''''
    photo_on_sound.posound()
    dir_path="/home/student/"
    terminnal_command = f"libcamera-still -o test.jpg"
    os.system(terminnal_command)
    ''''''
    import camoff_sound
    camoff_sound.cos()

    
fail_count=0
#photobuzzer
#import photo_on_sound


while True:
    import helmet_sound
    import no_helmet_sound
    import waitcam
    
    

					
	
    take_photo()
    img_path = "/home/student/test.jpg"
    resultText = classify_image(img_path)
    print(resultText)
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(relay, GPIO.OUT)
    
    if resultText=="with_helmet":
	    helmet_sound.hs()
	    GPIO.output(relay, True)
	    #time.sleep(10)
	    #GPIO.cleanup()
	    break
    
    else:
	    no_helmet_sound.nhs()
	    GPIO.output(relay, False)
	    fail_count +=1
	
	    if fail_count >=5:
		    waitcam.wait_sound()
		    print("Too many failure, stopping camera for 1minute")
		    time.sleep(60)
		    fail_count = 0
		    GPIO.cleanup()
	    else :
		    print(f"Attempt {fail_count}:No helmet detected")
	    
    
	
