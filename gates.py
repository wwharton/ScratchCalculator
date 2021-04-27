class Gates(object):
    def and_gate(self, input_a, input_b):
        """
        And Gate: Output is True when both inputs are true

          a   b   output
        | 0 | 0 | 0 |
        | 0 | 1 | 0 |
        | 1 | 0 | 0 |
        | 1 | 1 | 1 |


        :param input_a:
        :param input_b:
        :return:
        """
        if input_b and input_a: return True
        else: return False

    def not_gate(self, input=False):
        """
        Not Gate: Output is True when Input is False

          a   output
        | 0 | 1 |
        | 1 | 0 |
        :param input:
        :return:
        """
        if not input: return True
        else: return False

    def nand_gate(self, input_a, input_b):
        """
        Nand Gate - (Not And Gate) Inverse And Gate

          a   b   output
        | 0 | 0 | 1 |
        | 0 | 1 | 1 |
        | 1 | 0 | 1 |
        | 1 | 1 | 0 |
        :param input_a:
        :param input_b:
        :return:
        """
        return self.not_gate(
            self.and_gate(input_a, input_b)
        )

    def or_gate(self, input_a, input_b):
        """
        Or gate: If either input is True, output is True

          a   b   output
        | 0 | 0 | 0 |
        | 0 | 1 | 1 |
        | 1 | 0 | 1 |
        | 1 | 1 | 1 |
        :param input_a:
        :param input_b:
        :return:
        """
        return self.nand_gate(
            self.not_gate(input_a),
            self.not_gate(input_b)
        )

    def xor_gate(self, input_a, input_b):
        """
        Xor Gate: (Exclusive Or Gate) - Only True when a single input is True

          a   b   output
        | 0 | 0 | 0 |
        | 0 | 1 | 1 |
        | 1 | 0 | 1 |
        | 1 | 1 | 0 |

        :param input_a:
        :param input_b:
        :return:
        """
        return self.and_gate(
            self.or_gate(input_a, input_b),
            self.nand_gate(input_a, input_b)
        )





if __name__ == '__main__':
    a = True
    b = True
    carry = True
    gates = Gates()
    # print(f'Input_A = {a}')
    # print(f'Input_B = {b}')
    # print(f'And Gate Result: {gates.and_gate(a, b)}')
    # print(f'Not Gate Result: {gates.not_gate(b)}')
    # print(f'Nand Gate Result: {gates.nand_gate(a, b)}')
    # print(f'Or Gate Result: {gates.or_gate(a, b)}')
    # print(f'Adder Result: {gates.xor_gate(a, b)}')
    sum_bit, carry_bit = gates.adder(a, b, carry)
    print(f'Adder of {a} and {b} - Sum: {sum_bit} - Carry: {carry_bit}')
