# so easy concept no need to worry just see the logic and the dry run ,always remember as per the logic only our dry run only our code will be made that's it ...


def bubblesort(arr):
    length=len(arr)

    # this i is for iterating all the elements purpose that's it 
    for i in range(length):
        # chenks every 2 consecutive elements+skips the maximum element in every round (this is done with length-1-)
        for j in range(length-1-i):
            # chenking every 2 consecutive elements till end 
            if (arr[j]>arr[j+1]):
                # for swaping purposse
                arr[j],arr[j+1]=arr[j+1],arr[j]


    
    
    
arr=[5,3,1,7]
bubblesort(arr)
print(arr)