import os
import shutil

from copy_contents import copy_contents


static_dir = "./static"
public_dir = "./public"


def main():
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)

    copy_contents(static_dir, public_dir)

main()