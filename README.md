# Python-Soundboard
Soundboard zur Bedienung per Tastatur (shortcut und einfache Tasten)

Das Projekt wurde mit dem Programm Kate erstellt.
Die Idee und initiale Arbeit (Plugins finden, ersten Code zusammenstellen) stammt von TuxPlayDe (www.twitch.tv/tuxplayde)
Das Programm muss under linux mit sudo laufen um zugriff auf die Shortcuts/Tasteneingaben zu bekommen (Anforderung der keyboard Bibliothek).
Zum abspielen der Audiodateien wird VLC + Python Plugin benötigt. Das UI ist in dieser Version derzeit mit tkinter erstellt.

Was noch anzupassen ist:
- Alles etwas schöner/professioneller machen :-)
- Aktuell werden noch ausgaben in der konsole gemacht, die nicht mehr gebraucht werden.
- Wenn die Dateipfade zu lang werden kann man nurnoch den anfang lesen : Scrollbalken wären noch gut
- Es wird noch nicht berücksichtigt, dass die configdatei nicht da sein könnte
- Die shortcuts die ins eingabefeld eingegeben werden können (direkt) werden noch nicht gegengecheckt.
- Evtl. könnte es passieren/gehen, dass man den fokus in den Listen verändern kann während der Dialog zum Shortcut aufnehmen offen ist.
- sicher noch einiges mehr.
