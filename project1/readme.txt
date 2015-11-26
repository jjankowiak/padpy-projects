BEATBOX

1. beatbox.py
Moduł główny - wczytuje, z którego folderu lub skompresowanego pliku ma być utworzony utwór oraz wczytuje jego parametry (bpm).
Odowłuje się do funkcji tworzących piosenkę, wykonuje ją i zapisuje utwór.
W przypadku folderów niespakowanych utwór zapisywany jest w folderze, w których znajdują się wszystkie pliki związane z tą piosenką. W przypadku folderów skompresowanych utwór zapisywany jest w folderze głównym (stwierdziłam, że bez sensu zapisywać w tym czasowym i później go szukać).
Dla uproszczenia zakładam, że folder skompresowany ma rozszerzenie .zip.

2. read_defs.py
Zczytuje definicje utworu, w szczególności wartość bpm.
Zakładam, że def.txt jest w formacie JSON (tak jak przykładowo było w treści zadania).

3. modul_to_create_column.py
Zawiera funkcje, które tworzą kolumnę z pliku trackXY.txt, tzn.
- wczytuje odpowiednie sample wg kolejności i je łączy tworząc macierz (składową macierzy track)
- lub tworzy nutki, jeżeli kolumna jest trzyznakowa
Uwaga - ponieważ część sampli, których użyłam jest stereo, zatem nutki, które tworzę też są w stereo (tzn. dodaję zarówno do prawego jak i lewego kanału, czyli działam na macierzach, nie ma wektorach).

4. modul_to_create_tracks.py
Funkcje, które tworzą macierz dla trackXY.txt, tzn. najpierw tworzymy sobie poszególne macierze, później je łączymy.

5. modul_to_create_song.py
Mając już macierze odpowiadające trackom, łączymy je w piosenkę w odpowiedniej kolejności.

Projekt = podstawa + czytanie z .zip + możliwość odgrywania nutek
