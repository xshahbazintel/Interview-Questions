how to reverse a number in python?

def reverse_number(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10  # Get the last digit
        reversed_num = reversed_num * 10 + digit  # Append the digit to reversed_num
        num //= 10  # Remove the last digit from num
    return reversed_num

how do you sort a list without using sort method?
selection sort:
def selection_sort(a):
    for i in range(0, len(a)):
        min = i  #setting first index position to min value
        for j in range(i+1, len(a)):
            if a[j] < a[min]:
                min=j
        a[i],a[min]=a[min],a[i]
    return a

what is package, module and library in python?
module is collection of functions
package is a directory with __init__.py method in that directory, its a collection of moduless
A Python library is a collection of related modules

write a python code that returns biggest sub array
sample_array = [3,5,0,7,2,1]
output=[7,2,1]

what is difference between set and dictionary in python
Set: A collection of unique values (no keys).
Dictionary: A collection of key-value pairs.

Set: You can only iterate over elements; there is no way to access them by index.
Dictionary: You can access values using their corresponding keys


which is fast tuple or list and why?

Use a tuple when your collection will not change and you need speed and memory efficiency.
Use a list when you need to modify the collection (add, remove, or change elements) and need more flexibility.



what are generators and iterators in python?
generators are memory efficient functions while operating with large  data sets
they avoid the need to store the entire data set in memory there by saving memory
they have yield which which will return a generator object instead of retuning a value.
Inside a program, when you call a function that has a yield statement, as soon as a yield is encountered, the execution of the function stops and returns an object of the generator to the function caller.

An iterator is an object that is used to iterate or loop through the iterables such as lists, tuples, dictionaries, sets.
you can make an iterable object iterator using iter() method
this has an next() method implementation that returns the next element of iterator 

what is shallow and deep copy?

In Python, shallow copy and deep copy refer to the ways you can duplicate an object. They differ in how they handle nested objects or mutable objects within the original object.
eg: 
original = [1, 2, [3, 4]]
shallow_copy = copy.copy(original)
address or id of original[2] i.e [3,4] is same for both orignal and shallow copy list
original = [1, 2, [3, 4]]
shallow_copy = copy.deepcopy(original)
address or id of original[2] i.e [3,4] is different for both orignal and shallow copy list
