# PADPY 2015/2016 -- Praca domowa nr 1 (mała)

## Do zrobienia

* rozwiazac od 5 (na 3.0) do co najmniej 9 (na 5.0) wybranych zadan
-- im wiecej tym lepszymi bedziecie programistami Pythona przeciez

* rozwiazania (kody zrodlowe funkcji - pamietamy o docstringach)
oraz przykladowe wywolania funkcji umieszczamy w *jednym* notatniku
IPythona/Jupytera

* mile widziana dyskusja (markdown), rozwiazania alternatywne itp.

* pamietamy o wklejeniu na poczatku kazdego zadania jego tresci, co bym
wiedzial, co rozwiazujecie

* dla osob żądnych przygód szczególnie polecam zadania:
szklana pułapka, odejmowanie 2 bigintów, moda, sortowanie kubełkowe,
sortowanie szybkie, scalanie 2 posortowanych ciągów

* pozostałe osoby starają się nie wybierać tylko zadań najprostszych.
ocywiście te zadania, które rozwiązaliśmy na laboratoriach są wykluczone
z obszaru naszych zainteresowań już

* rozwiązania (.ipynb) wysyłamy do 26 października (poniedzialek) do północy
na mój adres e-mail -- czyli czas 2 tygodnie minus epsilon


# Zadania

1. Napisz funkcję `max()`, która zwraca maksimum z podanych trzech argumentów.

2. Napisz funkcję `med()`, która znajduje medianę (wartość środkową)
trzech liczb rzeczywistych, np. `med(4,2,7)==4` oraz
`med(1,2,3)=2`.

3. Napisz funkcję `med()`, która znajduje medianę
czterech liczb rzeczywistych, np. `med(4,2,7,3)=3.5`.

4. Napisz funkcję `prostokat()`, która dla danych 3 dodatnich liczb
rzeczywistych a, b, c sprawdzi, czy może istnieć trójkąt prostokątny
o bokach podanych długości.

5. Napisz funkcję, która dla danego `n` oblicza
oblicza $\max\{k\in\mathbb{N}_0 : 2^k\le n\}$.

6. Napisz funkcję, która dla danych liczb rzeczywistych a, b, c
wyznaczy rozwiązanie równania $ax^2+bx+c=0$ (względem $x$).
Zwróć krotkę o długości od 0 do 2.

7. Napisz funkcję, która zwraca przybliżenie wartości liczby $\pi$
za pomocą wzoru:
$\pi \simeq 4\left(1-\frac{1}{3}+\frac{1}{5}-\frac{1}{7}+\dots\right)$
na podstawie $n$ (argument funkcji) pierwszych elementów tego szeregu
liczbowego.

8. Wyrazy ciągu Fibonacciego $(F_n)_{n=0,1,\dots}$ określone są wzorem
$F_0=F_1=1$ oraz $F_n=F_{n-1}+F_{n-2}$ dla $n\ge 2$. Napisz funkcję,
która dla danego $k$ zwróci takie $i$, że $F_i$ jest najmniejszym elementem,
który ma dokładnie $k$ cyfr w~zapisie dziesiętnym. Na przykład dla $k=3$
jest to $12$, bo $F_{12}=144$, a $F_{11}=89$. Uwaga: funkcja ma działać
także np. dla $k=1000$.

9. Napisz funkcję, która sprawdza, czy dana liczba naturalna
jest liczbą pierwszą (\texttt{true}), czy też liczbą złożoną
(\texttt{false}).

10. Napisz funkcję, która wyznaczy liczbę liczb pierwszych w zadanym zbiorze
$\{a,a+1,\dots,b\}$, gdzie $a<b$ --- argumenty funkcji.

11. Napisz funkcję która przyjmuje 3 argumenty a,b,c. Znajdź ich permutację
taką, że a' <= b' <= c' i zwróć je jako krotkę (a',b',c').

12. (*Szklana pułapka*) Masz do dyspozycji pojemniki na wodę o objętości $x$
i $y$ litrów oraz dowolną ilość wody w~basenie. Czy przy ich pomocy (pojemniki
wypełnione do pełna) można wybrać $z$ litrów wody? Napisz pseudokod
algorytmu, który to sprawdza i dokonaj obliczeń dla
a) $x=13, y=31, z=1111$, b) $x=12, y=21, z=111$.


