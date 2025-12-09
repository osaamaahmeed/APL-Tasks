import dis;

# 1
def square(x):
    return x*x
# 2
dis.dis(square)
# 3. bytecode instruction is: BINARY_OP(*)

# comparing muliplication with BINARY_ADD:
# Similarity: Both instructions take the top two items from the stack, perform a math operation, and return one result.
# Difference: The only difference is the math itself. One adds, the other multiplies.

# 4. 
def multiply(a,b):
    return a*b

dis.dis(multiply)


# The bytecode for multiply(a,b) is nearly identical to add().
# Both load two arguments (LOAD_FAST) and then perform a binary operation.
# multiply uses BINARY_OP(*), while add uses BINARY_ADD.