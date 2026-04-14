import time
import random
import matplotlib.pyplot as plt

# --- tablica A-ksztaltna (rosnie potem maleje, jak /\) ---
def a_ksztaltna(n):
    tablica = []
    polowa = n // 2
    for i in range(0, polowa):
        tablica.append(i)
    for i in range(polowa, -1, -1):
        if len(tablica) < n:
            tablica.append(i)
    return tablica

# --- partition z pivotem skrajnie prawym ---
def partition_prawy(A, p, r):
    x = A[r]
    i = p - 1
    j = r + 1
    while True:
        j = j - 1
        while A[j] > x:
            j = j - 1
        i = i + 1
        while A[i] < x:
            i = i + 1
        if i < j:
            A[i], A[j] = A[j], A[i]
        else:
            return j

# --- partition z pivotem srodkowym ---
def partition_srodkowy(A, p, r):
    x = A[(p + r) // 2]
    i = p - 1
    j = r + 1
    while True:
        j = j - 1
        while A[j] > x:
            j = j - 1
        i = i + 1
        while A[i] < x:
            i = i + 1
        if i < j:
            A[i], A[j] = A[j], A[i]
        else:
            return j

# --- partition z pivotem losowym ---
def partition_losowy(A, p, r):
    los = random.randint(p, r)
    x = A[los]
    i = p - 1
    j = r + 1
    while True:
        j = j - 1
        while A[j] > x:
            j = j - 1
        i = i + 1
        while A[i] < x:
            i = i + 1
        if i < j:
            A[i], A[j] = A[j], A[i]
        else:
            return j

# --- quicksort iteracyjny ---
def quicksort(A, partition_func):
    if len(A) <= 1:
        return A
    stos = []
    stos.append((0, len(A) - 1))
    while len(stos) > 0:
        p, r = stos.pop()
        if p < r:
            q = partition_func(A, p, r)
            stos.append((p, q))
            stos.append((q + 1, r))
    return A

# --- pomiary ---
rozmiary = [10000, 25000, 50000, 75000, 100000, 125000, 150000,
            175000, 200000, 250000, 300000, 350000, 400000, 450000, 500000]

nazwy_pivotow = ["pivot prawy", "pivot srodkowy", "pivot losowy"]
funkcje_partition = [partition_prawy, partition_srodkowy, partition_losowy]
wyniki = {"pivot prawy": [], "pivot srodkowy": [], "pivot losowy": []}

for n in rozmiary:
    print("Rozmiar: " + str(n))
    for k in range(len(nazwy_pivotow)):
        nazwa = nazwy_pivotow[k]
        func = funkcje_partition[k]
        tab = a_ksztaltna(n)
        start = time.time()
        quicksort(tab, func)
        koniec = time.time()
        czas = koniec - start
        wyniki[nazwa].append(czas)
        print("  " + nazwa + ": " + str(round(czas, 4)) + " s")

# --- wykres ---
plt.figure(figsize=(10, 6))
plt.plot(rozmiary, wyniki["pivot prawy"], "o-", label="pivot prawy")
plt.plot(rozmiary, wyniki["pivot srodkowy"], "s-", label="pivot srodkowy")
plt.plot(rozmiary, wyniki["pivot losowy"], "^-", label="pivot losowy")
plt.xlabel("Rozmiar tablicy (n)")
plt.ylabel("Czas [s]")
plt.title("Quicksort - porownanie pivotow (tablica A-ksztaltna)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("quicksort_pivoty_wykres.png")
plt.show()
