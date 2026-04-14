import time
import random
import math
import matplotlib.pyplot as plt

# --- sortowanie Shella ---
def shell_sort(A):
    n = len(A)
    if n <= 1:
        return A
    t = int(math.log2(n))
    for s in range(t - 1, -1, -1):
        h = 2 ** s
        for j in range(h, n):
            key = A[j]
            i = j - h
            while i >= 0 and A[i] > key:
                A[i + h] = A[i]
                i = i - h
            A[i + h] = key
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
rozmiary = [5000, 10000, 15000, 20000, 30000, 40000, 50000,
            60000, 70000, 80000, 90000, 100000, 120000, 150000, 200000]

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
        shell_sort(tab)
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
plt.title("Shell Sort")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("shell_sort_wykres.png")
plt.show()
