<h1 align="center">
  <br>
  <a href="https://github.com/xerohackcom/chaya"><img src="https://i.ibb.co/X2WmCxm/chaya.png" alt="chaya"></a>
  <br>
  Chaya
  <br>
</h1>

<p align="center">
  <a href="https://github.com/xerohackcom/chaya">
    <img src="https://img.shields.io/badge/release-v1-green">
  </a>
   </a>
  <a href="https://github.com/xerohackcom/Chaya/blob/main/LICENSE">
      <img src="https://img.shields.io/badge/license-AGPL3-_red.svg">
  </a>
  <a href="https://www.python.org/downloads/">
    <img src="https://img.shields.io/badge/language-python3-green">
  </a>
</p>

<h3 align="center">Right To Privacy</h3>

**Chaya** protects your privacy through steganography, cryptography and compression. It effectively encrypts your payloads using *AES-256-GCM* cryptography, embeds them using *LSB-LPS* steganography technique into images and compresses them using *FLIF* to evade detection by performing lossless compression. 

Chaya is for your privacy.

<strong><a href="https://www.un.org/en/about-us/universal-declaration-of-human-rights">United Nations Declaration of Human Rights (UDHR) 1948, Article 12 - </strong></a>“No one shall be subjected to arbitrary interference with his privacy, family, home or correspondence, nor to attacks upon his honor and reputation. Everyone has the right to the protection of the law against such interference or attacks.”
<br><br>
<strong><a href="https://en.wikipedia.org/wiki/International_Covenant_on_Civil_and_Political_Rights">International Covenant on Civil and Political Rights (ICCPR) 1966, Article 1 - </strong></a>"No one shall be subjected to arbitrary or unlawful interference with his privacy, family, home or correspondence, nor to unlawful attacks on his honor or reputation. Everyone has the right to the protection of the law against such interference or attacks."


## Features v1.1

<p align="center" >
  <a href="https://xerohack.com/chaya/" >
    <img src="https://i.ibb.co/mR1WNwk/chaya-alpha1.png" alt="chaya_v1">
  </a>
</p>

- [x] Supports AES-256-GCM cryptography
- [x] Supports Standard LSB steganography
- [x] Supports LSB-LPS steganography
- [x] Supports FLIF lossless compression
- [x] Cipher data logs as json
- [x] Analytics support for your experiments
- [x] Supports json to csv conversions
- [x] Highly verbose cipher data logs
- [x] Workspace Cleaner
- [x] Easy installer for initial setup

## Changelog v1.1

- (bug fix) missing tqdm from requirements.txt
- (improvement) install.py for easy dep installations
- (improvement) readme
- (improvement) changelog for github

Changelog (main channel): https://github.com/xerohackcom/Chaya/blob/main/CHANGELOG.md
Changelog (dev channel): https://github.com/xerohackcom/Chaya/blob/dev/CHANGELOG.md

## Intallation

### One Line Setup

Use the following command for faster setup:

**Command For Ubuntu Based Distros**

```shell
sudo apt install python3-pip && sudo apt install git && git clone --depth=1 https://github.com/xerohackcom/Chaya.git && cd Chaya && pip3 install -r requirements.txt && sudo apt update && sudo apt-add-repository ppa:linuxuprising/libpng12 && sudo apt update && sudo apt install -y libpng12-0
```

**Command For Debian Based Distros**

```shell
sudo apt install python3-pip && sudo apt install git && git clone --depth=1 https://github.com/xerohackcom/Chaya.git && cd Chaya && pip3 install -r requirements.txt && sudo apt update && sudo apt install build-essential devscripts && cd ~/ && sudo touch /etc/apt/sources.list.d/libpng12.list && echo "deb http://ppa.launchpad.net/linuxuprising/libpng12/ubuntu hirsute main" | sudo tee -a /etc/apt/sources.list.d/libpng12.list && echo "deb-src http://ppa.launchpad.net/linuxuprising/libpng12/ubuntu hirsute main" | sudo tee -a /etc/apt/sources.list.d/libpng12.list && sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys && sudo apt update && sudo apt install -y libpng12-0
```

### Using Installer.py

You can install the dependencies using installer.py script. Run the following commands in terminal:

```shell
sudo apt install python3-pip && sudo apt install git && git clone --depth=1 https://github.com/xerohackcom/Chaya.git && cd Chaya
````

**Ubuntu Based Distros**
```shell
python3 installer.py --ubuntu
````

**Debian Based Distros**
```shell
python3 installer.py --debian
````


## Usage


### Help Menu

```python
python3 chaya.py --help
```

### Automatic Operations

- First add few images (png format) to /autoexp/image_raw/
- Remove the txt file from all autoexp sub-folders to avoid errors! 
- Run the following command

```python
python3 chaya.py -enc
```

### Output

- Enc + Steg images -> /autoexp/image_steg/
- Enc + Steg + Comp images -> /autoexp/image_steg_comp/
- Cipher data -> /appdata/cipher_data.json
- Analysis data -> /appdata/analysis_results_enc.json


## Scheduled v2

- [ ] test and add support for JXL (JpegXL)
- [ ] -----> replace flif with jxl as default
- [ ] add analytic subnode - sub analytics after generating main csv
- [ ] -----> comparisons - values only csv
- [ ] -----> comparisons plotter
- [ ] manual experiment mode
- [ ] linear payload chains
- [ ] -----> auto chunk payload for optimal storage in multiple images
- [ ] linked payload chains
- [ ] -----> randomize storage for added security against reversing
- [ ] payload in-memory execution for evading on-disk forensics
- [ ] video steganography support using ffmpeg

### The Plan
The plan is to build this into a modular framework where users can also add their custom scripts for encryption and steganography part. Support for multiple compression algorithms is being added. During the experiments, FLIF was supported, but now JpegXL (JXL) is the new best lossless raster based compression. Support for payload execution and other interesting stuff underway. Can be done combining commands, but not inbuilt. Video steganography using ffmpeg is being tested. ZG9udCBsZXQgdGhlIGdsb3dpZXMga25vdyBoYWhh
  

