
                                    #merge sort
# we need to merge two(sorted) arrays and sort it 
def mergesort(arr1,arr2):
#for iterating arr1 we are using i
    i=0
#for iterating arr2 we are using j
    j=0
    #finding length of both arrays
    len1=len(arr1)
    len2=len(arr2)
        #just creating an empty array for storing the arr1 and arr2
    arr=[]
    #creating an condition  i should less than len1 list and j should less than len2
    while((i<len1)and (j<len2)):
        # another condition array 1 index should less than array 2 index
        if (arr1[i]<arr2[j]):
#if this condition is true then it appends in the empty array
            arr.append(arr1[i])
            # then i increment takes place
            i=i+1
            # if above condition fails then this condition works
        else:
            arr.append(arr2[j])
            # and j increment takes place
            j=j+1
# this is for  left elements
# this condition i<len1 and j<len2 it append in empty  array
    while(i<len1):
        arr.append(arr1[i])
        i=i+1
    while(j<len2):
        arr.append(arr2[j])
        j=j+1
        # and finally that empty arr is returned
    return arr
arr1=[1,4,9,10]
arr2=[2,3,6,7,8]
arr=mergesort(arr1,arr2)
print(arr)

