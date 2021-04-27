class IOManager:

    def __init__(self):
        self.input = 0

        self.input_bin = 0
        self.input_bin_output = 0
        self.binary_int = 0
        self.output_int = 0

        self.get_input_bin()

    def get_input(self, input_var):
        self.input = input_var



    def get_input_bin(self):
        input_bin = bin(self.input)
        self.input_bin = input_bin.split('b')
        self.input_bin_output = self.input_bin[1]
        return self.input_bin_output

    def get_bin_bools(self):
        binary_str = str(self.input_bin_output)
        binary_list = list(binary_str)
        print(binary_list)
        self.bools_list = [True if x == str(1) else False for x in binary_list]
        return self.bools_list


    def bools_to_bin(self):
        binary_list = [str(1) if x == True else str(0) for x in self.bools_list]
        self.binary_int = int(''.join(binary_list))
        return self.binary_int

    def bin_to_int(self):
        self.binary_int = '0b' + str(self.binary_int)
        self.output_int = int(self.binary_int.encode('ascii'), 2)
        return self.output_int

    def int_to_bools(self, input_var):
        self.input = input_var
        self.get_input_bin()
        self.get_bin_bools()
        return self.bools_list

    def bools_to_int(self, input_list):
        self.bools_list = input_list
        self.bools_to_bin()
        self.bin_to_int()
        return self.output_int




if __name__ == '__main__':
    input_var = 134
    io_manager = IOManager()
    io_manager.get_input_bin(input_var())
    print(io_manager.int_to_bools())
    print(io_manager.bools_to_int())


