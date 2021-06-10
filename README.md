# Image-Super-Resolution
The goal of this repository is to enable real time super resolution for upsampling low resolution pictures. This design follows the SR-GAN architecture.

![snip](https://user-images.githubusercontent.com/52918128/121484795-31827f00-c9ed-11eb-8724-43a7dd8c5408.PNG)

# Getting Started with the Installation
Python3 and Tensorflow 2.x are required and should be installed on the host machine.

1. Clone the repository using provided command:
```bash
git clone https://github.com/Navneet035/Image-Super-Resolution
```

2. Install the required additional packages. This was tested on Python 3.6. To install the required packages, use the provided requirements.txt file like so:
```bash
pip install -r requirements.txt
```

# Usage

Run the flask app using provided command:
```bash
flask run
```
Upload the image using choose file and press Upload to get super resolution image. The sample test images are given in the folder static/test_images.

![s1](https://user-images.githubusercontent.com/52918128/121487579-d8681a80-c9ef-11eb-888f-e0678493d522.PNG)

![s2](https://user-images.githubusercontent.com/52918128/121487604-de5dfb80-c9ef-11eb-9dfd-a8159a9039eb.PNG)


