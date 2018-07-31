import os
from .. import settings

class MediaType:
    def __init__(self, type):
        pass


class File:
    def __init__(self, path, name):
        self.name = name
        self.full_path = os.path.join(path, name)
        self.is_dir = os.path.isdir(self.full_path)
        self.is_file = os.path.isfile(self.full_path)
        self.type = MediaType(None)  # media, music, video ...

    def __repr__(self):
        return self.name

    def get_full_path(self):
        return self.full_path


def parse_directory(directory):
    full_path = os.path.join(settings.MEDIA_DIR,directory)
    items = os.listdir(full_path)
    directories, files = [File(full_path,"..")], []

    for item in items:
        file = File(full_path, item)
        if file.is_dir:
            directories.append(item)
        else:
            files.append(item)

    return [directories, files]


def get_list(directory):
    text=""
    dir=os.listdir(settings.MEDIA_DIR+directory)
    dir.sort()
    topdir=""
    for i in directory.split("/")[:-2]:
        topdir+=i+"/"
    text+='<li><a href="?path=%s"><img src="server_files/folder.png" height="33" width="33">..</a></li>'%(topdir)
    for i in dir:
      try:
        os.chdir('/var/www/html/'+directory+'/'+i)
        os.chdir('..')
        if i != 'server_files': text+='<li><a href="?path=%s/"><img src="server_files/folder.png" height="33" width="33">%s</a></li>'%(directory+i,i[:50])
      except:
        pass

    for i in dir:
      try:
        os.chdir('/var/www/html/'+directory+'/'+i)
        os.chdir('..')

      except:
        if i[0]=='.' or ('index.' in i and directory==''):
          pass
        else:
          if '.png' in i or '.jpg' in i or '.JPEG' in i or '.jpeg' in i or  '.PNG' in i or '.JPG' in i or '.BMP' in i or '.bmp' in i or '.gif' in i or '.GIF' in i or '.tiff' in i or '.tif' in i:
            image='server_files/image.png'
          elif '.flac' in i or '.mp3' in i or '.MP3' in i or '.wma' in i or '.WMA' in i or  '.WAV' in i or '.wav' in i or '.ogg' in i or '.OGG' in i:
            image='server_files/audio.png'
          elif '.mov' in i or '.MOV' in i or '.mkv' in i or '.MKV' in i or '.avi' in i or '.AVI' in i or '.mp4' in i or '.MP4' in i or '.MPEG' in i or '.mpeg' in i or  '.MPG' in i or '.mpg' in i or '.WMV' in i or '.wmv' in i or '.divx' in i:
            image='server_files/video.png'
          else:
            image='server_files/doc.png'
          text+='<li>%s<a href="%s"><img src="%s" height="33" width="33">%s</a></li>'%(multimedia(directory+i), directory+i.replace(' ', '%20'), image,link(i))


    return text
