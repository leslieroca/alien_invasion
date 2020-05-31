# Building Alien Invasion

Steps were tested in Ubuntu 20.04 LTS with Python 3.8.2.  

### 1. Install pip3
```bash
sudo apt-get install python3-pip
```

### 2. Install Pygame
First, install some system dependencies and libraries Pygame needs.
```bash
sudo apt-get install python3.8-dev mercurial
sudo apt-get install libsdl-image1.2-dev libsdl2-dev libsdl-ttf2.0-dev
```
Install the next libraries to enable advanced abilities such as play sounds.
```bash
sudo apt-get install libsdl-mixer1.2-dev libportmidi-dev
sudo apt-get install libswscale-dev libsmpeg-dev libavformat-dev libavcode-dev
sudo apt-get install libfreetype6-dev
sudo apt-get install python-numpy
```
Install Pygame
```bash
python3 -m pip install -U pygame --user
```

### 3. Run the game.
```bash
python3 src/alien_invasion.py
```


