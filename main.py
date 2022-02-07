import cv2
import numpy as np
import face_recognition

imgtrain = face_recognition.load_image_file('imgs/2018.jpeg')
imgtrain = cv2.cvtColor(imgtrain, cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('imgs/2022.jpeg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

# trained img
facloc = face_recognition.face_locations(imgtrain)[0]
entrain = face_recognition.face_encodings(imgtrain)[0]
# print(facloc)
cv2.rectangle(imgtrain, (facloc[0], facloc[3]), (facloc[1], facloc[2]), (255, 0, 255), 2)
# testing
facloc2 = face_recognition.face_locations(imgTest)[0]
enTest = face_recognition.face_encodings(imgTest)[0]
# print(facloc2)
cv2.rectangle(imgTest, (facloc2[0], facloc2[3]), (facloc2[1], facloc2[2]), (255, 0, 255), 2)

# comparing
results = face_recognition.compare_faces([entrain], enTest)
facDist = face_recognition.face_distance([entrain], enTest)
print(results)
print(facDist)

# display image
cv2.imshow('Trained', imgtrain)
cv2.imshow('Test', imgTest)
cv2.waitKey(0)