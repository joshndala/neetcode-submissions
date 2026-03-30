class Solution:
    def isValid(self, s: str) -> bool:
        closing = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }

        opening = []

        for c in s:
            if c == "{" or c == "[" or c == "(":
                opening.append(c)

            else:
                if not opening:
                    return False
                if opening.pop() != closing[c]:
                    return False

        if opening:
            return False

        return True