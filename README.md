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

Chaya is for your privacy. Chaya is backed by research (I will publish public version whitepaper on xerohack.com), and has proven to be by far the most effective image steganography tool as compared to other FOSS image steganography tools.

**WHY CHAYA IS BETTER THAN THE REST?**

- [x] 0% detection rate using most of the publically available anti-steg tools like stegexpose and many more
- [x] 100% data retention with almost the same capacity of standard LSB technique with LBS-LPS
- [x] Transparent cryptography that gets as good as python has to offer

***There is no way this can be broken using a standard supercomputer unless there are exploits in python libs and python itself.. LSB-LPS will take exponetially large time to brute-force with larger graph images because you will have to attack every X,Y coordinates combo without any error. Making an ML to do so is also quite useless and can be only used for Natural language processing for example: which message is readable to find the coordinates. AFTER THAT, you have to break the encryption. MOREOVER, NLP ML cannot find the coordinates because the bruteforce results will be ciphertext anyway. If for some reason the attacker knows the coordinates to start the de-steg process, they will have to break AES-GCM-256. GCM is better because it offers integrity along with confidentiality, which is why it's the better AES mode).***

<strong><a href="https://www.un.org/en/about-us/universal-declaration-of-human-rights">United Nations Declaration of Human Rights (UDHR) 1948, Article 12 - </strong></a>“No one shall be subjected to arbitrary interference with his privacy, family, home or correspondence, nor to attacks upon his honor and reputation. Everyone has the right to the protection of the law against such interference or attacks.”
<br><br>
<strong><a href="https://en.wikipedia.org/wiki/International_Covenant_on_Civil_and_Political_Rights">International Covenant on Civil and Political Rights (ICCPR) 1966, Article 1 - </strong></a>"No one shall be subjected to arbitrary or unlawful interference with his privacy, family, home or correspondence, nor to unlawful attacks on his honor or reputation. Everyone has the right to the protection of the law against such interference or attacks."


## Features v1.2

<p align="center" >
  <a href="https://xerohack.com/" >
    <img src="https://xerohack.com/assets/images/chaya_1.2.png" alt="chaya_v1.2">
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
- [x] Comes with easy updater

### Changelogs

Changelog (main channel): https://github.com/xerohackcom/Chaya/blob/main/CHANGELOG.md
Changelog (dev channel): https://github.com/xerohackcom/Chaya/blob/dev/CHANGELOG.md


## Installation

### One Line Setup

Use the following command for faster setup:

**Command For Ubuntu Based Distros**

```shell
sudo apt install python3-pip && sudo apt install git && git clone --depth=1 https://github.com/xerohackcom/Chaya.git && cd Chaya && pip3 install -r requirements.txt && sudo apt update && sudo apt-add-repository ppa:linuxuprising/libpng12 && sudo apt update && sudo apt install -y libpng12-0
```

**Command For Debian Based Distros**

```shell
sudo apt install python3-pip && sudo apt install git && git clone --depth=1 https://github.com/xerohackcom/Chaya.git && cd Chaya && pip3 install -r requirements.txt && sudo apt update && sudo apt install build-essential devscripts && cd ~/ && sudo touch /etc/apt/sources.list.d/libpng12.list && echo "deb https://ppa.launchpadcontent.net/linuxuprising/libpng12/ubuntu hirsute main" | sudo tee -a /etc/apt/sources.list.d/libpng12.list && echo "deb-src https://ppa.launchpadcontent.net/linuxuprising/libpng12/ubuntu hirsute main" | sudo tee -a /etc/apt/sources.list.d/libpng12.list && sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 1CC3D16E460A94EE17FE581CEA8CACC073C3DB2A && sudo apt update && sudo apt install -y libpng12-0
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

### Output Data

- Enc + Steg images -> /autoexp/image_steg/
- Enc + Steg + Comp images -> /autoexp/image_steg_comp/
- Cipher data -> /appdata/cipher_data.json
- Analysis data -> /appdata/analysis_results_enc.json


## Future Plan
The plan is to build this into a modular framework where users can also add their custom scripts for encryption and steganography part. Support for multiple compression algorithms is being added. During the experiments, FLIF was supported, but now JpegXL (JXL) is the new best lossless raster based compression. Support for payload execution and other interesting stuff underway. Can be done combining commands, but not inbuilt. Video steganography using ffmpeg is being tested.

Please refer to the PLANLOG for detailed feature plans: https://github.com/xerohackcom/Chaya/blob/main/PLANLOG.md


## License

Chaya is licensed under <a href="https://github.com/xerohackcom/Chaya/blob/main/LICENSE">AGPLv3</a>

## Contributions

Helping to report bugs and fix issues is appreciated.

## Support Chaya!

You can support Chaya by Monero XMR donations: https://xerohack.com/support.php

<p align="center">
  <img src="https://xerohack.com/assets/images/monero.png">
  <Br><br>
  <b>Address:</b> 4BJLkV4GyaHCYgGSqYBAe418jzaUz6FPe8M14U49SzL5GG81YyoVtWABgJszGUdpUf6MNoWL4kJu7KqQFnWxDvXi34QeA7n
</p>
