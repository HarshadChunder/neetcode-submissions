class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def arithmetic_operation(operation, value, operand):
            match operation:
                case "+":
                    return value + operand
                case "-":
                    return value - operand
                case "*":
                    return value * operand
                case "/":
                    return value / operand
        
        operands = []
        valid_operations = ["+", "-", "*", "/"]

        for token in tokens:
            if token not in valid_operations:
                operands.append(int(token))
            else:
                if len(operands) > 1:
                    result = int(arithmetic_operation(token, operands[-2], operands[-1]))
                    operands.pop()
                    operands.pop()
                    operands.append(result)

        return operands[-1]
