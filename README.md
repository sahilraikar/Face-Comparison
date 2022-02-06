# Face-Comparison
Dependencies: cmake, dlib, opencv-python(cv2), face-recognition, numpy

Install visual studio with desktop development with c++ because it is necessary to install dlib library it wont install without the c++ of visual studio it takes two images and compares them and gives a boolean value and it gives values if values is less than 0.6 then both images are matching

Technology We are using Histogram of Oriented Gradients(HOG) method. To find faces in an image, we’ll start by making our image black and white because we don’t need color data to find faces: Then we’ll look at every single pixel in our image one at a time. For every single pixel, we want to look at the pixels that directly surrounding it. Our goal is to figure out how dark the current pixel is compared to the pixels directly surrounding it. Then we want to draw an arrow showing in which direction the image is getting darker The neural network learns to reliably generate 128 measurements for each person. Any ten different pictures of the same person should give roughly the same measurements. Machine learning people call the 128 measurements of each face an embedding. You can do that by using any basic machine learning classification algorithm. No fancy deep learning tricks are needed. We’ll use a simple linear SVM classifier, but lots of classification algorithms could work. All we need to do is train a classifier that can take in the measurements from a new test image and tells which known person is the closest match. Running this classifier takes milliseconds. The result of the classifier is the name of the person

###Instructions-
1. install pycharm
2. install opencv - pip install opencv-python
3. install face_recognition - Download and install CMAKE (https://cmake.org/download/)
                              Go to System -> Advanced System Settings -> Environment Variables -> System Variables -> New... Variable name: CMAKE Variable value: C:\Program Files\CMake\bin (Or where you installed the CMake bin directory)
                              Run CMD
                              Install visual studio with desktop development with c++
                              pip install dlib (the processor will go full throttle on this)
                              pip install face_recognition
