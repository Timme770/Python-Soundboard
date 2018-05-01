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

def play(hk):
#    print(*hk)
#    print(hk.index(hotkey))
#    print(keyboard.key_to_scan_codes(keyboard.stash_state()))
    hotkeypressed=keyboard.key_to_scan_codes(keyboard.stash_state())
#    print(hotkeypressed[0])
#    print(hotkeypressed)
    try:
        IndexInHK=hk.index(hotkeypressed[0])
    except:
        print("Variable "+hotkeypressed[0]+" nichtgefunden")
#    print("index in hk var:"+str(IndexInHK))
    hotkeyname=hk[IndexInHK-1]
#    print(hotkeyname[0])
    tondatei=hk[IndexInHK-2]
    print("""
    #################################
    #                               play funktion                              #""")
    print("# Hotkey-Liste                      :")
    print(*hk)
    print("# Hotkeycode-Direkt ausgelesen      : "+str(keyboard.key_to_scan_codes(keyboard.stash_state())))
    print("# Hotkey in variable gepackt (tulpe): "+str(hotkeypressed))
    print("# Hotkey wert 0 der tulpe           : "+str(hotkeypressed[0]))
    print("# Index in hk var                   : "+str(IndexInHK))
    print("# Hotkeyname                        : "+hotkeyname[0])
    print("# Abzuspielende Datei               : "+str(tondatei))
    
    player = vlc3.MediaPlayer(tondatei)
    player.play()
    
def readconfig(configdatei):
    hk=[]
    configuration = open(configdatei, "r")
    #print ("Name of the file: ", configuration.name)
    #print ("Closed or not : ", configuration.closed)
    #print ("Opening mode : ", configuration.mode)
    durchl=1
    for i in configuration:
        hk.append(i.strip())
        if durchl == 2:
            keynummer=keyboard.key_to_scan_codes(i.strip())
            hk.append(keynummer[0])
            print(keynummer[0])
            durchl=0
        print("Zeile in der Config Datei   :"+i)
        print("hotkeys-variable:::")
        print(*hk, sep=', ')
        print(":::")
        durchl += 1
    return hk

def startlisten(hk):
    num=0
    elementezahl=len(hk)
    print( "Elemente in der Liste: " + str(elementezahl))
    while num <= elementezahl:
        if num>=elementezahl:
            return
        hotkey=str(hk[num+1].strip())
        keynummer=hk[num+2]
        befehl=hk[num].strip()
        print("Durchlauf "+str(num)+"   Hotkey:"+hotkey+"-"+str(keynummer)+"   Befehl:"+befehl)
        #keyboard.add_hotkey(hotkey, lambda: play(befehl))
        print(id(befehl))
        keyboard.add_hotkey(hotkey, lambda: play(hk))
        num += 3


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
