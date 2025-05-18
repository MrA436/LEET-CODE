class Solution(object):
    def isPalindrome(self, s):
        a = 0
        b = len(s) - 1
        while a < b:
            while a < b and not s[a].isalnum():
                a += 1
            while a < b and not s[b].isalnum():
                b -= 1
            if s[a].lower() != s[b].lower():
                return False
            a += 1
            b -= 1
        return True


s = "A man, a plan, a canal: Panama"
sol = Solution()          
result = sol.isPalindrome(s)  

print(result)            
