'''
in function iterativePower with base and exponent variable
    set the result equal to 1
    for every exponent value 
        set the result as eqaul to result time base
    then return the result
print the iterativePower function with base 2 and exp 3 into the function
'''
def iterativePower(base, exp):
    result = 1
    for i in range(exp):
        result *= base
    return result

print(iterativePower(2,3))
'''
in function recursivePower with base and exponent variable
    if exp equal to one
        return the base
    else
        return the base multiplied by the return value from the function with base and exp - 1
print the recursivePower function with base 2 and exp 3 into the function
'''
base = 0
exp = 0
def recursivePower(base, exp):
    if exp == 1:
        return base
    else:
        return base * (recursivePower(base, exp - 1))

print(recursivePower(2,3))