# argument variables
argument_enc = True
argument_gcm = True
argument_lps = True
argument_lsb = False
argument_rautox = True
argument_secret_key = None
argument_secret_message = None
argument_json2csv = False
argument_jpg2png = False
argument_silent = False

# AES settings
BLOCK_SIZE = 32

# save all cipher data dictionaries in array dict
cipher_data_array = []

# save temporary cipher config image information
# this is a template for each dicttionary inside the cipher_data.json file
# please do not remove or edit unless you want to edit the code in chaya.py
image_information = {
    "image_id": 0,
    "raw_image_sha256": "",
    "steg_image_path": "",
    "steg_image_sha256": "",
    "comp_image_path": "",
    "comp_image_sha256": "",
    "gcm_auth_tag": "",
    "gcm_cipher_nonce": "",
    "lps_x_coordinate": 0,
    "lps_y_coordinate": 0,
    "secret_key": "",
    "secret_message": "",
    "message_length": 0
}

# save all image quality analysis data
image_quality_analysis_data_array = []

# save temporary image analysis data
# testing image_raw and image_steg only
image_quality_information_1 = {
    "Basic_Information_Source": [],
    "Basic_Information_Destination": [],
    "Quality_Metrics": []
}
