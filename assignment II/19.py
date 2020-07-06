class Parenthesis:
   def is_valid(self, str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for opening_parenthesis in str1:
            if opening_parenthesis in pchar:
                stack.append(opening_parenthesis)
            elif len(stack) == 0 or pchar[stack.pop()] != opening_parenthesis:
                return False
        return len(stack) == 0

case1 = Parenthesis().is_valid("(){}[]")
print(case1)
case2 = Parenthesis().is_valid("()[{)}")
print(case2)
case3 = Parenthesis().is_valid("()")
print(case3)