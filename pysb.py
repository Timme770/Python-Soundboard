#!/usr/bin/python3
#
# ***********************************************************************************************************************
#    This file is part of PYSB Python Soundboard.
#
#    Authors: Tim H. <contact at https://discord.gg/8hRXDnM (TuxPlayDE#6693), https://www.twitch.tv/tuxplayde>
#                   Alexander Glüsing <alexandergluesing@posteo.de>
#
#    PYSB Python Soundboard is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    PYSB Python Soundboard is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with PYSB Python Soundboard.  If not, see <http://www.gnu.org/licenses/>.
# ***********************************************************************************************************************

# #############################################################
#    Python Modul nachinstallieren: 'pip install keyboard'
# #############################################################

# ---    keyboard.get_hotkey_name(names=None)
# ---
# ---[source]
# ---
# ---Returns a string representation of hotkey from the given key names, or
# ---the currently pressed keys if not given. This function:
# ---
# ---    normalizes names;
# ---    removes "left" and "right" prefixes;
# ---    replaces the "+" key name with "plus" to avoid ambiguity;
# ---    puts modifier keys first, in a standardized order;
# ---    sort remaining keys;
# ---    finally, joins everything with "+".
# ---
# ---Example:
# ---
# ---get_hotkey_name(['+', 'left ctrl', 'shift'])
# ---# "ctrl+shift+plus"
# ---
# ---
# ---    print(hotkeypressed[0])
# ---    print(hotkeypressed)

# evtl. python-argparse für Kommandozeilen Interpretierung
# python-regex

# TODO per entry Volume
# TODO neues Tuple Dateiformat siehe: pickle und shelve
#

import vlc3 as vlc
import keyboard  # , time
from tkinter import filedialog
from tkinter import *

if sys.hexversion >= 0x03010000:
    # use some advanced feature
    print("Deine Version passt.")
else:
    print("Benutze python 3 :D")
    # use an alternative implementation or warn the user

configurationsdatei = 'PYSB.config'
hk = []


# ----------------- Tk- Dialog --------------------
# TODO löschen von Einträgen

class hotkeyerkennenDialog:
    def __init__(self, parent):
        top = self.top = Toplevel(parent)

        self.frameLabel = Frame(top)
        self.frameLabel.pack(pady=5, padx=5)

        self.l1 = Label(self.frameLabel, text="Erkannter Shortcut: ")
        self.l1.pack(side=LEFT)
        self.e = Entry(self.frameLabel)
        self.e.pack(side=RIGHT, padx=5)

        self.b = Button(top, text="OK", command=self.ok)
        self.b.pack(side=LEFT, pady=5)
        self.b2 = Button(top, text="Hotkey erkennen", command=self.recordkey)
        self.b2.pack(side=RIGHT, pady=5)

    def ok(self):
        root.hotkeyAufnahme = self.e.get()
        self.top.destroy()

    def recordkey(self):
        self.b.focus()  # habe den focus hier auf den button gesetzt, damit die registrierte tasteneingabe (eventueller einzelner buchstabe oder zahl nicht im eingabefeld landen kann. Praktisch könnte zudem auch sein, wenn dann gleich durch bestätigen mit enter der Dialog Bestätigt werden kann.)
        test = keyboard.read_hotkey(suppress=False)

        self.e.delete(0, END)
        self.e.insert(0, test)


def play(hk):
    try:
        hotkeypressed = keyboard.get_hotkey_name()
        for i in hk:
            if i[1] == hotkeypressed:
                media = root.instanz_vlc.media_new(i[0])
#                print("mediavariable: " + str(media))
                root.player.set_media(media)
                root.player.play()
    except:
        print(
            "Variable " + hotkeypressed + " wurde nicht gefundenoder es ist etwas in der funktion 'def play(hk) schiefgelaufen'")


def startlisten(hk):
    for i in hk:
        # test=keyboard.add_hotkey(i[1], lambda: play(hk))
        root.listenkeyeventhandlerliste.append(keyboard.add_hotkey(i[1], lambda: play(hk)))


def stoplisten():
    for i in root.listenkeyeventhandlerliste:
        keyboard.remove_hotkey(i)
    root.player.stop()
    root.listenkeyeventhandlerliste = []


def volumeset(event):
    if root.player == None:
        return
    volume = int(event)
    if volume > 100:
        volume = 100
    if root.player.audio_set_volume(volume) == -1:
        print('schschschsch... self.errorDialog("Failed to set volume")')


def readconfig(configdatei):
    lauf = 0
    hk = []
    zeile1_pfad = ""
    zeile2_hk = ""
    with open(configdatei, "r") as configuration:
        for i in configuration:
            lauf = lauf + 1
            if lauf == 1:
                zeile1_pfad = i.strip()
            elif lauf == 2:
                zeile2_hk = i.strip()

                hk.append((zeile1_pfad, zeile2_hk))
                lauf = 0
        configuration.close()
    return hk


