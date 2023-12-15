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