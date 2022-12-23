def linear(arr,n,key):
    for i in range(n):
        if arr[i]==key:
            print("Element found: in linear search")  
            return 0
    print("Element not found in linear search") 
            
def binarySer(arr,n,key):
    l=0
    u=n-1
    

    while(l<=u):
        mid=(l+u)//2
        if (arr[mid]==key):
            print("Element found in binary search: ")
            return 0
        else:
            if(arr[mid]<key):
                l=mid+1
            else:
                u=mid-1
    #    print("Element not found in binary search")

def sentinal(arr,n,key):
    last = arr[n-1]
    arr[n-1] = key
    i=0
    while arr[i] != key:
        i=i+1
    arr[n-1] = last
    if ((i<n-1) or(arr[n-1]==key) ):
        print("Element found in sentinal search")
    else:
        print("Element not found in sentinal search")


arr=[1,20,30,40,50,60,70]
key=70
n=len(arr)
binarySer(arr,n,key)
sentinal(arr,n,key)
linear(arr,n,key)
