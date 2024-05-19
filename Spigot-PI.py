# gth

N = 500
LEN = 10 * N // 3

if __name__ == '__main__':
    a = [0]
    
    # Start with 2s
    a.extend([2] * LEN)
    
    # First predigit is a 0
    nines = 0
    predigit = 0
    
    for j in range(1, N + 1):
        q = 0
        
        # Work backwards
        for i in range(LEN, 0, -1):
            x = 10 * a[i] + q * i
            a[i] = x % (2 * i - 1)
            q = x // (2 * i - 1)
        
        a[1] = q % 10
        q = q // 10
        
        if q == 9:
            nines += 1
        else:
            if q == 10:
                print(predigit + 1, end = '')
                
                # zeros
                for k in range(1, nines + 1):
                    print(0, end = '')
                
                nines = 0
                predigit = 0
            else:
                print(predigit, end = '')
                
                predigit = q
                
                if nines != 0:
                    for k in range(1, nines + 1):
                        print(9, end = '')
                    
                    nines = 0
    
    print(predigit, end = '')