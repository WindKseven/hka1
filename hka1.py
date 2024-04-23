A = []
n = int(input("n: "))
for i in range(n):
    A.append(int(input(f"Nhap phan tu thu{i+1}: ")))

ftA = []
for pt in A:
    if pt not in ftA:
        ftA.append(pt)
# print(ftA)

def SAPXEP(X,lenf):
    i = 1
    for i in range(lenf):
        key  = X[i]
        j = i - 1
        while j >= 0 and X[j] > key:
            X[j + 1] = X[j]
            j -= 1
        X[j + 1] = key
    return X
B = SAPXEP(ftA, len(ftA))
# print(B)

"""Max_2_ele && Min_2_ele"""
print("\nPhan tu lon thu 2 la: ", B[-2])
print("Phan tu nho thu 2 la: ", B[1])    

"So nguyen to hon kem nhau 2dv"
def snt(numb):
    if numb < 2: return False
    for i in range(2, int(numb**0.5)+1):
        if numb % i == 0: return False
    return True

def sntxy2(arr):
    sntA = [x for x in arr if snt(x)]
    snthk2 = []
    for i in range(len(sntA)):
        for j in range(i+1, len(sntA)):
            if  abs(sntA[i] - sntA[j]) == 2:
                snthk2.append((sntA[i], sntA[j]))
    return snthk2
res = sntxy2(ftA)
print("\nCap so nguyen to hon kem nhau 2 don vi: ")
for tup in res:
    if len(res) == 0: print("[||]")
    else: print(tup)

"""Cap so cong"""
def csc(A):
    d = A[1] - A[0]
    for i in range(n-1):
        if A[i+1] - A[i] != d:
            return False
    return True

"""Cap so nhan"""
def csn(A):
    q = A[1] / A[0]
    for i in range(n-1):
        if A[i+1] / A[i] != q:
            return False
    return True

if csc(A):
    print("\nCap so cong")
elif csn(A):
    print("\nCap so nhan")
else:
    print("\nKhong la cap so cong hay cap so nhan")

"""UCLN"""
def ucln(a, b):
    if a == 0 or b == 0: return a + b 
    while b != 0:
        acp = a 
        a = b 
        b = acp%b 
    return a 
uc = ucln(A[0], A[1])
for i in range(2, n):
    if uc == 1: break
    else: uc = ucln(uc, A[i])
print("\nUoc chung lon nhat la: ", uc)

"""BCNN"""
def bcnn(a, b):
    return  a * b / ucln(a, b)
bc =  bcnn(A[0], A[1])
for i in range(2, n):
    bc = bcnn(bc, A[i])
print("\nBoi chung nho nhat la: ", bc)
