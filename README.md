# Image-Super-Resolution
The goal of this repository is to enable real time super resolution for upsampling low resolution videos. Currently, the design follows the SR-GAN architecture.

![snip](https://user-images.githubusercontent.com/52918128/121484795-31827f00-c9ed-11eb-8724-43a7dd8c5408.PNG)

# Getting Started with the Installation
Python3 and Tensorflow 2.x are required and should be installed on the host machine.

1. Clone the repository using provided command:
```bash
git clone https://github.com/Navneet035/Image-Super-Resolution
```

2. Install the required additional packages.This was tested on Python 3.6. To install the required packages, use the provided requirements.txt file like so:
```bash
pip install -r requirements.txt
```

# Usage
In app.py and mod.py file, change the location of folder to the folder you have cloned the repository.

Run the flask app using provided command:
```bash
flask run
```
Upload the image using choose file and press Upload to get super resolution image.The sample test images are given in the folder static/test_images.


