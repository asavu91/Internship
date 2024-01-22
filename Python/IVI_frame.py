payloads_IVI_A102 = ["60", "20", "45", "6C", "FE", "3D", "4B", "AA", "40", "12", "6C", "AF", "05", "78", "4A", "04"]
binary_frame = ''.join(bin(int(payload, 16))[2:].zfill(8) for payload in payloads_IVI_A102)

def extract_signal_value(binary_frame, byte_position, bit_position, size):
    start_index = (byte_position * 8) + bit_position
    end_index = start_index + size
    signal_binary = binary_frame[start_index:end_index]
    signal_value = int(signal_binary, 2)
    return signal_value


passenger_seat_memo_request = {
    "byte_position": 0,
    "bit_position": 7,
    "size": 3
}

time_signal = {
    "byte_position": 5,
    "bit_position": 3,
    "size": 1
}

clim_fp_bright = {
    "byte_position": 5,
    "bit_position": 7,
    "size": 4
}


print("PassengerSeatMemoRequest:", extract_signal_value(binary_frame, **passenger_seat_memo_request))
print("Time:", extract_signal_value(binary_frame, **time_signal))
print("ClimFPBright:", extract_signal_value(binary_frame, **clim_fp_bright))