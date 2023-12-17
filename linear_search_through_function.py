#Linear search through fucntion..
#logic :search an element .if element is found return index of that element if not found return -1 in the given list of elements...

li=[int(x) for x in input('please enter the elements ').split()] #think slowly here nothing is there just only integer x is looping through the user integer(input) that first int will be applicable to x and input as well...
ele=int(input('please enter the element u want to search'))
def linearsearch(li,ele):
    for i in range(len(li)):
        if li[i]==ele:
            return i
    return -1
print(linearsearch(li,ele))  #this line is very much important in functions if we dont give we wont get the output this calling in the function is very much important..
