import sys
import os
import requests
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO


# AZURE preliminaries
subscription_key = "221841f3-ee3d-48e2-bdb2-b073be26fd9e"
assert subscription_key

vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v2.0/"

analyze_url = vision_base_url + "analyze"
#Assume images are in parent direcory /img
image_path = os.path.realpath('..') + '/img'

print(image_path)

