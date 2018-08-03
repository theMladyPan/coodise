# -*- coding: utf-8 -*-

import os
from .file import File
from .. import settings



def parse_directory(directory):
    full_path = os.path.join(settings.MEDIA_DIR,directory)
    items = os.listdir(full_path)
    parent = File(full_path,"..", True)
    parent.media_type.image = "up.png"
    directories, files = [parent], []

    for item in items:
        file = File(full_path, item)
        if file.is_dir:
            file.media_type.type = "Folder"
            file.media_type.deduce_image()
            directories.append(file)
        else:
            files.append(file)


    return [directories, files]
