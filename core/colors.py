import sys, os, platform


color = True
machine = sys.platform
checkplatform = platform.platform()

if machine.lower().startswith(('os', 'win', 'darwin', 'ios')):
    color = False
if checkplatform.startswith("Windows-10") and int(platform.version().split(".")[2]) >= 10586:
    color = True
    os.system('')
if not color:
    c_white = c_green = c_red = c_yellow = c_blue = c_bold = c_clean = c_cyan = ''
else:
    c_white, c_green, c_red, c_yellow, c_blue, c_bold, c_clean, c_cyan = '\033[97m', '\033[92m', '\033[91m', '\033[93m', '\033[94m', '\033[1m', '\033[0m', '\033[36m'
