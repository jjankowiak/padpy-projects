PADPY 2015/2016 - Praca domowa nr 6 (mała)
==========================================

Do zdobycia: 5 p.

Termin oddania pracy: 26.01.2015

Zadanie: zbadać zachowanie się różnych algorytmów analizy skupień
(clustering) na zbiorach benchmarkowych.

Dane benchmarkowe: wszystkie zbiory danych (bodaj 29) ze strony
http://gagolewski.rexamine.com/resources/data/clustering/.

Zwróćmy uwagę, że z każdym zbiorem benchmarkowym skojarzony jest zbiór
"oczekiwanych" ("prawdziwych") etykiet. Liczba unikalnych etykiet
daje nam liczbę skupień *k$, na które dany zbiór należy podzielić.

Każdy wygenerowany automatycznie podział na *k* podzbiorów
należy odnieść do "prawdziwego". Jako miarę podobieństwa dwóch podziałów
stosujemy index FM (Fowlkesa-Mallowsa), który jest zdefiniowany w artykule
E.B. Fowlkes,  C.L. Mallows, A Method for Comparing Two Hierarchical Clusterings,
Journal of the American Statistical Association 78(383), 1983, s. 553,
doi:10.2307/2288117 (zob. http://dx.doi.org). Artykuł można pobrać z sieci PW.

Algorytmy: wszystkie istotne z pakietu scikit-learn
(http://scikit-learn.org/stable/modules/clustering.html#clustering),
w tym: k-means, Birch, DBSCAN, hierarchczne
(single linkage, Ward linkage, complete linkage, average linkage) itd.

Uwaga: niektóre zbiory danych nie są punktami w przestrzeni R^k
(mamy np. napisy, które wymagają użycia odległości Hamminga
lub Levenshteina). Część algorytmów nie będzie na nich działać
(stosunkowo najbardziej uniwersalne są metody hierarchiczne).

Rozwiązanie oddajemy w formie 1 pliku .zip zawierającego:
a) pomocnicze skrypty .py (pure Python) lub .pyx (Cython)
b) jeden plik .csv zawierający policzone indeksy FM dla każdej pary
(algorytm, zbiór danych)
c) notebooka Jupyter/IPython przedstawiającego analizę wyników
zawartych w pliku .csv. Interesuje mnie m.in. tabelka zawierająca indeksy
FM dla każdej pary (algorytm, zbiór danych) oraz różne statystyki opisowe
(zagregowane dane) i wykresy.

Podobną rzecz robiliśmy ostatnio analizując nasz nowy algorytm analizy skupień
(który wygrywa ze wszystkimi klasycznymi metodami hierarchicznymi).

