class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ticket = []
        for c in tokens:
            if c == "+":
                ticket.append(ticket.pop() + ticket.pop())
            elif c == "-":
                a, b = ticket.pop(), ticket.pop()
                ticket.append(b - a)
            elif c == "*":
                ticket.append(ticket.pop() * ticket.pop())
            elif c == "/":
                a, b = ticket.pop(), ticket.pop()
                ticket.append(int(float(b) / a))
            else:
                ticket.append(int(c))
        return ticket[0]
