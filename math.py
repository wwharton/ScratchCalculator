from gates import Gates
from io_manager import IOManager

class Math(Gates):
    def __init__(self):
        self.io_manager = IOManager()
        super(Math, self).__init__()


    def adder(self, input_a, input_b, carry=0):
        sum_bit = self.xor_gate(
            self.xor_gate(input_a, input_b),
            carry
        )

        carry_bit = self.or_gate(
            self.and_gate(
                self.xor_gate(input_a, input_b),
                carry),
            self.and_gate(
                input_a,
                input_b
            )
        )

        return sum_bit, carry_bit


    def four_bit_adder(self, input_a, input_b, carry):
        # self.io_manager.get_input(a)
        input_a_bools = self.io_manager.int_to_bools(input_a)
        input_b_bools = self.io_manager.int_to_bools(input_b)
        while len(input_a_bools) < 4:
            input_a_bools.insert(0, False)
        while len(input_b_bools) < 4:
            input_b_bools.insert(0, False)

        input_a4 = input_a_bools[0]
        input_a3 = input_a_bools[1]
        input_a2 = input_a_bools[2]
        input_a1 = input_a_bools[3]

        input_b4 = input_b_bools[0]
        input_b3 = input_b_bools[1]
        input_b2 = input_b_bools[2]
        input_b1 = input_b_bools[3]
        print('tester')
        print(input_a_bools)
        print(input_b_bools)



        def adder_a(carry):
            print(input_a1)
            print(input_b1)
            print(carry)
            sum_bit, carry_bit = self.adder(input_a1, input_b1, carry)
            print(sum_bit)
            print(carry_bit)
            return sum_bit, carry_bit

        def adder_b(carry_a):
            sum_bit, carry_bit = self.adder(input_a2, input_b2, carry_a)
            return sum_bit, carry_bit

        def adder_c(carry_b):
            sum_bit, carry_bit = self.adder(input_a3, input_b3, carry_b)
            return sum_bit, carry_bit

        def adder_d(carry_c):
            sum_bit, carry_bit = self.adder(input_a4, input_b4, carry_c)
            return sum_bit, carry_bit

        output_a, carry_a = adder_a(carry)
        # print(output_a)
        # print(carry_a)
        output_b, carry_b = adder_b(carry_a)
        output_c, carry_c = adder_c(carry_b)
        output_d, carry_d = adder_d(carry_c)

        carry = carry_d

        output_bool_list = [output_d, output_c, output_b, output_a]
        print(output_bool_list)
        output_int = self.io_manager.bools_to_int(output_bool_list)
        print(output_int)
        print(carry)
        return output_int, carry




if __name__ == '__main__':

    a = 11
    b = 6
    carry = False
    my_math = Math()
    sum_bit, carry_bit = my_math.adder(a, b, carry)
    print(f'Adder of {a} and {b} - Sum: {sum_bit} - Carry: {carry_bit}')
    my_math.four_bit_adder(a, b, carry)