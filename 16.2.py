"""
TODO: don't know what is included as bits in a packet, eg what is calculated as trailing zero
"""


def get_trailing_zeroes(number_of_bits_in_packet):
    for i in range(number_of_bits_in_packet, number_of_bits_in_packet + 10):
        if i % 4 == 0:
            return i - number_of_bits_in_packet


"""
:param current index and index of first version number
:return number of bits, without trailing zeroes 
"""


def bits_in_packet_from_index(i, j):
    return j - i


def fifteen_bit_length_type_id(i):
    return i == 0


"""
:param 11 or 15 bit part of bin
:return integer, either number of sub packets or number of bits in sub packets
"""


def read_number_from_binary(b):
    print('inside read nr:', b)
    return int(b, 2)


"""
:param part of bin and current index
:return last index of packet in binary string
"""


def extract_lit_value(b, i):
    for i in range(i, len(b) - 1, 5):
        if b[i] == '0':
            i += 5
            break
    return i


"""
:param part of bin and current index
:return last index of packet in binary string and sum of versions

TODO: can i send part of bin to read_bin() ???  
"""

# -> 011 000 1 00000000010 000 000 0 000000000010110 000 100 0 1010 101 100 0 1011 001000100000000010000100011000111000110100

def extract_operator(b, i):
    sum_version_numbers = 0
    if fifteen_bit_length_type_id(b[i]):
        bits_in_sub_packets = read_number_from_binary(b[i + 1:i + 16])
        i += 16
        sub_packet_end = i + bits_in_sub_packets
        while i < sub_packet_end:
            sum_version_numbers += read_number_from_binary(b[i:i + 3])  # !
            if b[i + 3:i + 6] == '100':
                i = extract_lit_value(b, i + 7)
            else:
                res = extract_operator(b, i + 7)
                i = res[0]
                sum_version_numbers += res[1]
    else:
        print('before sending:', b[i + 1:1 + 12])
        number_of_sub_packets = read_number_from_binary(b[i + 1:1 + 12])
        i += 12
        sum_version_numbers += read_number_from_binary(b[i:i + 3])  # !
        for j in range(number_of_sub_packets):
            if b[i + 3:i + 6] == '100':
                i = extract_lit_value(b, i + 7)
            else:
                res = extract_operator(b, i + 7)
                i = res[0]
                sum_version_numbers += res[1]

    return [i, sum_version_numbers]


"""
:param binary string
:return sum of version numbers 
"""


def read_bin(b):
    sum_version_numbers = 0
    index = 0
    q = len(b) - 11
    while (len(b) - 1) - index > 11:
        sum_version_numbers += read_number_from_binary(b[index:index + 3])  # !
        if b[index + 3:index + 6] == '100':
            index = extract_lit_value(b, index + 7)
        else:
            res = extract_operator(b, index + 7)
            index = res[0]
            sum_version_numbers += res[1]
    return sum_version_numbers


hex_string = '38006F45291200'
num_of_bits = len(hex_string) * 4
binary = bin(int(hex_string, 16))[2:].zfill(num_of_bits)
n = read_bin(binary)
print(n)


# version sum collected every time type id is controlled for = !
# # = from where to calculate trailing zeroes
# 8A004A801A8002F478 -> 100 010 1 # 00000000001 001 010 1 00000000001 101 010 0 000000000001011 110 100 # 0 1111 000
# 620080001611562C8802118E34
# -> 011 000 1 00000000010 000 000 0 000000000010110 000 100 0 1010 101 100 0 1011 001000100000000010000100011000111000110100

# D2FE28 -> 110 100 1 0111 1 1110 0 0101 000
# 38006F45291200 -> 001 110 0 000000000011011 110 100 0 1010 010 100 1 0001 0 0100 0000000
# EE00D40C823060 -> 111 011 1 00000000011 010 100 0 0001 100 100 0 0010 001 100 0 0011 00000
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


root = Node(10)

root.left = Node(34)
root.right = Node(89)
root.left.left = Node(45)