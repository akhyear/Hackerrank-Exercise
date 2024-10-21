n = int(input())
a  = "".join(str(i) for i in range(1,n+1))
print(a)

# Inside the generator expression, str(i) converts each number i into its string representation.
#The join() function is used to concatenate (join together) the elements in an iterable (in this case, the string representations of numbers).
# ''.join(...) means that the elements are joined with an empty string '' as the separator, which means no space will be inserted between the numbers. This results in a single string: '12345'.
