# > ----------------------------- < #
# >                               < #
# >            [ Chaya ]          < #
# >                               < #
# >  Advance Image Steganography  < #
# >                               < #
# > ----------------------------- < #
#
# [= GitHub: https://github.com/xerohackcom/Chaya-Advance-Steganography
# [= Website: https://xerohack.com/chaya/
# [= Developer: https://www.linkedin.com/in/bhavesh-kaul-cs/
#


import sys
import os
import platform
import urllib.request
import time
import math
import json
import threading
import shutil

from core.config import *
from core.colors import *
from core.utils import *
from core.cryptography import *
from core.steganography import *
from core.compression import *
from core.analysis import Generate_Analysis_Results, Generate_CSV

import argparse
import pandas
import tqdm
from datetime import datetime
from pyfiglet import figlet_format
from prettytable import PrettyTable
from pprint import pprint
from copy import deepcopy

global argument_enc
global argument_gcm
global argument_lps
global argument_lsb
global argument_rautox
global argument_secret_message
global argument_secret_key
global argument_json2csv
global argument_jpg2png
global argument_silent
global cipher_data_array
global image_information

# define runlevel
runlevel = "dev"

# temp list for in-memory random id comparison
temporary_random_id_array = []

# temp array for in-memory decrypted cipher data
temporary_cipher_data = []

# Function > To get object data value from object name from file
def read_cipher_data_objects_value_from_file(object_name):
    global argument_silent

    object_values = []
    try:
        f = open("appdata/cipher_data.json", "r")
        images_cipher_data = json.loads(f.read())
        for image_data in images_cipher_data:
            object_values.append(image_data[object_name])
        f.close()
        if len(object_values) > 0:
            return object_values
        else:
            return None
    except Exception as e:
        return None


# Function > To read all cipher data
def read_all_cipher_data():
    global cipher_data_array
    global argument_silent

    cipher_data_array.clear()
    try:
        f = open("appdata/cipher_data.json", "r")
        cipher_data_array = json.loads(f.read())
        f.close()
    except Exception as e:
        msg_status('ERROR', 'Cannot read cipher data file!')


# Function > To save image cipher data
def save_all_cipher_data():
    global argument_enc
    global argument_silent

    savepath = "appdata/cipher_data.json"
    with open(savepath, 'w') as f:
        json.dump(cipher_data_array, f, indent=4)
        msg_status('INFO', f'Cipher Data Saved: {c_blue}{savepath}{c_green}')
    if argument_enc == True:
        # if json2csv option
        if argument_json2csv == True:
            Generate_CSV("cipher_data")


# Function > To save analysis results
def save_all_analysis_results(type):
    global argument_silent

    if type == "enc":
        savepath = "appdata/analysis_results_enc.json"
        with open(savepath, 'w') as f:
            json.dump(image_quality_analysis_data_array, f, indent=4)
            msg_status('INFO', f'Analysis [Enc] Results Saved: {c_blue}{savepath}{c_green}')
        image_quality_analysis_data_array.clear()
    elif type == "dec":
        savepath = "appdata/analysis_results_dec.json"
        with open(savepath, 'w') as f:
            json.dump(image_quality_analysis_data_array, f, indent=4)
            msg_status('INFO', f'Analysis [Dec] Results Saved: {c_blue}{savepath}{c_green}')
        image_quality_analysis_data_array.clear()