def reloadconfiganddisplay(configdatei):
    root.hotkeys = readconfig(configdatei)
    configinlistenladen()


def writeconfig(configdatei, hk):
    with open(configdatei, "w") as configuration:
        for i in hk:
            configuration.write(i[0])
            configuration.write("\n")
            configuration.write(i[1])
            configuration.write("\n")
        configuration.close()


def configinlistenladen():
    listbox_dn.delete(0, END)
    listbox_hk.delete(0, END)
    for i in root.hotkeys:
        listbox_dn.insert(END, str(i[0]))
        listbox_hk.insert(END, str(i[1]))
    listboxenneuereintraghinzufuegen()


def listboxenneuereintraghinzufuegen():
    listbox_dn.insert(END, "Neuer Eintrag...")
    listbox_hk.insert(END, "Neuer Eintrag...")


def listenrechtsklick_hk(event):
    y = str(str(event).split()[5]).strip(
        "y=>")  # im event steht der die zur liste relative posizion des cursors beim click - die so herausgefiltert wird
    listenrechtsklick("hk", y)


def listenrechtsklick_dn(event):
    y = str(str(event).split()[5]).strip(
        "y=>")  # im event steht der die zur liste relative posizion des cursors beim click - die so herausgefiltert wird
    listenrechtsklick("dn", y)


def listenrechtsklick(liste, y):
    auswahl = listbox_dn.nearest(
        y)  # die nearest funktion gibts mit hilfe von y den eintrag an position y wieder (relative koordinate)
    listenrechtsklick_play(listbox_dn.get(auswahl))


def listenrechtsklick_play(file):
    if file != "Neuer Eintrag...":
        media = root.instanz_vlc.media_new(file)
        root.player.set_media(media)
        root.player.play()


def listendoppelklick_hotkey(event):
    root.hotkeyAufnahme = "test"
    d = hotkeyerkennenDialog(root)  # Dialog zum Hotkey Abfragen aufrufen
    root.wait_window(d.top)  # ^^^
    if root.hotkeyAufnahme == "":  # wurde kein Hotkey im Dialog eingegeben?
        print("hotkey wurde nicht aufgenommen/kein hotkey bekomen.")
    else:
        auswahl = listbox_hk.curselection()[0]  # den ausgewählten eintrag in der listbox auslesen
        listbox_hk.delete(auswahl)  # den eintrag in der liste austauschen
        listbox_hk.insert(auswahl, root.hotkeyAufnahme)  # ^^^
        if listbox_hk.size() == (auswahl + 1):  # Der Eintrag für ein neues Element in der Liste wurde geändert/gewaehlt
            root.hotkeys.append(("", str(root.hotkeyAufnahme)))  # Einen neuen Eintrag in der Tuple anlegen
            listbox_dn.delete(
                auswahl)  # Eintrag in der Dateinamen Liste aktualisieren auf ein leeren inhalt (ist ja komplett neu)
            listbox_dn.insert(auswahl, "")  # ^^^
            listboxenneuereintraghinzufuegen()  # Neuen Platzhalter fuer hinzufuegen erstellen.
        else:
            root.hotkeys[auswahl] = ((root.hotkeys[auswahl][0]), str(
                root.hotkeyAufnahme))  # die Tulpe/von der config gelesene liste auch aktualisieren


def listendoppelklick_dateiname(event):
    auswahl = listbox_dn.curselection()[0]  # den ausgewählten eintrag in der listbox auslesen
    try:
        root.neuedatei = filedialog.askopenfilename(initialdir="~/", title="Eine Vlc kompatible Datei auswählen",
                                                    filetypes=[("alle Dateien",
                                                                "*.*")])  # "Audiodateien","*.mp3"),("all files","*.*")))     #(angabe aller audioformate wäre ganz schön mühsam, villeicht später # TODO)
        listbox_dn.delete(auswahl)  # Den Eintrag in der Liste austauschen
        listbox_dn.insert(auswahl, root.neuedatei)  # ^^^
        if listbox_dn.size() == (auswahl + 1):  # Der Eintrag für ein neues Element in der Liste wurde geändert/gewaehlt
            root.hotkeys.append((str(root.neuedatei), ""))  # Einen neuen Eintrag in der Tuple anlegen
            listbox_hk.delete(
                auswahl)  # Eintrag in der Dateinamen Liste aktualisieren auf ein leeren inhalt (ist ja komplett neu)
            listbox_hk.insert(auswahl, "")  # ^^^
            listboxenneuereintraghinzufuegen()  # Neuen Platzhalter fuer hinzufuegen erstellen.
        else:
            root.hotkeys[auswahl] = (
            str(root.neuedatei), root.hotkeys[auswahl][1])  # die Tulpe/von der config gelesene liste auch aktualisieren
    except:
        print("Es wurde keine Datei ausgewählt:")


