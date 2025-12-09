import ast

line = "y = (4*5) - 3"

tree = ast.parse(line)

print(ast.dump(tree, indent=4))

# the (4*5) is represented by a BinOp node where (operator) op=Mult(), the left operand is constant with value 4 and same for the right operand with value 5
# the (.. -  3) is the parent BinOp node, its (operator) op=Sub(), the left operand is the muliplication node and the right operand is the constant value 3

# Binary operations in the AST are structured recursively.
# A BinOp node consisits of 3 parts: left & right operands and the operator, if an operation is complex the operand can be nested