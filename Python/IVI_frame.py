from frame_utils import hex_to_binary

payload_input = "60 20 45 6C FE 3D 4B AA"
payload_input2 = "40 12 6C AF 05 78 4A 04"

signal_info = [
    ["PassengerSeat", 0, 7, 3],
    ["TimeFormat", 5, 3, 1],
    ["ClimFP", 5, 7, 4]
]

def extract_signal_value(signal_info, binary_string):

    #Impartem in grupuri de 8 biți payload-ul convertit
    binary_groups = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]

    #Extragem informațiile despre semnal din lista signal_info
    signal_name, group_number, reverse_start_position, size = signal_info

    #Calculează poziția de început pentru extragerea valorii semnalului
    start_position = 7 - reverse_start_position

    #Extrage grupul relevant de 8 biți
    group = binary_groups[group_number]

    #Extrage segmentul corespunzător valorii semnalului din grupul de 8 biți
    signal_value_bin = group[start_position: start_position + size]

    signal_value_decimal = int(signal_value_bin, 2)
    print(signal_name, signal_value_decimal)


def show_frame_value(input, info):
    binary_frame = hex_to_binary(input)
    for signal_info in info:
        extract_signal_value(signal_info, binary_frame)

print("----1st Frame----")
show_frame_value(payload_input, signal_info)
print("----2nd Frame----")
show_frame_value(payload_input2, signal_info)
