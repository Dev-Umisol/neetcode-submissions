class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        all_bracks = { ")" : "(", "]" : "[", "}" : "{"}

        for c in s:
            if c in all_bracks:
                if stack and stack[-1] == all_bracks[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False