class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_ = set(('(', '[', '{'))
        full_ = set(("()", "[]", "{}"))
        for char in s:
            if char in open_:
                stack.append(char)
            else:
                if stack:
                    bracket_pair = stack[-1] + char
                    if bracket_pair not in full_:
                        return False
                    stack.pop()
                else:
                    return False

        return len(stack) == 0

            

        