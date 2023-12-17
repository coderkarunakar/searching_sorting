                                #INSERTION SORT
def insertionsort(arr):
    length=len(arr)
    #here i starts from index (1)to end 
    for i in range(1,length):
        #j starts from index 0 
        j=i-1
        #here every time temp is getting changed and first temp value starts with index 1
        temp=arr[i]
        # j value condition is >=0 and arr[j]>temp value if both are corect then swap takes place
        while(j>=0 and arr[j]>temp):
            #swap takes place..

            arr[j+1]=arr[j]
            # and every time j is getting reduced
            j=j-1
            # and every time arr[j+1] is assigned into temp
        arr[j+1]=temp
        
arr=[9,8,5,6,7,1]
insertionsort(arr)
print(arr)
