def twos_complement_binary(num, bits=8):
    return format(num & ((1 << bits) - 1), f'0{bits}b')


def signed_binary_arithmetic(a, b, operation):
    print("\nExpression:", f"({a}) {operation} ({b})")
    print("Operand 1:", twos_complement_binary(a))
    print("Operand 2:", twos_complement_binary(b))

    if operation == '+':
        result = a + b
    elif operation == '-':
        result = a - b
    else:
        print("Invalid operation")
        return

    print("Binary result:", twos_complement_binary(result))
    print("Decimal result:", result)

    if result < -128 or result > 127:
        print("Arithmetic Overflow: Yes")
    else:
        print("Arithmetic Overflow: No")


# Expression (a): +56 + (+29)
signed_binary_arithmetic(56, 29, '+')

# Expression (b): (-38) - (-23)
signed_binary_arithmetic(-38, -23, '-')

