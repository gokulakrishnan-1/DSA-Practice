class Solution:
    def reverseString(self, s: List[str]) -> None:
        stack = []
        for c in s:
            stack.append(c)
        
        i = 0
        for i in range(len(s)):
            s[i] = stack.pop()
            i += 1
        
        return s