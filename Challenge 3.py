def solution3(N):
    result = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_len = len(alphabet)
    
    # Number of occurrences for each character
    occurrences = N // alphabet_len
    
    # Remaining characters to reach N
    remaining = N % alphabet_len
    
    for char in alphabet:
        if occurrences > 0:
            result.append(char * occurrences)
        else:
            break
    
    if remaining > 0:
        result.append(alphabet[:remaining] * occurrences)
    
    return ''.join(result)
