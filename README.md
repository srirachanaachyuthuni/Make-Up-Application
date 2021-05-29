# Make Up Application
Program which detects facial landmarks using Dlib Python package and applies blush, lipstick and eye liner. Used PIL library tools such as gaussian blur, smoothening and interpolation have been used to achieve this

## Application of Makeup
For the application of eyeliner and lipstick, the Visage package of Python has been
used. This package includes the Dlib library to detect the facial landmarks and then,
smoothens the application of color. This package was not directly compatible with
Python3. I have modified the files - apply_makeup.py and detect_features.py to make
this work.

For the application of blush, in the same apply_makeup.py and detect_features.py file, I
have made use of the dlib library to calculate the landmark on the cheek Then, I have
used PIL library’s Image, ImageFilter, ImageEnhance and ImageDraw to draw, sharpen,
smoothen and blur the blush.

After calling the download_image() method, on each of the images downloaded, the
apply_eye_liner(), apply_lipstick() and apply_blush() functions are called respectively
from the same script.

## Setup
1. Create a clients_secrets.json file for providing authentication. 
2. Run the addMakeup.py file which should download the necessary libraries.
3. Replace the apply_makeup.py and detect_features.py files with the files provided to
make it compatible with Python3.
4. The output will be generated in file name - output.png
