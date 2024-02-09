#!/usr/bin/env python

import os
import shutil

copy_dir = ["KnobScripter"]

def build(source_path, install_path):
    '''
    build by simple copy
    '''

    for name in copy_dir:
        src = os.path.join(source_path, name)
        dst = os.path.join(install_path, name)

        if os.path.exists(src):
            print("src: {}".format(src))
            print("dst: {}".format(dst))
            if os.path.exists(dst):
                shutil.rmtree(dst)
            shutil.copytree(src, dst)
    
    # make sure to copy menu.py
    src = os.path.join(source_path, "menu.py")
    dst = os.path.join(install_path, "menu.py")
    shutil.copy2(src, dst)


if __name__ == '__main__':
    build(
        source_path=os.environ['REZ_BUILD_SOURCE_PATH'],
        install_path=os.environ['REZ_BUILD_INSTALL_PATH'],
    )