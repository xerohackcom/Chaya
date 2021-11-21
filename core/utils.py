import os
import random
import hashlib
from datetime import datetime
from PIL import Image
from prettytable import PrettyTable

from core.colors import *


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def msg_status(type, msg):
    if type == "ERROR":
        print(f"{c_white}[{get_current_time()}]{c_cyan} {c_red}[ERROR]{c_cyan} >{c_yellow} {msg} {c_cyan}")
    elif type == "INFO":
        print(f"{c_white}[{get_current_time()}]{c_cyan} {c_yellow}[INFO]{c_cyan} >{c_green} {msg} {c_cyan}")
    elif type == "WARNING":
        print(f"{c_white}[{get_current_time()}]{c_cyan} {c_yellow}[WARNING]{c_cyan} >{c_white} {msg} {c_cyan}")
    else:
        print(f"{c_white}[{get_current_time()}]{c_cyan} {c_white}[-]{c_cyan} >{c_white} {msg} {c_cyan}")


def get_files_in_dir(dir_path):
    files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
    return files


def generate_random_id():
    random_id = random.randint(1,10001)
    return random_id


def generate_filesignature_sha256(file_path):
    sha256_hash = hashlib.sha256()
    filehash = ""
    try:
        with open(file_path,"rb") as f:
            # Read and update hash string value in blocks of 4K
            for byte_block in iter(lambda: f.read(4096),b""):
                sha256_hash.update(byte_block)
            filehash = sha256_hash.hexdigest()
    except Exception as e:
        raise e
    return filehash


def get_current_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time


def convert_jpg_to_png(image_path):
    ximg = Image.open(image_path)
    new_image_path = f"{image_path[:-5]}.png"
    ximg.save(new_image_path)
    os.remove(image_path)


def get_current_script_path():
    return os.path.realpath(__file__)


def utf8len(s):
    return len(s.encode('utf-8'))


def clear_appdata():
    # get all the files from appdata folder
    data_files = get_files_in_dir("appdata/")
    msg_status('INFO', 'Safe cleaning appdata')
    # for each file in list of files in appdata folder
    for df in data_files:
        # if file is CSV
        if df[-4:] == ".csv":
            # delete the file
            os.remove(f"appdata/{df}")
            msg_status('WARNING', f'{c_red}[Deleted]{c_white} appdata/{df}')
        if df[-5:] == ".json":
            # if file is JSON, empty the file
            with open(f"appdata/{df}", "w") as f:
                f.write("")
            msg_status('WARNING', f'{c_blue}[Cleaned]{c_white} Content of: appdata/{df}')
    # delete all images in autoexp
    image_raw_files = get_files_in_dir("autoexp/image_raw/")
    image_steg_files = get_files_in_dir("autoexp/image_steg/")
    image_steg_comp_files = get_files_in_dir("autoexp/image_steg_comp/")
    msg_status('INFO', 'Deleting raw images')
    for imgfilex in image_raw_files:
        os.remove(f"autoexp/image_raw/{imgfilex}")
        msg_status('WARNING', f'{c_red}[Deleted]{c_white} autoexp/image_raw/{imgfilex}')
    msg_status('INFO', 'Deleting stego images')
    for imgfiley in image_steg_files:
        os.remove(f"autoexp/image_steg/{imgfiley}")
        msg_status('WARNING', f'{c_red}[Deleted]{c_white} autoexp/image_steg/{imgfiley}')
    msg_status('INFO', 'Deleting compressed images')
    for imgfilez in image_steg_comp_files:
        os.remove(f"autoexp/image_steg_comp/{imgfilez}")
        msg_status('WARNING', f'{c_red}[Deleted]{c_white} autoexp/image_raw_comp/{imgfilez}')
    msg_status('INFO', f'You are all set for new a experiment')