# Function > Run Automatic Experiments > Enc Mode
def AutoExp_Enc(raw_image_path, raw_image):
    global argument_enc
    global argument_gcm
    global argument_lps
    global argument_lsb
    global argument_secret_message
    global argument_secret_key
    global cipher_data_array
    global image_information
    global argument_silent

    # refresh image information data - with None value
    for x in image_information:
        image_information[x] = None

    msg_status("INFO", f"Generating Metadata For: {c_blue}{raw_image_path}{c_green}")

    # generate a random id
    for x in range(100):
        # generate a random id
        random_id = generate_random_id()
        # test for cipher data file not empty
        if not read_cipher_data_objects_value_from_file("image_id") == None:
            # if random id value is not in our json cipher_data
            if random_id not in read_cipher_data_objects_value_from_file("image_id"):
                # if random id is not in temporary array list
                if random_id not in temporary_random_id_array:
                    # append random id to image information array
                    image_information['image_id'] = random_id
                    # append random id to temporary array list
                    temporary_random_id_array.append(random_id)
                    # break from the loop
                    break
        else:
            # if random id is not in temporary array list
            if random_id not in temporary_random_id_array:
                # append random id to image information array
                image_information['image_id'] = random_id
                # append random id to temporary array list
                temporary_random_id_array.append(random_id)
                # break from the loop
                break

    temporary_random_id_array.clear()

    image_information['raw_image_sha256'] = generate_filesignature_sha256(raw_image_path)
    image_information['steg_image_path'] = f"autoexp/image_steg/{raw_image}"
    image_information['comp_image_path'] = f"autoexp/image_steg_comp/{raw_image[:-4]}.flif"
    image_information['secret_key'] = argument_secret_key
    image_information['secret_message'] = argument_secret_message

    # /* ---- PERFORM ENCRYPTION ---- */
    if argument_gcm:
        gcm_result_array = AES_256_GCM_Encrypt(image_information['secret_key'], image_information['secret_message'])
        msg_status('INFO', "AES-256-GCM Encryption Successful")
        # save to image information dict
        image_information['secret_message'] = gcm_result_array[0]
        image_information['gcm_auth_tag'] = gcm_result_array[1]
        image_information['gcm_cipher_nonce'] = gcm_result_array[2]
        gcm_result_array.clear()

    # /* ---- PERFORM ENCODING ---- */
    if argument_lps:
        lps_results_array = LPS_Encode(raw_image_path, image_information['secret_message'], image_information['steg_image_path'], startingPixel=(0,0))
        msg_status('INFO', "LSB-LPS Steganography Successful")
        # save to image information dict
        image_information['lps_x_coordinate'] = lps_results_array[0]
        image_information['lps_y_coordinate'] = lps_results_array[1]
        lps_results_array.clear()
        image_information['steg_image_sha256'] = generate_filesignature_sha256(image_information['steg_image_path'])
    elif argument_lsb:
        LSB_Encode(raw_image_path, image_information['secret_message'], image_information['steg_image_path'])
        image_information['lps_x_coordinate'] = 0
        image_information['lps_y_coordinate'] = 0
        image_information['steg_image_sha256'] = generate_filesignature_sha256(image_information['steg_image_path'])
    
    # /* ---- PERFORM COMPRESSION ---- */
    steg_image_path = f"autoexp/image_steg/{raw_image}"
    comp_image_path = f"autoexp/image_steg_comp/{raw_image[:-4]}.flif"
    image_information['comp_image_path'] = comp_image_path
    flif('e', steg_image_path, comp_image_path)
    image_information['comp_image_sha256'] = generate_filesignature_sha256(image_information['comp_image_path'])
    image_information['message_length'] = utf8len(image_information['secret_message'])
    cipher_data_array.append(deepcopy(image_information))
    Generate_Analysis_Results(raw_image_path, steg_image_path)


# Function > Run Automatic Experiments > Dec Mode
def AutoExp_Dec(raw_image_path):
    global argument_lps
    global argument_lsb
    global image_information
    global argument_silent

    # /* ---- PERFORM DECOMPRESSION ---- */
    flif('d', image_information['steg_image_path'], image_information['comp_image_path'])
    
    # /* ---- PERFORM DECODING ---- */
    if argument_lps:
        encrypted_data = LPS_Decode(image_information['steg_image_path'], int(image_information['lps_x_coordinate']), int(image_information['lps_y_coordinate']))
    elif argument_lsb:
        encrypted_data = LSB_Decode(image_information['steg_image_path'])

    # /* ---- PERFORM DECRYPTION ---- */
    image_information['secret_message'] = AES_256_GCM_Decrypt(image_information['secret_key'], encrypted_data, image_information['gcm_auth_tag'], image_information['gcm_cipher_nonce'])

    # /* ---- PERFORM ANALYSIS ---- */
    Generate_Analysis_Results(raw_image_path, image_information['steg_image_path'])


