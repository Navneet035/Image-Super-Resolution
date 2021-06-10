import os
from flask import Flask, request, redirect, url_for, send_from_directory, render_template
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from PIL import Image
import cv2
import glob
import random
import tensorflow as tf
import tensorflow_hub as hub
import matplotlib.pyplot as plt
from tensorflow.python.keras.layers import Add, BatchNormalization, Conv2D, Dense, Flatten, Input, LeakyReLU, PReLU, Lambda
from tensorflow.python.keras.models import Model
from tensorflow.python.keras.applications.vgg19 import VGG19

from mod import *


UPLOAD_FOLDER = 'static/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app=Flask(__name__,template_folder='templates')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filename = 'orgimg.jpg'
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))
    return render_template('home.html')


@app.route('/<filename>')
def uploaded_file(filename):
    res('static/'+filename)
    return render_template('final.html', filename=filename)


def res(path):
    im1=Image.open(path)
    if(im1.format=='PNG'):
        image=im1.convert('RGB')
        image.save(r'C:/Users/Navneet/Desktop/super_res/static/test_images/ne.png')
        lr = load_image('C:/Users/Navneet/Desktop/super_res/static/test_images/ne.png')
        sr = resolve_single(model, lr)
        np_im = numpy.array(sr)
        new_im = Image.fromarray(np_im)
        new_im.save("static/newimg.png")
        print ('png') 
    elif(im1.format=='JPEG'):
        image=im1.convert('RGB')
        im1.save(r'C:/Users/Navneet/Desktop/super_res/static/test_images/ne.png')
        lr = load_image('C:/Users/Navneet/Desktop/super_res/static/test_images/ne.png')
        sr = resolve_single(model, lr)
        np_im = numpy.array(sr)
        new_im = Image.fromarray(np_im)
        new_im.save("static/newimg.png")
        print("jpeg")
    else:
        print('bie')
    return send_file('newimg.png')


@app.route('/send_file/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.jinja_env.auto_reload = True
    app.run()





