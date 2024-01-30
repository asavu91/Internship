def hex_to_binary(hex_payload):
    binary_payload = bin(int(hex_payload.replace(" ", ""), 16))[2:]
    return binary_payload.zfill(8 * ((len(binary_payload) + 7) // 8))

def binary_to_hex(binary_payload):
    hex_payload = hex(int(binary_payload, 2))[2:]
    return ' '.join(hex_payload[i:i + 2] for i in range(0, len(hex_payload), 2)).upper()


# split frame into 12 bytes
def frame_to_bytes(frame):
    return frame.split()

def split_frame_into_pdus(frame, ignore_bytes=4):

    bytes_list = frame_to_bytes(frame)
    pdus = [' '.join(bytes_list[i:i+12]) for i in range(0, len(bytes_list), 12)]
    return [pdu.split(' ', ignore_bytes)[-1] for pdu in pdus]

def split_into_pdus(frame):
    bytes_list = frame_to_bytes(frame)
    pdus = [' '.join(bytes_list[i:i + 12]) for i in range(0, len(bytes_list), 12)]
    return pdus

