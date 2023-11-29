'''
Excersise 1: Write a function that reads a string s, and prints that line on 
the standard output in reverse, that is, flipped right-to-left.

Example:
Input: "Hello World!"
Output: "!dlroW olleH"

Solution: Using string slicing with negative step/stride and omitting start 
and end indices.
'''
reversed = lambda s: s[::-1]

'''
Excersise 2: Write an algorithm that reads a number n. If n is even, then divide
it by 2. If n is odd, then multiply it by 3 and add 1. Repeat this process until
n is equal to 1. Print n and all subsequent results on the standard output.
See Collatz conjecture for more information.

Example:
Input: 5
Output: 5, 16, 8, 4, 2, 1
'''
def collatz(n):
    print(n, end=', ')
    if n == 1:
        return
    if n % 2 == 0:
        collatz(n // 2)
    else:
        collatz(n * 3 + 1)

'''
Excersise 3: Write a function that reads a list of integers l, and prints a 
histogram corresponding to those numbers in l on the standard output.

Example:
Input: [1,3]
Output: #
        ###
'''
def histogram(l):
    for i in l:
        print(i * '#')

'''
Excersise 4: Given all numbers between 1,2,...,n except one. Find the missing
number.

Example:
Input: 10, [2,8,10,6,5,1,3,4,7]
Output: 9
'''
def find_missing_number(n,l):
    gauss_sum = lambda n: (n * (n + 1)) // 2
    print(gauss_sum(n) - sum(l))

'''Exercises 5: Given a list of integers, find the longest identical sequence 
and print out the length of the sequence and the sequence itself.

Example:
Input: [1,1,1,2,2]
Output: 3, [1,1,1]
'''
def find_longest_identical_sequence(a):
    length_of_sequence = 1
    sequence = [a[0]]

    for i in range(1, len(a)):
        if a[0] == a[i]:
            length_of_sequence += 1
            sequence.append(a[i])
        else:
            new_length, new_sequence = find_longest_identical_sequence(a[i:])
            if length_of_sequence < new_length:
                length_of_sequence = new_length
                sequence = new_sequence

    return length_of_sequence if length_of_sequence > 1 else 0 , sequence if len(sequence) > 1 else []

if __name__ == '__main__':
    # s = input("Enter a string: ")
    # print(reversed(s))
    # collatz(5)
    # histogram([10,15,7,9,1,3])
    # find_missing_number(10,[2,8,10,6,5,1,3,4,7])
    a = [int(x) for x in input().split()]
    print(find_longest_identical_sequence(a))
