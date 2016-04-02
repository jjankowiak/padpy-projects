Opis gry
--------
Celem gry jest zaznaczenie wszystkich pól, w których znadują się bomby. Gra została napisane w języku python z wykorzystaniem biblioteki PyQt.


Instrukcja
----------

**Uruchomienie gry:**

    python Minesweeper.py

Należy upewnić się, że w jednym folderze znajdują się wszystkie pliki związane z grą, tzn. trzy skrypty `.py` oraz folder z obrazkami nazwany `images`.

**Zasady gry:**
Celem gry jest oznaczenie wszystkich sektorów, w których znajdują się bomby.
 * Odkrycie miny kończy grę.
 * Odkrycie pustego pola oznacza kontynuowanie rozgrywki.
 * Odkrycie liczby informuje, ile min ukryto wśród ośmiu sąsiadujących z nią pól - na tej podstawie trzeba wydedukować, które pola dookoła można bezpiecznie kliknąć.

