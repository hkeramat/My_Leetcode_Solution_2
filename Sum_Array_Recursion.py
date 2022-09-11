arr = [1,0,9,2,3]
def rec_sum(l):
    if len(l) == 0:
        return 0
    else:
        
        return l[0]+ rec_sum(l[1:])

print(rec_sum(arr))
