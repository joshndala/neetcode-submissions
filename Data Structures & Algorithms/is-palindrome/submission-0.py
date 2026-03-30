class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = s.lower().replace(" ", "") #lowercase and remove spaces
        letters = re.sub(r'[^a-zA-Z0-9]', '', letters) # remove special characters
        
        letters = list(letters)

        print(letters)

        firstLetter = 0
        lastLetter = len(letters) - 1

        print(lastLetter)

        while (firstLetter < lastLetter):
            if letters[firstLetter] != letters[lastLetter]:
                return False
            firstLetter += 1
            lastLetter -= 1

        return True