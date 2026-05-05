def min_operations(N, A, K):
    mod = A[0] % K
    
    # Check feasibility
    for x in A:
        if x % K != mod:
            return -1
    
    # Normalize
    B = [(x - mod) // K for x in A]
    B.sort()
    
    median = B[N // 2]
    
    # Count operations
    ops = sum(abs(x - median) for x in B)
    
    return ops


# Input
N = int(input())
A = list(map(int, input().split()))
K = int(input())

print(min_operations(N, A, K))
