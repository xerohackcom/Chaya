
<p align="center" >
  <a href="https://xerohack.com/chaya/" >
    <img src="https://i.ibb.co/X2WmCxm/chaya.png" alt="chaya">
  </a>
</p>


<h2 align="center">Chaya</h2>

<p align="center">
  <br><br>
  <strong>Advance Image Steganography</strong>
  <br><br>

<p>Using LSB-LPS + AES-256-GCM + FLIF

## Right To Privacy!

<strong><a href="https://www.un.org/en/about-us/universal-declaration-of-human-rights">United Nations Declaration of Human Rights (UDHR) 1948, Article 12 - </strong></a>“No one shall be subjected to arbitrary interference with his privacy, family, home or correspondence, nor to attacks upon his honor and reputation. Everyone has the right to the protection of the law against such interference or attacks.”
<br><br>
<strong><a href="https://en.wikipedia.org/wiki/International_Covenant_on_Civil_and_Political_Rights">International Covenant on Civil and Political Rights (ICCPR) 1966, Article 1 - </strong></a>"No one shall be subjected to arbitrary or unlawful interference with his privacy, family, home or correspondence, nor to unlawful attacks on his honor or reputation. Everyone has the right to the protection of the law against such interference or attacks."

With Chaya, you can easily protect your privacy by using steganography. Chaya experiments showcase very promising results by evading detection against various attacks against steganography.


## Released v1

- [x] automatic experiment mode
- [x] automatic jpg to png (if specified)
- [x] json data to csv conversion (if specified)
- [x] support for lsb only steganography
- [x] add encrypted message size in json data
- [x] convert cipher_data.json to cipher_data.csv
- [x] add silent mode (default - verbose)
- [x] workspace cleaner

## Intallation

FLIF support only works with the following Operating Systems completely!:

- Ubuntu / Pop!_OS / Linux Mint / Blackbuntu
- All other Linux distributions that support PPA / Ubuntu based

FLIF compression has to be commented from the script for 'Kali Linux', 'Parrot OS' and other direct Debian based system that don't support PPA. This means your compression will not work, but the steganography will work perfectly. Recommended to use a Ubuntu/PopOS VM and use this script.

### Python Setup

If already done, skip to next step.

```python

sudo apt install python3-pip

```

### Get Repository

```python

git clone --depth=1 https://github.com/xerohackcom/Chaya.git && cd Chaya && pip3 install -r requirements.txt

```

### System Setup

```

sudo apt-add-repository ppa:linuxuprising/libpng12
sudo apt update
sudo apt install libpng12-0

```

### Usage


#### Help Menu

```python

python3 chaya.py --help

```

#### Automatic Operations

- First add few images (png format) to /autoexp/image_raw/
- Run the following command

```python

python3 chaya.py -enc

```

#### Output

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
  

