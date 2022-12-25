def accept_data(arr):
    n=int(input("Enter how many records do you want to enter? :"))
    for i in range(n):
        data=int(input("Enter Rollno: "))
        arr.append(data)
    print("Student Info Accepted Successfully: ")
        
    print("Student Rollno:",arr)
    return n
    
def linear_search(arr,l,key):
    for i in range(l):
        if(arr[i]==key):
            print("(Linear Search) Element",arr[i],"found at:",i+1)
            return i
    print("(Linear Search)Element not found")
    return -1
    
def sentinal_search(arr,l,key):
    last=arr[l-1]
    arr[l-1]=key
    i=0
    while arr[i]!=key:
        i=i+1
    arr[l-1]=last
    if(i<l-1 or arr[l-1]==key):
        print("(Sentinal Search)Element",arr[i],"found at:",i+1)
        return 1
    print("(Sentinal Search)Element not found:")
    return -1
    


# arr=[10,20,10,30,45,60,70,80,12]
def main():
    arr=[]
    while True:
        print("\t1. Accept Student info & Display")
        print("\t2. Linear Search")
        print("\t3. Sentinal Search")
        print("\t4. Exit")
        ch=int(input("Enter Choice: "))
        if ch==4:
            print("Thanks for using the program: ")
            quit()
        elif ch==1:
            l=accept_data(arr)
        elif ch==2:
            key=int(input("Enter element do you want to search: "))
            linear_search(arr,l,key)
        elif ch==3:
            key=int(input("Enter element do you want to search: "))
            sentinal_search(arr,l,key)
        else:
            print("Enter valid Choice")
   
main()
