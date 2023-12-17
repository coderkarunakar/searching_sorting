                                    #BINARY SEARCH

#a array is given and we need to find out the specific element if element is found we need to return it's index else return -1 since -1 is not an element for any array


#NOTE:for binary search the elements need to be sorted..
arr=[int (x) for x in input('please enter the elements of the array ').split()]
y=arr.sort
ele=int(input("please enter the element u want to search"))
# Note:binary search will return it's index 
def binarysearch(arr,ele):
    start=0
    end=len(arr)-1
    while(start<=end):
        mid=(start+end)//2
        if(arr[mid]==ele):
            return mid
        elif(arr[mid<ele]):
            start=mid+1

        else:
            end=mid-1
    return -1
y=arr
print(binarysearch(y,ele))

#just please look my class notes as well once for better clarity this concept is really really so much easiest