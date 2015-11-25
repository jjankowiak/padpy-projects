beatbox.py
Moduł główny - zczytuje, z które folderu, pliku ma być utworzony utwór oraz zczytuje parametry utworu (bpm), odowłuje się do funkcji tworzące piosenke, wykonuje ją i zapisuje utwór.

W przypadku folderów niespakowanych utwór zapisywany jest w folderze dot. tej piosenki. W przypadk folderów skompresowanych utwór zapisywany jest w folderze głównym (stwierdziłam, że bez sensu zapisywać w tym czasowym i później go szukać).

Dla uproszczenia zakładam, że folder skompresowany ma rozszerzenie .zip.


read_defs.py
Zczytuje definicje utworu, w szczególności wartość bpm.
Zakładam, że def.txt jest w formacie JSON (tak jak przykładowo było w treści zadania)


modul_to_create_colum.py
Zawiera funkcje, które tworzą kolumnę z pliku trackXY.txt, tzn.
- wczytuje odpowiednie sample wg kolejności i je łączy tworząc macierz (składową macierzy track)
- lub tworzy nutki, jeżeli kolumna jest trzyznakowa


modul_to_create_tracks.py
Funkcje, które tworzą macierz dla trackXY.txt, tzn. najpierw tworzymy sobie poszególne kolumny, później je łączymy.


modul_to_create_song.py
Mając już macierze odpowiadające trackom, łączymy je w piosenke (w odpowiedniej kolejności)
