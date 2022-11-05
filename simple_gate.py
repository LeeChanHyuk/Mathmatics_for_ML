inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]

def and_gate(x1, x2):
    x1 *= 0.5
    x2 *= 0.5
    return (x1+x2) > 0.6

def or_gate(x1, x2):
    x1 *= 0.5
    x2 *= 0.5
    return x1+x2 > 0.01

def not_gate(x1):
    return x1 < 0

def xor_gate(x1, x2):
    and_gate(not_gate(and_gate(x1, x2)), or_gate(x1, x2))


for x1, x2 in inputs:
    print(xor_gate(x1, x2))