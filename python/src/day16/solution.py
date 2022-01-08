class PacketDecoder():
    def __init__(self, file):
        with open(file, "r") as f:
            hex_string = f.readline()
        self.bin_string = bin(int("1" + hex_string, 16))[3:]

    def decode_packet(self):
        packet_version = int(self.bin_string[:3], 2)
        packet_type = int(self.bin_string[3:6], 2)
        rest = self.bin_string[6:]



    def get_literal_value(self, rest):
        final_bin = ""
        while len(rest) >= 5:
            print(rest)
            final_bin += rest[1:5]
            rest = rest[5:]
        return int(final_bin, 2)

    def get_operator_value(self, rest):
        pass


if __name__ == "__main__":
    print(f"Part 1: {PacketDecoder('test.txt').decode_packet()}")
    #print(f"Part 2: {PacketDecoder('test.txt').get_result(40)}")
