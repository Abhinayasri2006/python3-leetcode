class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        # Track the start and end of the longest palindrome found
        start, end = 0, 0
        
        def extend(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the length of the palindrome found
            return right - left - 1

        for i in range(len(s)):
            # Case 1: Odd length (center is one character)
            len1 = extend(i, i)
            # Case 2: Even length (center is between two characters)
            len2 = extend(i, i + 1)
            
            max_len = max(len1, len2)
            
            # Update indices if a longer palindrome is found
            if max_len > (end - start):
                # Calculate new start/end based on center i and max_len
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
                
        return s[start : end + 1]
