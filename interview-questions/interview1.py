def test():
    lst = [0,1,1,1,0,0,1,0,1]

    a = 0
    b = len(lst)-1
    while b>=a:
        if lst[a]<lst[b]:
            a+=1
            b-=1
        elif lst[a]>lst[b]:
            lst[a],lst[b]=lst[b],lst[a]
            a+=1
            b-=1
        else:
            b-=1

    return lst

print(test())