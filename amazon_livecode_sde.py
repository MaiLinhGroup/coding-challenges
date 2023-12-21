# https://livecode.amazon.jobs/session/b2ac6ead-5781-4f09-bfca-e9db14537c96
# RLE Encoder
# Input: Buffer of bytes 
# Output: Buffer of bytes, compressed by RLE (https://en.wikipedia.org/wiki/Run-length_encoding)
# Example Input: WWWBCAAAAAB
# Example Output: 3W1B1C5A1B

def rle_encoder(input):
    if len(input) == 0:
        return ""
    else:
        output = ""
        count = 1
        for i in range(1, len(input)):
            if input[i] == input[i-1]:
                count += 1
            else:
                output += str(count) + input[i-1]
                count = 1
        output += str(count) + input[len(input)-1]
        return output
    
print(rle_encoder("WWWBCAAAAAB") == "3W1B1C5A1B")

# Given an integer array nums that does not contain any zeros,
# return the largest positive integer k such that -k also exists in the array.
# If such an integer does not exist, return -1.

def largest_positive_num(nums):
    k = -1
    
    if len(nums) <= 1:
        return k
    
    s = set(nums) # O(n)
    
    for i in nums: # O(n)
        if -i in s and i > k :
            k = i
    
    # O(n) + O(n) = 2*O(n) = O(n)
    return k

print(largest_positive_num([5,8,-1,2,-2,-8]))