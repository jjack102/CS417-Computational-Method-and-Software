import sys

MAX_DIGITS = 8

# Function to convert a decimal number to binary
def convert_dec_to_binary(dec_number):
    binary = []

    while dec_number > 0 and len(binary) < MAX_DIGITS:
        dec_number *= 2
        if dec_number >= 1:
            binary.append(1)
            dec_number -= 1
        else:
            binary.append(0)

    return binary

def main():
    # if arg is entered wrong it exits
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]:} <decimal_number1> <decimal_number2> ...")
        sys.exit(1)

    # prints header and divider
    print("|  Base 10  |   Base 2  |")
    print("|:" + "-" * 10 + "|:" + "-" * 10 + "|")

    # outputs the decimal num and binary num
    for arg in sys.argv[1:]:
        decimal_number = float(arg)
        binary = convert_dec_to_binary(decimal_number)

        binary_str = ''.join(map(str, binary))
        print(f"| {decimal_number:<9} | 0.{binary_str:<8}|")


if __name__ == "__main__":
    main()