class Solution:
    
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            "+":lambda a, b: a + b,
            "-":lambda a, b: a - b,
            "*":lambda a, b: a * b,
            "/":lambda a, b: int(a / b),
        }
        
        nums = []

        for token in tokens:
            if token in ops.keys():
               a = nums.pop()
               b = nums.pop()
               val = ops[token](b, a)
               nums.append(val)
            else:
                nums.append(int(token))

        return nums[-1]
        
