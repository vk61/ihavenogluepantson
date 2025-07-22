class Solution:
    def checkParanthesis(self,c1:str,c2:str):
        return ( c1=="(" and c2==")" ) or ( c1 == "{" and c2 == "}" ) or ( c1 == "[" and c2 == "]" )
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if len(stack) != 0:
                if self.checkParanthesis(stack[len(stack)-1],ch):
                    stack.pop()
                    continue
            else:
                stack.append(ch)

        return len(stack) == 0


input = "()[]"

print(Solution().isValid(input))
