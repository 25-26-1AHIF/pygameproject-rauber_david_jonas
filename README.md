Räuber Simulator
Von Jonas Stocker und David Fußenegger
1AHIF
POS
2026

 
Inhaltsverzeichnis
1.	Projekttagebuch	3
2.	Lastenheft	4
2.1	Projekt-Idee:	4
2.2	Must-To-Have:	4
2.3	Nice-To-Have:	4
3.	Pflichtenheft	5
3.1 Softwarevoraussetzungen	5
3.2 Architektur	5
3.3 Beschreibung der Umsetzung	5
3.4 Mögliche Probleme und ihre Lösung	5
4. Bedienungsanleitung	7
5. Quellenverzeichnis	8



 
1.	Projekttagebuch

12.05	David, Jonas	Start
18.05	Jonas	Main file erstellt, game_variables erstellt, play_screen erstellt
20.05	David	Pause Screen erstellt, Player angefangen
21.05	Jonas	Animation erstellt, Ordner aufgeräumt
22.05	David	Steuerung Screen erstellt, Game Loop verbessert
22.05	Jonas	Code fix
26.05	Jonas	Ersten Room erstellt
26.05	David	Player Bewegung im Raum
28.05	David	Erstes Rätsel erstellt
29.05	David	Rätsel verbessert, Münzen erstellt
31.05	Jonas	Straße erstellt, Animation hinzugefügt
01.06	David	Uhr erstellt, zweites Rätsel erstellt
01.06	Jonas	Türen-Hitboxen erstellt, Player Laufanimation
04.06	Jonas	Gang hinzugefügt mit neunen Räumen
04.06	David	Rätsel 3, 4 hinzugefügt
07.06	David	Code fix
07.06	Jonas	Gang verbessert
11.06	Jonas	Wohnwagen verbessert
12.06	David	Rätsel 3 verbessert, Rätsel 4 überarbeitet, Gang-Hitbox
14.06	David	Wohnwagen gefixt, Rätsel 5
15.06	David	Großer Fix, Speichern
16.06	David	Fix
18.06	David	Shop
20.06	Jonas	Letzten Räume hinzugefügt
21.06	David	Problem fix
21.06	Jonas	Problem fix


 
2.	Lastenheft
2.1	Projekt-Idee:
Ein 2D Spiel, indem der Spieler die Rolle eines Räubers übernimmt und innerhalb begrenzter Zeit Häuser ausrauben muss. Der Spieler kann so Geld verdienen und seine besten Scores werden gespeichert.
2.2	Must-To-Have:
5 Haus in einer Reihe (Straße), verschiedene Aufgaben, um Haus Schlößer zu knacken, die besten 3 Scores (Bestzeiten) speichern und ausgeben, Geld, das man durch geklaute Sachen verdienen kann, Man hat eine Nacht zeit
2.3	Nice-To-Have:
Shop mit Skins, Hausbewohner die geweckt werden können



3.	Pflichtenheft
3.1 Softwarevoraussetzungen
Programmiersprache: Python Version 3.13.
Verwendete Bibliotheken: 
•	Pygame
•	json 

3.2 Architektur
•	main.py: Enthält die Hauptschleife und steuert den Wechsel zwischen den Screens
•	game_variables.py: Verwaltet alle globalen Variablen (Coins, Positionen, Zeiten, geladene Fonts, Skins) zentral in der Klasse GameVariables.
•	save_game.py: Mit JSON für das Schreiben und Speichern des Spiels. 
•	Ordner objects/Screens/: Beinhaltet alle Screens

3.3 Beschreibung der Umsetzung
Zustandssteuerung (Screen-Management): Der Wechsel zwischen Menü, Spiel, Pause und Endscreen wird über Rückgabewerte in Funktionen geregelt. Wenn ein Screen beendet wird, gibt er den nächsten Zustand an die main.py zurück.
Speichersystem: Daten werden in einem strukturierten JSON-Format abgelegt. Beim Highscore werden Dictionaries (mit Zeit und Coins) sortiert und auf die Top 3 begrenzt. Damit Pfade flexibel bleiben, wird mit relativen Pfaden gearbeitet.

3.4 Mögliche Probleme und ihre Lösung
Problem: Pfadkonflikte beim Ausführen aus Unterordnern. save_game.py suchte die JSON-Datei im falschen Verzeichnis.

Lösung: Umstellung aller Dateioperationen auf den relativen Pfad ../savegame.json, um immer das Hauptprojektverzeichnis anzusprechen.

Problem: Das Spiel setzte sich beim Schließen selbst zurück.

Lösung: Das fälschlicherweise am Ende der main.py platzierte reset_game() wurde entfernt, damit der Spielstand beim Beenden erhalten bleibt.
 

4. Bedienungsanleitung
•	Starten des Spiels: Führe die Datei main.py in deiner Python-Umgebung aus.
•	Hauptmenü:
•	Klicke auf Starten, um eine völlig neue Runde zu beginnen

•	Klicke auf Spiel laden, um am exakten Speicherpunkt im jeweiligen Raum mit deinen Coins fortzufahren.

•	Klicke auf Scores, um die Top 3 der Bestzeiten mitsamt gesammelten Münzen zu sehen.

•	Klicke auf Shop, um Skins freizuschalten und zu wechseln.

•	Steuerung im Spiel:
•	W, A, S, D/ Pfeiltasten: Spieler nach links, rechts, oben und unten bewegen.

•	[SPACE]: Spiel pausieren und Pause-Menü öffnen um zu Speichern

•	[ESC]: In Menüs zurück zum Hauptmenü springen.
 

5. Quellenverzeichnis
Bilde: Alles selbst gezeichnet mit Piskel.com




