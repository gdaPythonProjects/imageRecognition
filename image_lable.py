#!/usr/bin/python
# -*- coding: utf-8 -*-

import io
import os

from tkinter import *
from tkinter.filedialog import askopenfilename

from google.cloud import vision
from google.cloud.vision import types
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "api_key.json"
import metadata

class ImageRecognition():
    def __init__(self):
        self.image_path = ""

    def get_image_path(self):
        Tk().withdraw()
        self.image_path = askopenfilename()

    def image_labels(self):
        # Tworzy klienta
        client = vision.ImageAnnotatorClient()

        # Łączy ścieżki
        file_name = os.path.join(
            os.path.dirname(__file__),
            self.image_path)

        # Ładuje zdjecie do pamieci
        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)

        metadata.getTag(image)

        # Wykonuje wykrywanie etykiet obrazu
        response = client.label_detection(image=image)
        self.labels = response.label_annotations

        for label in self.labels:
            self.test = Label(text="{}".format(label.description), font=16).pack()
