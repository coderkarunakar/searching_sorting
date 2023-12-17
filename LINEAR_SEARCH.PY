#Linear search basic bacha logic.... based  on the list...



# n=int(input('please enter the total no of elemets u need '))

# #taking space seperated integers 
# li=[int(x) for x in input('please enter the elements one by one').split(',')]  #this is new list and here it splits according to the white space only...  note:if u give split based on comma , u need to give only , if u give space or any thing else it gives the error ...

# print(li)  #this line print the list based on the white space  till now what we gave in the input terminal

# ele=int(input('please enter the element u want to search '))

# isFound=False  #note:not only false we can give true as well  but need to chang it in the 
#below code as well...

# for i in range(len(li)): #this loop runs till the length of the li 
#     if li[i]==ele:       # if  our required li equal to our list elements 
#         print(i)           #then print that index number ,note:our index will be stored in i since we are running our loop with the help of 'i'
#         isFound=True
#         break
# if isFound is False:
#     print(-1)  #here -1 integer works since we gave boolean expression in the above line
#if u give simply and integer in the print it gives u an error here u gave an boolean value 
#so it is not giving an error ...




#here we are able to take the space seperated input and able to apply our algorithm successfully ..
#instead of this we can use the if else statement as well but this builds our logic super fast..
    
