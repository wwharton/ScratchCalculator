from gates import Gates
from io_manager import IOManager

class Math(Gates):
    def __init__(self):
        self.sum_bit = 0
        self.io_manager = IOManager()
        self.input_a_bools = 0
        self.input_b_bools = 0
        self.bit_size = 0
        self.index = 0
        self.output_bool_list = []
        self.carry_bit = False



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

        # Insert False values to fill 4bit
        while len(input_a_bools) < 4:
            input_a_bools.insert(0, False)
        while len(input_b_bools) < 4:
            input_b_bools.insert(0, False)

        # Binary reads right to left, so we read the list from end index to beginning
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

        # These adders chain together, like doing formal addition. Starting from the right,
        # The first inputs are added - if it is TRUE TRUE, we have a carry -
        # So the carry from each previous operation chains to the next as the inputs are added

        output_a, carry_a = adder_a(carry)
        # print(output_a)
        # print(carry_a)
        output_b, carry_b = adder_b(carry_a)
        output_c, carry_c = adder_c(carry_b)
        output_d, carry_d = adder_d(carry_c)

        carry = carry_d

        # Convert final outputs into a list of bools, then back to an int
        output_bool_list = [output_d, output_c, output_b, output_a]
        print(output_bool_list)
        output_int = self.io_manager.bools_to_int(output_bool_list)
        print(output_int)
        print(carry)
        return output_int, carry


    def eight_bit_adder(self, input_a, input_b, carry=False):
        # self.io_manager.get_input(a)
        input_a_bools = self.io_manager.int_to_bools(input_a)
        input_b_bools = self.io_manager.int_to_bools(input_b)

        # Insert False values to fill 4bit
        while len(input_a_bools) < 8:
            input_a_bools.insert(0, False)
        while len(input_b_bools) < 8:
            input_b_bools.insert(0, False)

        # Binary reads right to left, so we read the list from end index to beginning
        input_a8 = input_a_bools[0]
        input_a7 = input_a_bools[1]
        input_a6 = input_a_bools[2]
        input_a5 = input_a_bools[3]
        input_a4 = input_a_bools[4]
        input_a3 = input_a_bools[5]
        input_a2 = input_a_bools[6]
        input_a1 = input_a_bools[7]

        input_b8 = input_b_bools[0]
        input_b7 = input_b_bools[1]
        input_b6 = input_b_bools[2]
        input_b5 = input_b_bools[3]
        input_b4 = input_b_bools[4]
        input_b3 = input_b_bools[5]
        input_b2 = input_b_bools[6]
        input_b1 = input_b_bools[7]

        sixteens_a = [input_a4, input_a3, input_a2, input_a1]
        sixteens_a_int = self.io_manager.bools_to_int(sixteens_a)

        sixteens_b = [input_b4, input_b3, input_b2, input_b1]
        sixteens_b_int = self.io_manager.bools_to_int(sixteens_b)

        thirtytwos_a = [input_a8, input_a7, input_a6, input_a5, False, False, False, False]
        thirtytwos_a_int = self.io_manager.bools_to_int(thirtytwos_a)

        thirtytwos_b = [input_b8, input_b7, input_b6, input_b5, False, False, False, False]
        thirtytwos_b_int = self.io_manager.bools_to_int(thirtytwos_b)



        output_sixteen, carry = self.four_bit_adder(sixteens_a_int, sixteens_b_int, carry)
        if carry:
            output_thirtytwo = self.four_bit_adder(thirtytwos_a_int, thirtytwos_b_int, carry)

        print(output_sixteen)
        print(output_thirtytwo)

    def variable_bit_adder(self, input_a, input_b, carry=False):
        self.input_a_bools = self.io_manager.int_to_bools(input_a)
        self.input_b_bools = self.io_manager.int_to_bools(input_b)

        if len(self.input_a_bools) >= len(self.input_b_bools):
            self.bit_size = len(self.input_a_bools) + 1
        else:
            self.bit_size = len(self.input_b_bools) + 1

        while len(self.input_a_bools) < self.bit_size:
            self.input_a_bools.insert(0, False)
        while len(self.input_b_bools) < self.bit_size:
            self.input_b_bools.insert(0, False)

        self.index = self.bit_size - 1
        self.output_bool_list = []

        self.carry_bit = False



        self.dynamic_adder()
        print(self.output_bool_list)
        output_int = self.io_manager.bools_to_int(self.output_bool_list)
        print(self.input_a_bools)
        print(self.input_b_bools)
        print(output_int)
        print(self.output_bool_list)








    def dynamic_adder(self):
        if len(self.output_bool_list) < self.bit_size:
            self.sum_bit, self.carry_bit = self.adder(self.input_a_bools[self.index], self.input_b_bools[self.index], self.carry_bit)
            self.output_bool_list.insert(0, self.sum_bit)
            self.index -= 1
            self.dynamic_adder()
        # else:
        #     sum_bit = 0
        #     carry_bit = 0
        return self.sum_bit, self.carry_bit








if __name__ == '__main__':

    a = 40000
    b = 9
    carry = False
    my_math = Math()
    # sum_bit, carry_bit = my_math.adder(a, b, carry)
    # print(f'Adder of {a} and {b} - Sum: {sum_bit} - Carry: {carry_bit}')
    # my_math.four_bit_adder(a, b, carry)
    # my_math.eight_bit_adder(a, b, carry)
    my_math.variable_bit_adder(a, b, carry)