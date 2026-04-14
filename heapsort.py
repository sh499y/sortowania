import time
import random
import matplotlib.pyplot as plt

# --- sortowanie przez kopcowanie ---
def heapify(A, i, heapsize):
    l = 2 * i + 1
    r = 2 * i + 2
    if l < heapsize and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < heapsize and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        heapify(A, largest, heapsize)

def build_heap(A):
    heapsize = len(A)
    for i in range(len(A) // 2 - 1, -1, -1):
        heapify(A, i, heapsize)

def heapsort(A):
    build_heap(A)
    heapsize = len(A)
    for i in range(len(A) - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapsize = heapsize - 1
        heapify(A, 0, heapsize)
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
        heapsort(tab)
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
plt.title("Heapsort")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("heapsort_wykres.png")
plt.show()
