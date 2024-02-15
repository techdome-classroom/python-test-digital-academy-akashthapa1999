class Solution(object):

    def isValid(self, s):

        l1 = []

        store = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in store.values():
                l1.append(char)
            elif char in store.keys():
                if not l1 or l1[-1] != store[char]:
                    return False
                l1.pop()
            else:
                continue
        return not l1

s1 = Solution()

print(s1.isValid("()"))

print(s1.isValid("()[]{}")) 

print(s1.isValid("(]"))