def listendeletekey_hotkey(event):
    auswahl = listbox_hk.curselection()[0]
    listendelete(auswahl)


def listendeletekey_dateiname(event):
    auswahl = listbox_dn.curselection()[0]
    listendelete(auswahl)


def listendelete(auswahl):
    if listbox_dn.size() > 1:
        listbox_hk.delete(auswahl)
        listbox_dn.delete(auswahl)
        del root.hotkeys[auswahl]
    else:
        print("ähhh")


# TODO irgendwann entfernen? definition zum ausgeben der tuple im terminal
def PRinttuple():
    for i in root.hotkeys:
        print(i[0])
        print(i[1])
        print("\n")


if __name__ == '__main__':
    root = Tk()

    root.title("PySB - Python-Soundboard")
    root.hotkeys = readconfig("PYSB.config")
    root.hotkeyAufnahme = "older shiiit xD"
    root.listenkeyeventhandlerliste = []
    ################ top frame  [ Config / Speichern ]
    frame_saveandreload = Frame(root)
    frame_saveandreload.pack(side=TOP)
    reloadButton = Button(frame_saveandreload, text="Config neu Laden",
                          command=lambda: reloadconfiganddisplay(configurationsdatei))
    saveButton = Button(frame_saveandreload, text="Speichern",
                        command=lambda: writeconfig(configurationsdatei, root.hotkeys))
    reloadButton.pack(side=LEFT, padx=5, pady=5)
    saveButton.pack(side=RIGHT, padx=5, pady=5)

    ################2ter frame  [ Listen ]
    frame_listen = Frame(root)
    frame_listen.pack(fill=BOTH, expand=1)  # side=TOP)

    frame_listenleft = Frame(frame_listen, width=23)
    frame_listenleft.pack(side=LEFT, fill=Y)  # , expand=1)

    frame_listenright = Frame(frame_listen)
    frame_listenright.pack(side=RIGHT, fill=BOTH, expand=1)

    label_hk = Label(frame_listenleft, text="Shortcuts:")
    listbox_hk = Listbox(frame_listenleft)  # , width=20          )
    label_hk.pack(side=TOP)
    listbox_hk.pack(fill=Y, expand=1)

    listbox_dn = Listbox(frame_listenright)  # , width=60          )
    label_dn = Label(frame_listenright, text="Dateinamen:")
    label_dn.pack(side=TOP)
    listbox_dn.pack(side=LEFT, fill=BOTH, expand=1)

    #   listbox_hk.grid(     row=1, column=0, fill=Y   , expand=1)
    #   listbox_dn.grid(     row=1, column=1, fill=BOTH, expand=1)
    listbox_hk.bind('<Button-3>', listenrechtsklick_hk)
    listbox_hk.bind('<Double-Button-1>', listendoppelklick_hotkey)
    listbox_hk.bind('<Delete>', listendeletekey_hotkey)
    listbox_dn.bind('<Button-3>', listenrechtsklick_dn)
    listbox_dn.bind('<Double-Button-1>', listendoppelklick_dateiname)
    listbox_dn.bind('<Delete>', listendeletekey_dateiname)

    configinlistenladen()
    label_editinfo = Label(root,
                           text='(Zum editieren "doppelklicken"         Zum Löschen [entf] drücken     Rechtsklick zum abspielen)')
    label_editinfo.pack()

    frame_volume = Frame(root)
    frame_volume.pack(fill=X)
    label_volume = Label(frame_volume, text="Lautsärke:")
    volslider = Scale(frame_volume, command=volumeset,
                      from_=0, to=100, orient=HORIZONTAL, length=600)
    label_volume.pack(side=LEFT, padx=10)
    volslider.pack(side=LEFT, fill=X, expand=1)
    ########################   [ listen start/stop  / Quit]
    b1 = Button(root, text='shortcutüberwachung starten', command=lambda: startlisten(root.hotkeys))
    b2 = Button(root, text='shortcutüberwachung stoppen', command=lambda: stoplisten())
    b3 = Button(root, text='Quit', command=root.quit)
    b1.pack(side=LEFT, padx=5, pady=5)
    b2.pack(side=LEFT, padx=5, pady=5)
    b3.pack(side=LEFT, padx=5, pady=5)

    #######################   [ Vlc player - ini?! ] ########################################
    root.instanz_vlc = vlc.Instance()
    root.player = root.instanz_vlc.media_player_new()
    # set the volume slider to the current volume
    # self.volslider.SetValue(self.player.audio_get_volume() / 2)
    volslider.set(root.player.audio_get_volume())

    ##### below is a test, now use the File->Open file menu   #### kopiert :-)
    #####media = self.Instance.media_new('output.mp4')
    #####self.player.set_media(media)
    #####self.player.play() # hit the player button
    #####self.player.video_set_deinterlace(str_to_bytes('yadif'))

    root.mainloop()
