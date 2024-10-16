class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # Total length of the string
        length = a + b + c
        
        # Initialize result string and character counters
        result = ''
        ca, cb, cc = 0, 0, 0
        
        # Iterate through the length of the string
        for _ in range(length):
            # Append 'a' if conditions met
            if (a >= b and a >= c and ca != 2) or (cb == 2 and a > 0) or (cc == 2 and a > 0):
                result += 'a'
                a -= 1
                ca += 1
                cb = cc = 0
            # Append 'b' if conditions met
            elif (b >= a and b >= c and cb != 2) or (ca == 2 and b > 0) or (cc == 2 and b > 0):
                result += 'b'
                b -= 1
                cb += 1
                ca = cc = 0
            # Append 'c' if conditions met
            elif (c >= b and c >= a and cc != 2) or (cb == 2 and c > 0) or (ca == 2 and c > 0):
                result += 'c'
                c -= 1
                cc += 1
                cb = ca = 0
            # Break if no conditions met
            else:
                break
        
        return result
