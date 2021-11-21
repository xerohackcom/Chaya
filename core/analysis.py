import imquality.brisque as brisque
import numpy as np
import cv2
import sys
import json
import csv
import warnings
from PIL import Image
from copy import deepcopy
from pprint import pprint

from core.config import image_quality_analysis_data_array, image_quality_information_1
from core.colors import *
from core.utils import msg_status

# remove warnings
warnings.filterwarnings('ignore')

# set numpy threashold
np.set_printoptions(threshold=sys.maxsize)

# Function > Image BRISQUE Difference
def Calculate_BRISQUEDIFF(src, dst):
    imgA = cv2.imread(src, 1)
    imgB = cv2.imread(dst, 1)
    imgA_brisque = brisque.score(imgA)
    imgB_brisque = brisque.score(imgB)
    BRISQUEDIFF = (imgA_brisque - imgB_brisque)
    return BRISQUEDIFF


# Function > Image RMSE
def Calculate_RMSE(src, dst):
    imgA = cv2.imread(src)
    imgB = cv2.imread(dst)
    RMSE = np.sqrt(((imgA - imgB) ** 2).mean())
    return RMSE


# Function > Image MSE
def Calculate_MSE(src, dst):
    imgA = cv2.imread(src)
    imgB = cv2.imread(dst)
    err = np.sum((imgA.astype("float") - imgB.astype("float")) ** 2)
    err /= float(imgA.shape[0] * imgB.shape[1])
    MSE = err
    return MSE


# Function > Image PSNR
def Calculate_PSNR(src, dst):
    raw_image = cv2.imread(src)
    encoded_image = cv2.imread(dst)
    PSNR = cv2.PSNR(raw_image, encoded_image)
    return PSNR


# Function > Basic Image Information
def Basic_Image_Information(img):
    image_information = []
    Basic_Information_Dict = {
        "Image":"",
        "Image_Format": "",
        "Image_Mode": "",
        "Image_Width": 0,
        "Image_Height": 0,
        "Image_Size": 0
    }

    ximg = Image.open(img)
    Basic_Information_Dict['Image'] = img
    Basic_Information_Dict['Image_Format'] = ximg.format
    Basic_Information_Dict['Image_Mode'] = ximg.mode
    Basic_Information_Dict['Image_Width'] = ximg.width
    Basic_Information_Dict['Image_Height'] = ximg.height
    Basic_Information_Dict['Image_Size'] = os.path.getsize(img)
    image_information.append(Basic_Information_Dict)
    ximg.close()
    return image_information


# Function > Image Quality Metrics
def Image_Quality_Information(src, dst):
    quality_information = []

    Quality_Metrics_Dict = {
        "PSNR": Calculate_PSNR(src, dst),
        "MSE": Calculate_MSE(src, dst),
        "RMSE": Calculate_RMSE(src, dst),
        "BRISQUEDIFF": Calculate_BRISQUEDIFF(src, dst)
    }

    quality_information.append(Quality_Metrics_Dict)
    return quality_information


# Function > To generate all results
def Generate_Analysis_Results(src, dst):
    global image_quality_information_1

    msg_status('INFO', f"Starting Analysis{c_green}")

    image_quality_information_1['Basic_Information_Source'] = Basic_Image_Information(src)
    image_quality_information_1['Basic_Information_Destination'] = Basic_Image_Information(dst)
    image_quality_information_1['Quality_Metrics'] = Image_Quality_Information(src, dst)
    image_quality_analysis_data_array.append(deepcopy(image_quality_information_1))

    msg_status('INFO', f"Analysis{c_green} Successful")

# -- CSV RELATED -- #

def pad_list(lst, size, padding=None):
    _lst = lst[:]
    for _ in range(len(lst), size):
        _lst.append(padding)
    return _lst


def flatten(json_data):
    lst = []
    for dct in json_data:
        max_size = 0
        flattened = dict()
        for k, v in dct.items():
            entries = list(next(iter(v), dict()).values())
            flattened[k] = entries
            max_size = max(len(entries), max_size)
        lst.append({k: pad_list(v, max_size) for k, v in flattened.items()})
    return lst


def merge(flattened):
    merged = dict()
    for dct in flattened:
        for k, v in dct.items():
            if k not in merged:
                merged[k] = []
            merged[k].extend(v)
    return merged


def format_for_writer(merged):
    formatted = []
    for k, v in merged.items():
        for i, item in enumerate(v):
            if i >= len(formatted):
                formatted.append(dict())
            formatted[i][k] = item
    return formatted


def convert_csv(formatted, savepath):
    keys = formatted[0].keys()
    with open(savepath, 'w', encoding='utf8', newline='')  as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(formatted)


def Generate_CSV(sender):

    if sender == "analysis_results":
        # open files
        ar_file_enc = open('appdata/analysis_results_enc.json','r')
        ar_file_dec = open('appdata/analysis_results_dec.json','r')

        # read json files
        json_data_enc = json.load(ar_file_enc)
        json_data_dec = json.load(ar_file_dec)

        # flatten nested json data
        flattened_enc = flatten(json_data_enc)
        flattened_dec = flatten(json_data_dec)

        # merge the flattened json data
        merged_enc = merge(flattened_enc)
        merged_dec = merge(flattened_dec)

        # format the merged data
        formatted_enc = format_for_writer(merged_enc)
        formatted_dec = format_for_writer(merged_dec)

        # convert the json data to csv
        convert_csv(formatted_enc, 'appdata/analysis_results_enc.csv')
        convert_csv(formatted_dec, 'appdata/analysis_results_dec.csv')

        # close files
        ar_file_enc.close()
        ar_file_dec.close()
    elif sender == "cipher_data":
        json_file = open('appdata/cipher_data.json','r')
        json_data = json.load(json_file)

        keys = json_data[0].keys()
        
        with open('appdata/cipher_data.csv', 'w', encoding='utf8', newline='')  as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(json_data)
        json_file.close()
