PADPY 2015/2016 - Praca domowa nr 3 (duża)
==========================================

Do zdobycia tym razem: 10 p.

Termin oddania pracy: 30.11.2015

Rozwiązania umieszczamy we własnym, nowym repozytorium na githubie
lub gitlabie (może być prywatne, ale trzeba mi dać do niego dostęp
co najmniej do odczytu w-ów-czas). Link do strony domowej repozytorium
przesyłacie mi mailem (i nic więcej nie trzeba). Na marginesie - na githubie
można dostać bezpłatnie free individual micro plan (5 prywatnych repozytoriów)
(https://education.github.com/discount_requests/new), ale dość długo się
czeka na niego.


Struktura plików w repozytorium
-------------------------------

```
/
   beatbox.py     # główna "aplikacja"

   readme.txt     # dodatkowe informacje o programie (m.in. opis plików, rozszerzeń itp.)

   innymodul1.py  # dodatkowy moduł, nazwa dowolna
   ...
   innymodulN.py  # dodatkowy moduł, nazwa dowolna (musza byc co najmniej 2 dodatkowo)

   utwor/         # katalog, nazwa dowolna, definicja utworu
       sample01.wav # plik .wav, nazwa sampleUV.wav, gdzie UV to 2 cyfry
       ...
       sampleXY.wav # jw.

       track01.txt  # definicja ścieżki 01, nazwa trackUV, gdzie UV to 2 cyfry
       ...
       trackAB.txt  # jw.

       defs.txt     # konfiguracja (m.in. bpm, zobacz niżej)

       song.txt     # określa kolejność odgrywanych ścieżek (zob. niżej)

    dance_and_bounce/

       jw. definicja utworu

    trash_metal/

       jw. definicja utworu

    itd.
```

Program główny
--------------

Możliwość uruchomienia przy użyciu:

```
./beatbox.py utworX/
```

gdzie `utworX` to nazwa katalogu w katalogu bieżącym.
Wynikiem działania programu jest plik `utworX.wav` (nazwa taka jak
katalogu wejściowego.

Cała aplikacja powinna się składać z co najmniej dwóch dodatkowych modułów
-- podział dowolny (np. wczytywanie definicji utworu i zapis pliku wav oddzielnie).


Konfiguracja utworu
-------------------

Konfiguracja każdego utworu znajduje się w pliku `defs.txt`.
Definicja podobna do składni tworzącej obiekt typu składnik.
W wersji podstawowej określamy tylko jedno pole: `bpm` (beats per minute).

```python
{
    "bpm": 120
}
```

Na wyższą ocenę potrzebne będą pola dodatkowe, patrz niżej.


Kolejność odgrywanych ścieżek
-----------------------------

Plik `song.txt` postaci na przykład:

```
01
01
01
02
01
01
01
03
```

Powyżej odwołania do trzech plików `trackAB.txt` (01, 02 i 03) - w takiej
kolejności będą one odgrywane. Plik o dowolnej liczbie wierszy.
Jak widać utwór zatem składa się ze ścieżek.



Definicja ścieżki
-----------------

Każda ścieżka złożona jest z *sampli* odgrywanych kolejno, brane
jest pod uwagę tempo (bpm). W wersji podstawowej możliwe jest odgrywanie
minimum co najmniej 4 sampli równocześnie.

```
01 02 03 04
-- -- 03 --
-- 02 03 --
-- -- 03 --
01 02 03 04
-- -- 03 --
-- 02 03 --
-- -- 03 --
01 02 03 04
-- -- 03 --
-- 02 03 04
-- -- 03 --
01 02 03 04
-- -- 03 04
-- 02 03 04
-- -- 03 04
```

Plik o dowolnej liczbie wierszy, ale podzielnej przez 4.
`--` oznacza pauzę, `XY` oznacza identyfikator pliku `.wav`, który ma
być odegrany. Każdy dwukolumnowy ciąg znaków oddzielony jest od siebie
niepustym ciągiem białych znaków, np. spacji.


Utwory
------

Należy w katalogu projektu umieścić co najmniej trzy przykładowe utwory
(demo). Mile widziane polskie piosenki zabawowe: *Szła dzieweczka do laseczka*,
*Mam chusteczkę haftowaną*, *W murowanej piwnicy* itp.


Ocena
-----

Powyższe wystarcza na ocenę 60%.
Dodatkowe punkty można dostać za:

1. Możliwość "odgrywania" spakowanych plików .zip (cały katalog z
utworem może być skompresowany). Pliki rozpakujemy do katalogu
na dane tymczasowe i stamtąd je sczytujemy. (na 70%)

2. Możliwość "grania nutek". W wersji uproszczonej hardkodujemy
jeden instrument (fale sinusoidalne, trójkątne itp.).
Wówczas zamiast kolumny dwucyfrowej w definicji ścieżki można podać
kolumnę (gdziekolwiek) trzyznakową postaci np.:

    ```
    A-4
    A#4
    B-4
    ---
    C-5
    C#5
    D-5
    ---
    ```

    Umawiamy się, że `A-4` odpowiada 440 Hz.  (na 80%)

3. Możliwość definiowania nowych instrumentów -- pliki typu
sampleXY.txt (można też wciąż dodawać sampleAB.wav).
Sposób definicji dowolny (bierzemy pod uwage kształt fali,
attack, decay, sustain, itp.)
Wówczas zamiast kolumny dwucyfrowej w definicji ścieżki można podać
kolumnę (gdziekolwiek) sześcioznakową postaci np.:

    ```
    01:A-4
    01:A#4
    01:B-4
    ---
    02:C-5
    02:C#5
    02:D-5
    ---
    ```

    czyli `id_instrumentu:nutka` (na 100%).

4. Mile widziane wszelkie inne rozszerzenia (plik `defs.txt` oraz pakiety Pythona
typu `pyaudio`, `librosa`, `essentia` itd. pozostawiają duże pole do popisu).
+ wszystkie pomysly wlasne
