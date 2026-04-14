import time
import random
import matplotlib.pyplot as plt

# --- sortowanie szybkie ---
def partition(A, p, r):
    x = A[(p + r) // 2]
    i = p - 1
    j = r + 1
    while True:
        # repeat j = j - 1 until A[j] <= x
        j = j - 1
        while A[j] > x:
            j = j - 1
        # repeat i = i + 1 until A[i] >= x
        i = i + 1
        while A[i] < x:
            i = i + 1
        if i < j:
            A[i], A[j] = A[j], A[i]
        else:
            return j

# wersja iteracyjna zeby nie bylo problemu z rekursja
def quicksort(A):
    if len(A) <= 1:
        return A
    stos = []
    stos.append((0, len(A) - 1))
    while len(stos) > 0:
        p, r = stos.pop()
        if p < r:
            q = partition(A, p, r)
            stos.append((p, q))
            stos.append((q + 1, r))
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
        quicksort(tab)
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
plt.title("Quicksort")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("quicksort_wykres.png")
plt.show()
