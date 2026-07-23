class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ''

        for c in s:
            if c.isalnum():
                new_string += c.lower() # append lowercase verison of letters to empty string
        
        return new_string == new_string[::-1]