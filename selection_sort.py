#Note:this approach goes till n-1 elements...if we have n elements...

# # def selectionsort(arr):
# for finding the length 
# #     length=len(arr)
# for iterating all the elements till end -1 since it is rule as per this sort ,need to check till  end-1 elements...
# #     for i in range(length-1):
# this is for taking our first element as our mid index and comparing with all the elements
# #         minindex=i

#main logic our mid index element is compared with all the elements in the list if any small is found simply it swaps ,and it start searching from next element so we took i+1

# #         for j in range(i+1,length):  
# #             if (arr[j]<arr[minindex]):
# #                 minindex=j

#if condition satisfies then swaps...
# #         arr[i],arr[minindex]=arr[minindex],arr[i]


# # arr=[int (x) for x in input("enter the array elements").split()]
# # selectionsort(arr)
# # print(arr)



#simple some assignment ..
# # cn=complex(2,3)
# # print(cn)
# # print(cn.real)
# # print(cn.imag)
# # print(bool(5>3 ))



# # range and len() function
# # a=[2,3,4,5]
# # for i in range(len(a)):
# #     print(i,a[i])



                                            #SELECTION SORT...

def selectionsort(arr):
    length=len(arr)
    for i in range(length-1):
        midindex=i
        for j in range(i+1,length):
            if(arr[j]<arr[midindex]):
                midindex=j

        arr[i],arr[midindex]=arr[midindex],arr[i]

arr=[int (x) for x in input('enter the list elements').split( )]
selectionsort(arr)
print(arr)


