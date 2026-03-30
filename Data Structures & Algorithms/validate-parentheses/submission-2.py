class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
                continue

            if not stack:
                return False
            
            x = stack.pop()

            if c == ')':
                if x != '(':
                    return False
            
            elif c == '}':
                if x != '{':
                    return False
            
            elif c == ']':
                if x != '[':
                    return False
        
        return not stack