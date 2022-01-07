import os, sys, zipfile
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
from core.utils import *

# Function > Download Updated Archive
def download_update():
	runtime = current_runtime()
	url = f"https://github.com/xerohackcom/Chaya/archive/refs/heads/{runtime}.zip"
	download_file(url, "req")


# Function > Extract Archive
def extract_archive():
	runtime = current_runtime()
	with zipfile.ZipFile(f"{get_current_script_path().replace('core/utils.py', f'downloads/{runtime}.zip')}", "r") as zip_ref:
		zip_ref.extractall(f"{get_current_script_path().replace('core/utils.py', f'downloads/')}")


# Function > Cleanup & Replace
def update_setup():
	runtime = current_runtime()
	run_cmd(f"rm -rf {get_current_script_path().replace('core/utils.py', f'downloads/Chaya-{runtime}/updater')}")
	chaya_files = get_files_in_dir(f"{get_current_script_path().replace('core/utils.py', '')}")
	chaya_dirs = next(os.walk(f"{get_current_script_path().replace('core/utils.py', '')}"))[1]
	
	# delete folders and files except /updater, /downloads
	for cdir in chaya_dirs:
		if cdir != "updater":
			if cdir != "downloads":
				cdir = f"{get_current_script_path().replace('core/utils.py', f'{cdir}')}"
				msg_status("WARNING", f"{c_red}Deleting Directory > {c_white}{cdir}")
				run_cmd(f"rm -rf {cdir}")
	for cfile in chaya_files:
		cfile = f"{get_current_script_path().replace('core/utils.py', f'{cfile}')}"
		msg_status("WARNING", f"{c_red}Deleting File > {c_white}{cfile}")
		run_cmd(f"rm -rf {cfile}")

	# move folders and files from /downloads/chaya-runtime/
	new_chaya_files = get_files_in_dir(f"{get_current_script_path().replace('core/utils.py', f'downloads/Chaya-{runtime}/')}")
	new_chaya_dirs = next(os.walk(f"{get_current_script_path().replace('core/utils.py', f'downloads/Chaya-{runtime}/')}"))[1]

	# move new folder and files except /updater, /downloads
	for ndir in new_chaya_dirs:
		if ndir != "updater":
			if ndir != "downloads":
				ndir = f"{get_current_script_path().replace('core/utils.py', f'downloads/Chaya-{runtime}/{ndir}')}"
				msg_status("WARNING", f"{c_red}Moving Directory > {c_white}{ndir}")
				run_cmd(f"mv {ndir} f'{get_current_script_path().replace('core/utils.py', f'{ndir}')}'")
	for nfile in new_chaya_files:
		nfile = f"{get_current_script_path().replace('core/utils.py', f'downloads/Chaya-{runtime}/{nfile}')}"
		msg_status("WARNING", f"{c_red}Moving File > {c_white}{nfile}")
		run_cmd(f"mv {nfile} f'{get_current_script_path().replace('core/utils.py', f'{nfile}')}'")


if __name__ == "__main__":
	download_update()
	extract_archive()
	update_setup()
