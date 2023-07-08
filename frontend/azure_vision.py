#
# Python functions for visual search with Azure Computer Vision 4 Florence
#
# File: azure.py
#
# Azure Service : Azure Computer Vision 4.0 (Florence)
# Usecase: Visual search using image or text to find similar images
# Python version: 3.8.5
#
# Date: 3 May 2023
# Author: Serge Retkowsky | Microsoft | https://github.com/retkowsky
#

import datetime
import json
import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import pandas as pd
import requests
import seaborn as sns

from dotenv import load_dotenv
from io import BytesIO
from PIL import Image
from cleanvision.imagelab import Imagelab

load_dotenv("../.env")

# Reading Azure Computer Vision 4 endpoint and key from the env file
key = os.getenv("azure_cv_key")
endpoint = os.getenv("azure_cv_endpoint")


def describe_image_with_AzureCV4(image_file):
    """
    Get tags & caption from an image using Azure Computer Vision 4 Florence
    """
    options = "&features=tags,caption"
    model = "?api-version=2023-02-01-preview&modelVersion=latest"
    url = endpoint + "/computervision/imageanalysis:analyze" + model + options

    headers_cv = {
        'Content-type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': key
    }

    with open(image_file, 'rb') as f:
        data = f.read()

    r = requests.post(url, data=data, headers=headers_cv)
    results = r.json()

    return {"mainCaption": results['captionResult']['text'],
            "mainCaptionResult": results['captionResult']['confidence'],
            "detectedTags": results['tagsResult']['values']}


def dataset_quality_report(image_path):
    imagelab = Imagelab(data_path=image_path)
    issues = imagelab.find_issues()

    report = imagelab.report()
    summary = imagelab.issue_summary

    return {"issues": issues, "report": report, "summary": summary}
