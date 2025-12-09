import dis

def calcuate_sum(a,b):
    return a+b

dis.dis(calcuate_sum)

# LOAD_FAST: fetch a local variable and pushes it onto the top of the evaluation stack
# BINARY_OP(+): pops the top 2 values off the stack, adds them together, and push the restul back onto the stack
# RETURN_VALUE: pops the value currently at the top of the stack and returns it to the caller

'''
Relation to the Stack-Based PVM:
These instructions illustrate the Stack-Based nature of the Python Virtual Machine because the operations are "zero-address" instructions.
Unlike Assembly (which uses specific registers like EAX), Python instructions do not specify where the data is; they implicitly assume the data is waiting for them at the top of the stack.
'''