# Function > Auto Experiment Mode
def RunType_AutoExp():
    global cipher_data_array
    global image_information
    global argument_json2csv
    global argument_jpg2png
    global argument_silent

    msg_status("INFO", f"Starting Automatic Operations")
    multi_thread_list = []

    cipher_data_array.clear()


     # for conversion from jpg to png
    if argument_jpg2png == True:
        # raw image directory
        raw_images_dir = "autoexp/image_raw/"
        msg_status("INFO", f"Getting All Raw Images From Directory")
        raw_images = get_files_in_dir(raw_images_dir)
        msg_status("INFO", "Converting JPG to PNG")
        for raw_image in tqdm.tqdm(raw_images):
            raw_image_path = f"{raw_images_dir}{raw_image}"
            convert_jpg_to_png(raw_image_path)
    
    #clear_screen()

    # raw image directory
    raw_images_dir = "autoexp/image_raw/"
    msg_status("INFO", f"Getting All Raw Images From Directory")
    raw_images = get_files_in_dir(raw_images_dir)

    # if encryption
    if argument_enc:
        # for each image in the folder of raw images
        for raw_image in tqdm.tqdm(raw_images):
            raw_image_path = f"{raw_images_dir}{raw_image}"
            AutoExp_Enc(raw_image_path, raw_image)
        save_all_cipher_data()
        save_all_analysis_results('enc')
        cipher_data_array.clear()
        image_information.clear()
    # if decryption
    else:
        image_information.clear()

        read_all_cipher_data()

        for x in range(len(cipher_data_array)):
            image_information = cipher_data_array[x]
            raw_image_path = f"{raw_images_dir}{raw_images[x]}"
            AutoExp_Dec(raw_image_path)
            # use if we want to erase other metadata after decrypting msg
            #for x in image_information:
            #    if not x == "secret_message":
            #        image_information[x] = None
            temporary_cipher_data.append(deepcopy(image_information))
        cipher_data_array.clear()
        cipher_data_array = temporary_cipher_data
        save_all_cipher_data()
        save_all_analysis_results('dec')
        cipher_data_array.clear()
        image_information.clear()
    
        # if json2csv option
        if argument_json2csv == True:
            Generate_CSV("analysis_results")


# Function > Manual Mode
def RunType_Manual():
    global argument_silent

    msg_status("WARNING", f"Manual Mode Not Available Yet..")
    msg_status("INFO", f"Exiting")
    exit()

    # - manual mode to be focused on later
    #src_image = input("Enter Source Image [*.png] >> ")
    #dst_image = f"{src_image[:-4]}.flif"

    #if argument_enc:
    #    pass
    #else:
    #    pass


# Function > Script Run Type Mode Management 
def run_manager():
    global argument_rautox
    global argument_silent

    if argument_rautox:
        RunType_AutoExp()
    else:
        RunType_Manual()

# Function > Determine runlevel
def check_runlevel():
    global runlevel
    with open('updater/RUNLEVEL.txt') as f:
        runlevel = f.readline()


# Function > Download Updater Script
def download_updater():
    global runlevel

    filename = "update.py"
    filepath = f"updater/{filename}"
    if os.path.isfile(filename):
        msg_status("INFO", f"Removing > updater/update.py")
        os.remove(filename)
    try:
        msg_status("INFO", f"Downloading > updater/update.py")
        urllib.request.urlretrieve(f"https://raw.githubusercontent.com/xerohackcom/Chaya/{runlevel}/updater/update.py", filename)
        if os.path.isfile(filepath):
            os.remove(filepath)
        shutil.move(filename, filepath)
    except Exception as e:
        msg_status('ERROR', f"Unable to download {c_yellow}update.py{c_red}\n{e}{c_white}\nEXITING!\n")
        exit()


# Function > GitHub Script Version
def github_version():
    global runlevel
    response = urllib.request.urlopen(f"https://raw.githubusercontent.com/xerohackcom/Chaya/{runlevel}/VERSION.txt")
    for content in response:
        return int(content)


# Function > Current Script Version
def current_version():
    version_number = 0
    with open('VERSION.txt') as f:
            version_number = f.readline()
    return int(version_number)


