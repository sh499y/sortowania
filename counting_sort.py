import time
import random
import matplotlib.pyplot as plt

# --- sortowanie przez zliczanie ---
def counting_sort(A):
    if len(A) == 0:
        return A
    # znajdz maksimum
    k = 0
    for i in range(len(A)):
        if A[i] > k:
            k = A[i]
    # tablica zliczajaca
    C = [0] * (k + 1)
    B = [0] * len(A)
    # zlicz wystapienia
    for i in range(len(A)):
        C[A[i]] = C[A[i]] + 1
    # sumy prefiksowe
    for j in range(1, k + 1):
        C[j] = C[j] + C[j - 1]
    # budowanie tablicy wynikowej
    for i in range(len(A) - 1, -1, -1):
        B[C[A[i]] - 1] = A[i]
        C[A[i]] = C[A[i]] - 1
    return B

# --- generowanie tablic ---
def losowa(n):
    tablica = []
    for i in range(n):
        tablica.append(random.randint(0, n))
    return tablica

def rosnaca(n):
    tablica = []
    for i in range(n):
        tablica.append(i)
    return tablica

def malejaca(n):
    tablica = []
    for i in range(n - 1, -1, -1):
        tablica.append(i)
    return tablica

def stala(n):
    tablica = []
    for i in range(n):
        tablica.append(42)
    return tablica

def v_ksztaltna(n):
    tablica = []
    polowa = n // 2
    for i in range(polowa, 0, -1):
        tablica.append(i)
    for i in range(0, n - polowa):
        tablica.append(i)
    return tablica

# --- pomiary ---
rozmiary = [10000, 25000, 50000, 75000, 100000, 125000, 150000,
            175000, 200000, 250000, 300000, 350000, 400000, 450000, 500000]

nazwy = ["losowa", "rosnaca", "malejaca", "stala", "v-ksztaltna"]
generatory = [losowa, rosnaca, malejaca, stala, v_ksztaltna]
wyniki = {"losowa": [], "rosnaca": [], "malejaca": [], "stala": [], "v-ksztaltna": []}

for n in rozmiary:
    print("Rozmiar: " + str(n))
    for k in range(len(nazwy)):
        nazwa = nazwy[k]
        generator = generatory[k]
        tab = generator(n)
        start = time.time()
        wynik = counting_sort(tab)
        koniec = time.time()
        czas = koniec - start
        wyniki[nazwa].append(czas)
        print("  " + nazwa + ": " + str(round(czas, 4)) + " s")

# --- wykres ---
plt.figure(figsize=(10, 6))
plt.plot(rozmiary, wyniki["losowa"], "o-", label="losowa")
plt.plot(rozmiary, wyniki["rosnaca"], "s-", label="rosnaca")
plt.plot(rozmiary, wyniki["malejaca"], "^-", label="malejaca")
plt.plot(rozmiary, wyniki["stala"], "d-", label="stala")
plt.plot(rozmiary, wyniki["v-ksztaltna"], "x-", label="v-ksztaltna")
plt.xlabel("Rozmiar tablicy (n)")
plt.ylabel("Czas [s]")
plt.title("Counting Sort")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("counting_sort_wykres.png")
plt.show()
