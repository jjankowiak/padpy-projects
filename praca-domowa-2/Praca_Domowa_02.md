# PADPY 2015/2016 -- Praca domowa nr 2 (mała)

## Do zrobienia

* rozwiazac od 5 (na 3.0) do co najmniej 9 (na 5.0) wybranych zadan
-- im wiecej tym lepszymi bedziecie programistami Pythona przeciez

* rozwiazania (kody zrodlowe funkcji - pamietamy o docstringach)
oraz przykladowe wywolania funkcji umieszczamy w *jednym* notatniku
IPythona/Jupytera

* we wszystkich przypadkach dzialamy na tablicach lub macierzach z **numpy**

* mile widziana dyskusja (markdown), rozwiazania alternatywne itp.

* pamietamy o wklejeniu na poczatku kazdego zadania jego tresci, co bym
wiedzial, co rozwiazujecie

* rozwiązania (.ipynb) wysyłamy do 9 listopada (poniedzialek) do północy
na mój adres e-mail -- czyli czas 2 tygodnie minus epsilon


# Zadania

1. Przy uzyciu petli napisz funkcję `movingavg()`, która dla wektora `x` o $n$
elementach oraz nieparzystej liczby naturalnej $k$ wyznaczy $k$-średnią ruchomą,
$k < n$, tj. ciag $(w_1,\dots,w_{n-k+1})$, dla którego
$w_i=\sum_{j=1}^k x_{i+j-1}/k$.

2. Napisz funkcje `logiderle()`, która jako argumenty przyjmuje równoliczne
wektory całkowitoliczbowe `i`, `j` oraz wartość całkowitą $n$.
Jeśli dla każdego możliwego $l$ nie zachodzi
$1 \le i_l \le j_l \le n$ oraz $i_l > j_{l-1}$,
natychmiast zakończ działanie błędem (`raise Exception("komunikat")`).
Funkcja ma generować $n$-elementowy wektor logiczny `w`
taki, że $w_l == \mathtt{True}$ wtw $(\exists p)$
$l\in[i_p; j_p]$. Dla przykładu, jeśli $n=7$,
$\mathtt{i}=(1, 4)$, $\mathtt{j}=(1, 6)$, to w wyniku
powinniśmy otrzymać łaskawie $(\mathtt{True},\mathtt{False},\mathtt{False},
\mathtt{True},\mathtt{True},\mathtt{True},\mathtt{False})$.

3. Napisz funkcję `gendyskr()`, która jako argumenty przyjmuje:
    * wartość całkowitą dodatnią $n$,
    * $k$-elementowy wektor liczbowy `x` o unikalnych wartościach,
    * $k$-elementowy wektor prawdopodobieństw `p` -- jeśli
      wartości w `p` nie sumują się do 1, należy go przed wykonaniem
      obliczeń unormować.
      
    Naszym zadaniem jest implementacja algorytmu, który generuje 
    $n$-elementową pseudolosową próbkę z rozkładu dyskretnego zmiennej losowej $X$
    takiego, że $\Pr(X=x_i)=p_i$ $(\forall i=1,\dots,k)$. Pojedynczą wartość 
    otrzymujemy tak oto:
    
    a. Wygeneruj obserwację $u$ z rozkładu jednostajnego na $(0,1)$.
    b. Znajdź $m\in\{1,\dots,k\}$ takie, że $u\in(\sum_{j=1}^{m-1} p_{j}, \sum_{j=1}^m p_{j}]$, przy założeniu $\sum_{j=1}^0 \cdot =0$.
    c. Zwróć $x_m$ jako wynik.

4. Zaimplementuj algorytm sortowania przez scalanie danej tablicy liczb rzeczywistych.

5. Zaimplementuj algorytm sortowania szybkiego  tablicy liczb rzeczywistych
przy użyciu metody `ndarray.partition`.

6. Napisz funkcję `liniowa()`, która
jako argumenty przyjmuje: 
    * posortowany rosnąco $n$-elementowy wektor liczbowy `x`,
    * $n$-elementowy wektor liczbowy `y` (dowolny),
    * $k$-elementowy wektor liczbowy `z` o wartościach z przedziału $[x_1,x_n)$.
    
    Funkcja ta powinna zwracać $k$-elementowy wektor, którego $i$-ty element 
    jest wynikiem obliczenia wartości funkcji kawałkami liniowej (tj. łamanej)
    interpolującej liniowo punkty $(x_1,y_1),\dots,(x_n,y_n)$ w punkcie $z_i$. 
    Formalnie, jeśli $j\in\{1,\dots,n-1\}$ jest taki, że $x_j \le z_i < x_{j+1}$,
    to $i$-tą wartością wynikową będzie $y_j + (y_{j+1}-y_j)(z_i-x_j)/(x_{j+1}-x_j)$.

7. Four men want to cross a bridge. But at most 2 people may cross it at a time.
For man A it takes 10 minutes to cross, for B -- 5 minutes,
C -- 2 minutes, and D  -- 1 minute. If two people cross the bridge together,
they must walk at the pace of the slower one.
Also, it is night. Each trip requires a flashlight.  There
is only one flashlight. The men are not allowed to toss the light over
the river. How fast can you get all 4 men over the bridge?
Examine all the 108 possible solutions and determine the optimal one
(the optimal time is $<19$).

8. Implement the $k$-means clustering algorithm for a given $n\times m$ matrix:
    a. Choose initial cluster centroids, $\mu_i$, $i=1,\dots,k$ (component-wise means).
    b. Assign each point to the nearest centroid
    c. Recalculate cluster centroids by computing the means $\mu_i$ of all the points assigned to each cluster.
    d. If convergence not reached: Goto (b)

9. Macierz kwadratowa $E$ o rozmiarze $n\times n$ i elementach calkowitych
nieujemnych może reprezentować graf skierowany ważony $G=(\{0,1,\dots,n-1\}, E)$. 
Zaimplementuj algorytm Dijkstry znajdowania najkrótszej ścieżki
między dwoma danymi wierzchołkami $i,j\in\{0,1,\dots,n-1\}$ w $G$.

10. Zaimplementuj algorytm Floyd-Warshalla (najkrótsze ścieżki - grafy).

11. Zaimplementuj algorytm $A^*$ (najkrótsza ścieżka - grafy).

12. Zaimplementuj algorytm Kruskala (drzewo rozpinające).

13. Zaimplementuj algorytm Forda-Fulkersona (przepływy w grafie).

14. Znajdź jedno (albo wszystkie możliwe, co kto lubi)
wybrane rozwiązanie problemu 8 hetmanów (jak ustawić 8 "królowych" 
na szachownicy tak, by żadna z nich nie biła się - tfu! - z inną).

Inne ciekawe własne inicjatywy (grafy, programowanie dynamiczne,
optymalizacja kombinatoryczna (np. problem plecakowy),
algorytmy numeryczne (np. optymalizacja, wyszukiwanie zer,
układów równań, rozkłady macierzy),
PageRank, dowód faktu, że $P=NP$ itd.) - mile widziane.
Polecam zajrzeć na stronę https://en.wikipedia.org/wiki/List_of_algorithms
bądź do ksiązki Cormena i in. 
[*Wprowadzenie do algorytmów*](https://cebulko.com/Programming-Resources/Introduction%20to%20Algorithms%20-%20CLRS.pdf) i tamże inspiracji (przepraszam miłych Słowaków i Czechów za
to słowo) poszukać. Na pewno każdy z Was ma swoją własną listę algorytmów
"jej, zawsze chciałem to zaimplementować!" - jest to dobra okazja po temu.
