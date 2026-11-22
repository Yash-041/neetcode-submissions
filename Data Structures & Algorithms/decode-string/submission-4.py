class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cStr = ""

        for ch in s:
            if ch == ']':
                while stack[-1] != '[':
                    cStr = stack.pop() + cStr

                stack.pop()  # remove '['

                digits = ""
                while stack and stack[-1].isdigit():
                    digits = stack.pop() + digits

                num = int(digits)
                decoded = num * cStr

                stack.append(decoded)
                cStr = ""

            else:
                stack.append(ch)

        return "".join(stack)