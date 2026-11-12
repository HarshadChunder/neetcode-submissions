class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        def closing_bracket(bracket: str) -> str:
            match bracket:
                case ")":
                    return "("
                case "}":
                    return "{"
                case "]":
                    return "["

            return ""

        for bracket in s:
            if stack and stack[-1] == closing_bracket(bracket):
                stack.pop()
            else:
                stack.append(bracket)
        
        if len(stack) > 0:
            return False
        
        return True
        