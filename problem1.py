def max_cyclic_substring_sum(S):
    n = len(S)
    S = S + S  # make cyclic
    
    char_set = set()
    left = 0
    current_sum = 0
    max_sum = 0
    
    for right in range(len(S)):
        val = ord(S[right]) - ord('a') + 1
        
        # remove duplicates
        while S[right] in char_set or (right - left + 1) > n:
            char_set.remove(S[left])
            current_sum -= (ord(S[left]) - ord('a') + 1)
            left += 1
        
        char_set.add(S[right])
        current_sum += val
        
        max_sum = max(max_sum, current_sum)
    
    return max_sum


# Input
S = input().strip()
print(max_cyclic_substring_sum(S))
