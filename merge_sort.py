import time
import random
import sys
import matplotlib.pyplot as plt

sys.setrecursionlimit(100000)

# --- sortowanie przez scalanie ---
def merge_sort(A, l, r, B):
    m = (l + r) // 2
    if (m - l) > 0:
        merge_sort(A, l, m, B)
    if (r - m) > 1:
        merge_sort(A, m + 1, r, B)
    i = l
    j = m + 1
    for k in range(l, r + 1):
        if (i <= m and j > r) or (i <= m and j <= r and A[i] <= A[j]):
            B[k] = A[i]
            i = i + 1
        else:
            B[k] = A[j]
            j = j + 1
    for k in range(l, r + 1):
        A[k] = B[k]

def merge_sort_main(A):
    if len(A) <= 1:
        return A
    B = [0] * len(A)
    merge_sort(A, 0, len(A) - 1, B)
    return A

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
        merge_sort_main(tab)
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
plt.title("Merge Sort")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("merge_sort_wykres.png")
plt.show()
