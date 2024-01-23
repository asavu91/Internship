payloads_IVI_A102 = ["60 20 45 6C FE 3D 4B AA", "40 12 6C AF 05 78 4A 04"]
binary_frame = ''.join(''.join(bin(int(byte, 16))[2:].zfill(8) for byte in frame.split()[::-1]) for frame in payloads_IVI_A102)

def extract_signal_value(binary_frame, frame_index, signal_info):
    byte_position = signal_info["byte_position"]
    bit_position = signal_info["bit_position"]
    size = signal_info["size"]

    start_index = (frame_index * 64) + (byte_position * 8) + bit_position
    end_index = start_index + size
    signal_binary = binary_frame[start_index:end_index][::-1]
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

# Extracting values for the first frame
print("PassengerSeatMemoRequest (Frame 1):", extract_signal_value(binary_frame, 0, passenger_seat_memo_request))
print("PassengerSeatMemoRequest (Frame 2):", extract_signal_value(binary_frame, 1, passenger_seat_memo_request))
print("Time (Frame 1):", extract_signal_value(binary_frame, 0, time_signal))
print("Time (Frame 2):", extract_signal_value(binary_frame, 1, time_signal))
print("ClimFPBright (Frame 1):", extract_signal_value(binary_frame, 0, clim_fp_bright))
print("ClimFPBright (Frame 2):", extract_signal_value(binary_frame, 1, clim_fp_bright))
