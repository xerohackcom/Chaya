from __future__ import ( division, absolute_import, print_function, unicode_literals )

import sys, os, tempfile, logging, zipfile, shutil, re, urllib.request
from distutils.dir_util import copy_tree
import urllib.parse as urlparse

def runlevel():
    runlevel = "dev"
    with open('updater/RUNLEVEL.txt') as f:
        runlevel = f.readline()
        return runlevel

def perform_update():
    file_list, files_to_remove = [], []

    runlevel = runlevel()

    # extract archive
    print("Extracting archive")
    with zipfile.ZipFile(f"{runlevel}.zip","r") as zr:
        zr.extractall("")
    # remove 'updater' folder from extracted
    print("Removing 'updater' folder")
    shutil.rmtree(f'Chaya-{runlevel}/updater', ignore_errors=True)
    # remove all items in old dir
    for root, dirs, files in os.walk(os.path.abspath("../")):
        for file in files:
            temppath = f"{os.path.join(root, file)}"
            file_list.append(temppath)
    # discover files to remove
    for filepath in file_list:
        if filepath.find("updater") == -1: # removed instances of items with "updater"
            if filepath.find(".git") == -1:
                files_to_remove.append(filepath)
    # delete old files
    for filepath in files_to_remove:
        try:
            os.remove(filepath)
        except Exception as e:
            raise e
    # copy extracted dir contents to old dir
    copy_tree(f"Chaya-{runlevel}", "../")
    print("Update Complete!")


def download_file(url, dest=None):
    """ 
    Download and save a file specified by url to dest directory,
    """
    u = urllib.request.urlopen(url)

    scheme, netloc, path, query, fragment = urlparse.urlsplit(url)
    filename = os.path.basename(path)
    if not filename:
        filename = 'downloaded.file'
    if dest:
        filename = os.path.join(dest, filename)

    with open(filename, 'wb') as f:
        meta = u.info()
        meta_func = meta.getheaders if hasattr(meta, 'getheaders') else meta.get_all
        meta_length = meta_func("Content-Length")
        file_size = None
        if meta_length:
            file_size = int(meta_length[0])
        print(f"Downloading: {url} Bytes: {file_size}")

        file_size_dl = 0
        block_sz = 8192
        while True:
            buffer = u.read(block_sz)
            if not buffer:
                break

            file_size_dl += len(buffer)
            f.write(buffer)

            status = f"{file_size_dl}"
            if file_size:
                status += "   [{0:6.2f}%]".format(file_size_dl * 100 / file_size)
            status += chr(13)
            print(status, end="")
        print()

    return filename


if __name__ == "__main__":  # Only run if this file is called directly
    print("Updating Chaya")
    runlevel = runlevel()
    url = f"https://github.com/xerohackcom/Chaya/archive/{runlevel}.zip"
    filename = download_file(url)
    print(filename)
    perform_update()
