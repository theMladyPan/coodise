import os
from .. import settings

class MediaType:
    def __init__(self, filename = "", type = None):
        if type is not None:
            self.type = type
        else:
            self.type = self.yield_type_from_filename(filename)
        self.deduce_image()
        self.filename = filename

    def get_type(self):
        return self.type

    def yield_type_from_filename(self, filename):
        extension = filename.split(".")[-1].lower()
        d_extensions = dict()
        d_extensions["video"] = ["webm", "avi", "mov", "mkv","mp4","3gp","divx","mpeg","mpg"]
        d_extensions["picture"] = ["png", "jpg", "jpeg","tif","tiff","bmp","gif"]
        d_extensions["audio"] = ["mp3","flac","ogg","wav","wma"]
        d_extensions["text"] = ["txt","py", "pyw", "cpp","log", "srt", "c", "m", "h", "hpp"]  # TODO: extend this list

        if extension in d_extensions["picture"]:  # TODO: implement other types
            return "Picture"
        elif extension in d_extensions["video"]:
            return "Video"
        elif extension in d_extensions["audio"]:
            return "Audio"
        elif extension in d_extensions["text"]:
            return "Text"
        else:
            return None

    def deduce_image(self):
        if self.type:
            if self.type == "Picture":  # TODO: implement other types
                self.image = "image.png"
            elif self.type == "Video":
                self.image = "video.png"
            elif self.type == "Folder":
                self.image = "folder.png"
            elif self.type == "Audio":
                self.image = "audio.png"
            elif self.type == "Image":
                self.image = "disc.png"
            else:
                self.image = "doc.png"
        else:
            self.image = "doc.png"


class File:
    def __init__(self, path, name, is_parent = False):
        self.name = name
        if is_parent:
            self.full_path = "/".join(path.split('/')[:-1])
        else:
            self.full_path = os.path.join(path, name)
        self.is_parent = is_parent
        self.is_dir = os.path.isdir(self.full_path)
        self.is_file = os.path.isfile(self.full_path)
        self.media_type = MediaType(name)  # media, music, video ...
        self.relative_path = self.full_path.split(settings.MEDIA_DIR)[1]
    def __repr__(self):
        return self.name

    def get_full_path(self):
        return self.full_path

    def get_media_type(self):
        return self.media_type.get_type()

    def get_content(self):
        with open(self.full_path, "r") as ofile:
            return ofile.read()
