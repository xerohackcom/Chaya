import subprocess
from core.colors import *
from core.utils import msg_status

def flif(opt, src, dst):
    if opt == 'e':
        flif_args = f"./flif -r0 {src} {dst}"
    elif opt == 'd':
        flif_args = f"./flif -d -r0 {dst} {src}"
    msg_status("INFO", f"{c_blue}[Executing]{c_green} {flif_args}")
    try:
        proc = subprocess.Popen([flif_args], stdout=subprocess.PIPE, shell=True)
        (output, err) = proc.communicate()
        proc_status = proc.wait()
        #msg_status("INFO", f"Status: {output}\nError: {err}") # use for debugging
    except Exception as e:
        msg_status("ERROR", f"{e}")
