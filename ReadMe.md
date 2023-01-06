## Research Paper 

https://ieeexplore.ieee.org/document/9645917

## Copyright

https://copyright.gov.in/
Registration Number : L-112342/2022

## Background 

An electrocardiogram  (ECG) is a simple test  that can be used to check electrical activity.  ECG is a fundamental  tool in the everyday  practice of clinical  medicine, with more  than 300 million ECGs  obtained annually  worldwide

The model takes input as raw ECG data and outputs prediction of cardiac arrythmia into classes. The ECG model can predict reports into the five categories.

Class 0  Normal ECG

Class 1  Supraventricular ectopic beats

Class 2  Ventricular ectopic beats

Class 3  Fusion Beats 

Class 4  Unknown Beats

## Application

The application is based on flask framework.

The flask server runs the ECGModel.py file to open the web app

Upload the image of ECG report to get the report analysis

## Required Packeges

flask

tensorflow 

cv2

PIL 

pylsd.lsd 

image_slicer

