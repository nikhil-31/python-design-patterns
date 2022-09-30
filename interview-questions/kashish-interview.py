def sort01(a, arr_size):
    l=0 
    h= arr_size-1
    mid=0 
    while(mid<=h):
        if a[mid]==0: 
            a[l],a[mid]=a[mid],a[l]
            l=l+1 
            mid=mid+1 
        elif a[mid]==1:
            mid=mid+1 
        else:
            a[h],a[mid]=a[mid],a[h]
            h=h-1 
    return a

#######driver program
arr=[1,0,1,0,0,0,1,1]
arr_size=len(arr)
arr=sort01(arr, arr_size)
print(arr)
