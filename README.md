# Coodise
Coodise, a homeserver in Django for interfacing (and streaming) content from local Storage throught HTTP


## Contains:
Coodise [source code](coodise/)

## Main branch:
for now, [devel](https://github.com/theMladyPan/coodise/tree/devel)

## How to:
### Install and run for development

Make sure you are using latest version of **`python 3.6`** or higher

1. Install pip with your favourite package manager (skip if already installed):
```bash
foo@bar:~/$ sudo apt install python3-pip
```
2. install django:
```bash
foo@bar:~/$ pip3 install django
```
3. clone this repo:
```bash
foo@bar:~/$ git clone https://github.com/theMladyPan/coodise.git
```
4. inside repo, link your cloud and run server
```bash
foo@bar:~/$ cd coodise
foo@bar:~/coodise$ ln -s /path/to/my/storage ./Cloud
foo@bar:~/coodise$ python3 manage.py runserver
```

#### Making server public
in coodise/settings.py, line ALLOWED_HOSTS, change it to desired hosts, set to [0] for everybody or temporarily run with:
```bash
foo@bar:~/coodise$ python3 manage.py runserver 0:8000
```
