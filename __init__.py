#/urs/bin/python3

#import tkinter
import vlc3
import keyboard
hk = []
elementezahl = 0

configurationsdatei = 'PYSB.config'

#WINDOW = tkinter.Tk()
#s1 = vlc3.MediaPlayer("lfl.mp3")
#s2 = vlc3.MediaPlayer("bbs.mp3")

#def play1():
#    s1.play()

#def play2():
#    s2.play()
#evtl python-argparse für kommandozeilen interpretierung
#python-regex

def play(tondatei):
    print(str(tondatei))
    player = vlc3.MediaPlayer(tondatei)
    player.play()
    
def readconfig(configdatei):
    hk=[]
    configuration = open(configdatei, "r")
    #print ("Name of the file: ", configuration.name)
    #print ("Closed or not : ", configuration.closed)
    #print ("Opening mode : ", configuration.mode)
    for i in configuration:
        hk.append(i.strip())
        print("Zeile in der Config Datei   :"+i)
        print("hotkeys-variable:::")
        print(*hk, sep=', ')
        print(":::")
    return hk

def startlisten(hk):
    num=0
    elementezahl=len(hk)
    print( "Elemente in der Liste: " + str(elementezahl))
    while num <= elementezahl:
        if num>=elementezahl:
            break
        hotkey=str(hk[num+1].strip())
        befehl=hk[num].strip()
        print("Durchlauf "+str(num)+"   Hotkey:"+hotkey+"   Befehl:"+befehl)
        keyboard.add_hotkey(hotkey, lambda: play(befehl))
        num += 2


    #keyboard.add_hotkey("ä", lambda: play("bbs.mp3"))
    #keyboard.add_hotkey("ö", lambda: play("lfl.mp3"))
#    for i in hk:
#        print(num+":::"+hk[num]+":::"+hk[num+1])
#        keyboard.add_hotkey(hk[num+1], play(hk[num]))
#        num += 1
#keyboard.add_hotkey('ö', play1)
#keyboard.add_hotkey('ä', play2)


hotkeys=readconfig("PYSB.config")
#readconfig("PYSB.config")
startlisten(hotkeys)
#startlisten()
#tastendruck = ' '
#while tastendruck != 'q' :
#  tastendruck = ' '
#  tastendruck = keyboard.read_key(suppress=True)
#  print('---',tastendruck,'---')
#  if tastendruck == 'q':
#      break
#  if tastendruck == 'ö':
#      play('lfl.mp3')
#  elif tastendruck == 'ä':
#      play('bbs.mp3')

#tastendruck = ' '
#while tastendruck != 'q' :
#  tastendruck = ' '
#  tastendruck = keyboard.read_key(suppress=True)
##  tastqendruck = keyboard.read_key()
#  print('---',tastendruck,'---')
#  if tastendruck == 'q':
#      break
 
#  if tastendruck == 'ö':
#    play('lfl.mp3')
#  elif tastendruck == 'ä':
#     play('bbs.mp3')

#WINDOW.mainloop()

#keyboard.


################### QT Fenster
from Ui_PYSB import Ui_MainWindow
from PyQt5 import QtWidgets
class myMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(myMainWindow, self).__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":  #fenster von qt designer importieren (Ui_PYSB.py)
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
