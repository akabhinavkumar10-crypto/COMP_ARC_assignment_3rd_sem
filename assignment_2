def rotate_right(value, bits=8, positions=3):
    mask = (1 << bits) - 1
    value &= mask

    print("\nRotate Right Without Carry (ROR)")
    print("Original:", format(value, '08b'))

    for i in range(positions):
        lsb = value & 1
        value = (value >> 1) | (lsb << (bits - 1))
        print(f"After rotation {i + 1}:", format(value, '08b'))

    print("Final result:", format(value, '08b'))


def rotate_right_with_carry(value, carry=0, bits=8, positions=3):
    mask = (1 << bits) - 1
    value &= mask

    print("\nRotate Right Through Carry (RCR)")
    print("Original:", format(value, '08b'))
    print("Initial Carry:", carry)

    for i in range(positions):
        new_carry = value & 1
        value = (value >> 1) | (carry << (bits - 1))
        carry = new_carry

        print(
            f"After rotation {i + 1}:",
            format(value, '08b'),
            "| Carry:", carry
        )

    print("Final result:", format(value, '08b'))
    print("Final Carry:", carry)


# Use the last 8 bits of the given numbers
rotate_right(int("110111101"[-8:], 2))
rotate_right_with_carry(int("110100001"[-8:], 2), carry=0)