# Function > Compare Current Version
def version_check():
    current_v, github_v = current_version(), github_version()
    if current_v < github_v:
        msg_status("INFO", f"Update Available!")
        msg_status("INFO", f"Updating Your Script.. Please DO NOT Exit!")
        try:
            msg_status("INFO", f"Running > updater/update.py")
            os.system("python3 updater/update.py")
        except Exception as e:
            msg_status('ERROR', f"Unable to start {c_yellow}update/updater.py{c_red}\n{e}{c_white}\nEXITING!\n")
    elif current_v == github_v:
        msg_status("INFO", f"You have the latest updates!\n")
    elif current_v > github_v:
        msg_status("INFO", f"You are runnnig ahead of the github version!\n")


# Function > Chaya Updater
def chaya_update():
    check_runlevel()
    download_updater()
    version_check()


# Function > Chaya banner
def chaya_banner():
    version_number = 0
    print(f''' {c_red}
              'i`            
       ^].>Q.  `$>       
       LB;>K'  .#;       
   :>  ;9|;P,  ;m'       
   ;K` 'xZrm?-~ei`       
   `*='`^qRBQBQQ;` `2^   
    `^yyD@@@@@@Q*` ;B7`  
      :Q@@@@@@QQo;:RQ^   
      `R@@@@QQQ@RgQQZ`   
       z#@@@@@QQQQ#J,   {c_clean}  \n''')
    print(f" {c_green}{c_bold}Chaya Advance Steganography{c_clean}")
    
    try:
        with open('VERSION.txt') as f:
            version_number = list(f.readline())
            print(f" {c_bold}{c_yellow}     [ {version_number[0]}.{version_number[1]} ] {c_red} [ 2022 ]{c_clean}")
    except Exception as e:
        print(f" {c_bold}{c_yellow}     [ v1 ] {c_red} [ 2021 ]{c_clean}")
    print(f" {c_blue}{c_bold}     [ Bhavesh Kaul ]{c_clean}\n")

    chaya_update()


# Function > Chaya Help
def chaya_help():
    htable_parser_main = PrettyTable()
    htable_group_operations = PrettyTable()
    htable_group_steganography = PrettyTable()
    htable_group_runmode = PrettyTable()
    htable_parser_main.field_names = htable_group_operations.field_names = htable_group_steganography.field_names = htable_group_runmode.field_names = ["Arg Less", "Arg Full", "Description"]

    # arguments for operations
    htable_group_operations.add_row([f"{c_green}-enc", "--encrypt", f"{c_cyan}Perform Encryption{c_white}"])
    htable_group_operations.add_row([f"{c_green}-dec", "--decrypt", f"{c_cyan}Perform Decryption{c_white}"])

    # arguments for steganography
    htable_group_steganography.add_row([f"{c_green}-lps", "--lps", f"{c_cyan}LSB-LPS Steganography {c_blue}(Default){c_white}"])
    htable_group_steganography.add_row([f"{c_green}-lsb", "--lsb", f"{c_cyan}LSB-Only Steganography {c_red}(Not Preferred){c_white}"])

    # arguments for main parser
    htable_parser_main.add_row([f"{c_green}-m", "--msg", f"{c_cyan}Your Secret Message{c_white}"])
    htable_parser_main.add_row([f"{c_green}-k", "--key", f"{c_cyan}Your Secret Key{c_clean}"])
    htable_parser_main.add_row([f"{c_green}-j2c", "--json2csv", f"{c_cyan}Convert JSON Data To CSV{c_white}"])
    htable_parser_main.add_row([f"{c_green}-jpg2png", "--jpg2png", f"{c_cyan}Raw JPG to PNG Conversion {c_blue}(untested){c_white}"])
    htable_parser_main.add_row([f"{c_green}-silent", "--silent", f"{c_cyan}Minimum Verbosity{c_white}"])
    htable_parser_main.add_row([f"{c_green}-cleardata", "--cleardata", f"{c_cyan}Clear all appdata{c_white}"])
    htable_parser_main.add_row([f"{c_green}-h", "--help", f"{c_cyan}Help Menu{c_white}"])

    # arguments for runmode
    htable_group_runmode.add_row([f"{c_green}-rautox", "--runautoexp", f"{c_cyan}Run Automatic Experiments {c_blue}(default){c_white}"])
    htable_group_runmode.add_row([f"{c_green}-rmanx", "--runmanualexp", f"{c_cyan}Help Menu {c_red}(in-development){c_white}"])

    # print help menu
    print(f" Operations Options > Mutually Exclusive")
    print(f"{c_white}{htable_group_operations}{c_clean}")
    print("\n Steganography Options > Mutually Exclusive")
    print(f"{c_white}{htable_group_steganography}{c_clean}")
    print("\n Standard Options")
    print(f"{c_white}{htable_parser_main}{c_clean}")
    print("\n Run Options > Mutually Exclusive")
    print(f"{c_white}{htable_group_runmode}{c_clean}")


