class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for ch in s:
            if ch==']':
                cStr=""
                while stack and stack[-1]!="[":
                    cStr=stack.pop()+cStr
                
                stack.pop()
                digit=""
                while stack and stack[-1].isdigit():
                    digit=stack.pop()+digit
                decoded=int(digit)*cStr
                stack.append(decoded)
                cStr=""
            else:
                stack.append(ch)
            
        return "".join(stack)