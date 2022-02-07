# Face-Comparison
Dependencies: cmake, dlib, opencv-python(cv2), face_recognition, numpy

Methods used: HOG, SVM classifier, 

Note: Install visual studio with desktop development with c++ because dlib library wont install without the c++ of visual studio as it takes two images and compares them to return a boolean value and it gives values if values is less than 0.6 then both images are matching

Technology:  We are using Histogram of Oriented Gradients(HOG) method to find faces in an image. We start by making our image black and white because we don’t need color data to find faces, then we’ll look at every single pixel in our image one at a time. For every pixel, we want to look at the pixels that directly surround it. Our goal is to figure out how dark the current pixel is compared to the pixels directly surrounding it. Then we draw an arrow showing in which direction the image is getting darker. The neural network learns to reliably generate 128 measurements for each person. Any ten different pictures of the same person should give roughly the same measurements. In Machine learning the 128 measurements of each face are called embeddings. You can do that by using any basic machine learning classification algorithm. No fancy deep learning tricks are needed. We’ll use a simple linear SVM classifier, but lots of classification algorithms could work. All we need to do is train a classifier that can take in the measurements from a new test image and tells which known person is the closest match. Running this classifier takes milliseconds. The result of the classifier is the name of the person. 0.6 is the typical best performance for compare_faces function.

### Instructions-
1. install pycharm
2. use python3.8
3. install opencv - pip install opencv-python
4. Download and install CMAKE (https://cmake.org/download/) - Go to System -> Advanced System Settings -> Environment Variables -> System Variables -> New... Variable name: CMAKE Variable value: C:\Program Files\CMake\bin (Or where you installed the CMake bin directory) / In pycharm go to settings -> python interpreter -> + -> search cmake and click install
5. Install visual studio with desktop development with c++ (https://visualstudio.microsoft.com/vs/community/)
6. install face_recognition 
   - Open terminal<br />
   - pip install dlib (the processor will go full throttle on this)<br />
   - pip install face_recognition
