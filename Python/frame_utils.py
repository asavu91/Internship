def hex_to_binary(hex_payload):
    binary_payload = bin(int(hex_payload.replace(" ", ""), 16))[2:]
    return binary_payload.zfill(8 * ((len(binary_payload) + 7) // 8))

def binary_to_hex(binary_payload):
    hex_payload = hex(int(binary_payload, 2))[2:]
    return ' '.join(hex_payload[i:i + 2] for i in range(0, len(hex_payload), 2)).upper()

