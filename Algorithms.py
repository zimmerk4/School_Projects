def MaxHeapify(A, i):
    if i >= len(A)//2 or A[i] >= max(A[2*i], A[2*i+1]):
        pass
    else:
        if A[2*i] >= A[2*i+1]:
            A[i], A[2*i] = A[2*i], A[i]
            MaxHeapify(A, 2*i)
        else:
            A[i], A[2*i+1] = A[2*i+1], A[i]
            MaxHeapify(A, 2*i+1)
    return

def BuildMaxHeap(A):
    for i in range(len(A)//2, 0, -1):
        MaxHeapify(A, i)
    return


def merge_count(A, p, q, r):
    i = p
    j = q + 1
    B = []
    flag = 0
    count = 0
    while i <= q or j <= r:
        if i <= q and j <=r:
            if A[i] <= A[j]:
                B.append(A[i])
                i += 1
            else:
                B.append(A[j])
                j += 1
                count += q + 1 - i
        elif i == q + 1:
            B.extend(A[j:r+1])
            j = r+1
        else:
            B.extend(A[i:q+1])
            i = q + 1
        flag += 1
    A[p:r] = B[:r-p+1]
    return count


def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        count = merge_count(A, p, q, r)
    else:
        return
    return count


A = [7, 12, 2, 3, 10, 4, 20]
B = [4, 2, 5, 3, 1]

print(A)
print()
BuildMaxHeap(A)
print(A)
print()
print(B)
print(merge_sort(B, 1, len(B)))
print(B)