# Function > Start Chaya Script
def chaya_start():
    global argument_enc
    global argument_gcm
    global argument_lps
    global argument_lsb
    global argument_rautox
    global argument_secret_key
    global argument_secret_message
    global argument_json2csv
    global argument_jpg2png
    global argument_silent

    clear_screen()
    chaya_banner()

    # start argument parser
    parser = argparse.ArgumentParser(description="Chaya Argument Parser", add_help=False)

    group_operations = parser.add_mutually_exclusive_group()
    group_operations.add_argument('-enc','--encrypt', action="store_true")
    group_operations.add_argument('-dec','--decrypt', action="store_true")
    parser.add_argument('-gcm', '--gcm', action="store_true")
    group_steganogprahy = parser.add_mutually_exclusive_group()
    group_steganogprahy.add_argument('-lps', '--lps', action="store_true")
    group_steganogprahy.add_argument('-lsb', '--lsb', action="store_true")
    parser.add_argument('-m','--msg', type=str)
    parser.add_argument('-k','--key', type=str)
    parser.add_argument('-j2c','--json2csv', action="store_true")
    parser.add_argument('-jpg2png','--jpg2png', action="store_true")
    parser.add_argument('-silent', '--silent', action="store_true")
    parser.add_argument('-cleardata', '--cleardata', action="store_true")
    parser.add_argument("-h", "--help", action="store_true")
    group_runmode = parser.add_mutually_exclusive_group()
    group_runmode.add_argument('-rautox','--runautoexp', action="store_true")
    group_runmode.add_argument('-rmanx','--runmanualexp', action="store_true")

    args = parser.parse_args()

    # if no args passed
    if not len(sys.argv) > 1:
        exit()

    # special args
    if args.cleardata:
        clear_appdata()
        exit()

    # settings global variables
    if args.encrypt:
        argument_enc = True
    elif args.decrypt:
        argument_enc = False
    else:
        argument_enc = True
    if args.gcm:
        argument_gcm = True
    if args.lps:
        argument_lps = True
        argument_lsb = False
    elif args.lsb:
        argument_lsb = True
        argument_lps = False
    if args.msg:
        argument_secret_message = args.msg
    if args.key:
        argument_secret_key = args.key
        for x in range(0, 32):
            if len(argument_secret_key) < 32:
                argument_secret_key = f"{argument_secret_key}x"
    if args.runautoexp:
        argument_rautox = True
    elif args.runmanualexp:
        argument_rautox = False
    else:
        argument_rautox = True
    if args.json2csv:
        argument_json2csv = True
    if args.jpg2png:
        argument_jpg2png = True
    if args.silent:
        argument_silent = True
    if args.help:
        chaya_help()
        exit()

    if (argument_secret_key == None or argument_secret_key == ""):
        if not argument_silent:
            msg_status('WARNING', 'User has not defined any secret key')
        argument_secret_key = "abcdefghijklmnopqrstuvwxyzabcdef"
        if not argument_silent:
            msg_status('INFO', f'Using default key {c_yellow}>>{c_blue} {argument_secret_key}')
    if (argument_secret_message == None or argument_secret_message == ""):
        if not argument_silent:
            msg_status('WARNING', 'User has not defined any payload')
        argument_secret_message = "proc./<h77p5://4p7-5734l5-3v3ry7hInG.54d/>./ess|.start.|"
        if not argument_silent:
            msg_status('INFO', f'Using default payload {c_yellow}>>{c_blue} {argument_secret_message}')

    # start the run manager
    run_manager()


# Initialize Script
if __name__ == "__main__":
    chaya_start()