13. Dane są liczby rzeczywiste $x_1,\dots,x_4,y_1,\dots,y_4\in\mathbb{R}$
(dwie czteroelementowe listy). Napisz funkcję, która sprawdzi, korzystając
z jak najmniejszej liczby warunków logicznych, czy prostokąty
$[x_1,x_2]\times[y_1,y_2]$ oraz~$[x_3,x_4]\times[y_3,y_4]$ mają część
wspólną (tj. przecinają się).

14. Napisz funkcję, która za pomocą tylko jednej pętli `for` znajduje
i zwraca jako krotkę element najmniejszy i element największy
danej listy.

15. Napisz funkcję, która za pomocą tylko jednej pętli `for` wyznaczy i zwróci
trzeci największy element listy, np. dla ciągu (3.0,5.0,2.0,4.0,1.0,6.0)
będzie to 4.0.

16. Dana jest lista `t` składająca się z liczb całkowitych od 0 do 19.
Napisz funkcję, która wyznaczy jej dominantę (modę), czyli najczęściej
pojawiającą się wartość. Wskazówka: skorzystaj z~pomocniczej,
20-elementowej listy, przy użyciu której zliczysz, ile razy w `t` występuje
każda możliwa wartość.

17. Uogólnij funkcję z poprzedniego zadania tak, by działała nie tylko dla list
o elementach ze~zbioru $\{0,1,\dots,19\}$, ale dla dowolnego $\{a,a+1,\dots,b\}$.

18. Dana jest n-elementowa lista `t` wypełniona liczbami naturalnymi ze zbioru
$\{1, 2, \dots, k\}$ dla pewnego `k`. Napisz funkcję, która za pomocą
tzw. sortowania kubełkowego uporządkuje w kolejności niemalejącej elementy
z `t`. W algorytmie sortowania kubełkowego korzystamy z `k`-elementowej tablicy
pomocniczej, która służy do zliczania liczby wystąpień każdej z `k` wartości
elementów z `t`. Na początku tablica pomocnicza jest wypełniona zerami.
Należy rozpatrywać kolejno każdy element tablicy `t`, za każdym razem
zwiększając o 1 wartość odpowiedniej komórki tablicy pomocniczej.

19. Dane są dwie liczby całkowite w systemie dziesiętnym: `n`-cyfrowa liczba
reprezentowana przy użyciu listy `a` oraz m-cyfrowa reprezentowana
przy użyciu listy `b`. Każda cyfra jest reprezentowana jako osobny element
odpowiedniej listy. Cyfry zapisane są w kolejności od najmłodszej do
najstarszej, tzn. element o indeksie 0 oznacza jedności, 1 -- dziesiątki itd.,
przy czym najstarsza cyfra jest różna od 0. Napisz funkcję, która utworzy nową
listę reprezentującą wynik odejmowania liczb `a` i `b`.

20. Niech dane będą wielomiany $w(x)$ i $v(x)$ stopnia, odpowiednio, $n$ i $m$.
Napisz funkcję, która wyznaczy wartości współczynników wielomianu $u(x)$
stopnia $n+m$, będącego iloczynem wielomianów $w$ i $v$.
Współczynniki przy kolejnych wyrazach wielomianu to kolejne elementy list.

21. Dane są dwie uporządkowane niemalejąco listy liczb całkowitych `x` i `y`
rozmiarów, odpowiednio, `n` i `m`. Napisz funkcję, który zwróci uporządkowaną
niemalejąco listę rozmiaru `n+m` powstałą ze scalenia `x` i `y`.
Algorytm powinien mieć liniową (rzędu `n+m`) pesymistyczną złożoność czasową.
Np. dla `x=[1,4,5]` i `y=[0,2,3]` powinniśmy otrzymać `[0,1,2,3,4,5]`.

22. Dana jest n-elementowa, już posortowana lista liczb całkowitych
oraz liczba całkowita `x`. Napisz funkcję, która za pomocą wyszukiwania
binarnego (połówkowego) sprawdzi, czy wartość `x` jest elementem listy
i jeśli tak jest w istocie, to poda pod którym indeksem listy się znajduje bądź
zwróci -1 w przeciwnym przypadku.

23. Zaimplementuj algorytm sortowania przez wybór.

24. zaimplementuj algorytm sortowania przez wstawianie.

25. Zaimplementuj algorytm sortowania szybkiego.

26. Napisz funkcję, która dla danej listy zwróci nowa listę z pominiętymi
wszystkimi wartościami 0, `None` i napisami pustymi.

27. Napisz funkcję, która dla danej listy zwraca jej wersję z elementami
w odwróconej kolejności.

28. Napisz funkcję, która sprawdza, czy dana lista jest palindromem.
