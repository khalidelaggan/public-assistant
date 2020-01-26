#!/usr/bin/env python
import json
import sys
import pprint
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3

'''
{
  "url": "https://gateway-a.watsonplatform.net/visual-recognition/api",
  "note": "It may take up to 5 minutes for this key to become active",
  "api_key": "378cfd6a0b4cb24274951cec6758699c05fcb180"
}
'''

visual_recognition = VisualRecognitionV3('2016-05-20', api_key='378cfd6a0b4cb24274951cec6758699c05fcb180')

def classifyImage(image_path):
    with open(join(image_path), 'rb') as image_file:
        visR = visual_recognition.classify(images_file=image_file)
        print(visR['images'])

classifyImage(sys.argv[1])
