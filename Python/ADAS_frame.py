#00
# Header #1 - 06 02
# DLC - 08
# PDU - 80 00 00 00 00 00 00 00

#00
# Header #2 - 05 D0
# DLC 2 - 08
# PDU #2 - FF 60 00 00 02 00 00 00
#

#00
# Header #3 - 06 01
# DLC #3 - 08
# PDU #3 - 80 00 00 00 00 00 00 00


# Ignored - 00 00 10 C7 77 8A 70 AB AF 88 2A 8C

payload_input = "80 00 00 00 00 00 00 00"
payload_input2 = "FF 60 00 00 02 00 00 00"
payload_input3 = "80 00 00 00 00 00 00 00"

signal_info = [
    ["LDW_AlertStatus", 2, 5, 2],
    ["LCA_OverrideDisplay", 5, 2, 1],
    ["DW_FollowUpTimeDisplay", 4, 7, 6]
]
def hex_to_binary(hex_payload):
    binary_payload = bin(int(hex_payload.replace(" ", ""), 16))[2:]
    return binary_payload.zfill(8 * ((len(binary_payload) + 7) // 8))

def binary_to_hex(binary_payload):
    hex_payload = hex(int(binary_payload, 2))[2:]
    return ' '.join(hex_payload[i:i+2] for i in range(0, len(hex_payload), 2)).upper()

def modify_signal(pdu, signal_info, new_value):
    binary_frame = hex_to_binary(pdu)

    signal_name, group_number, reverse_start_position, size = signal_info
    start_position = 7 - reverse_start_position

    # Extract the relevant group of 8 bits
    group = binary_frame[group_number * 8: (group_number + 1) * 8]

    # Modify the signal value
    group = group[:start_position] + format(new_value, f'0{size}b') + group[start_position + size:]

    # Update the binary frame with the modified group
    binary_frame = binary_frame[:group_number * 8] + group + binary_frame[(group_number + 1) * 8:]

    # Convert the modified binary frame back to hex
    modified_pdu = binary_to_hex(binary_frame)

    return modified_pdu

def show_modified_pdu(original_pdu, modified_pdu, signal_name, new_value):
    print(f"Original PDU: {original_pdu}")
    print(f"Modified PDU: {modified_pdu}")
    print(f"{signal_name} modified to: {new_value}")
    print("\n")

ldw_alert_status_new_value = 2
dw_follow_up_time_display_new_value = 45
lca_override_display_new_value = 1


modified_pdu1 = modify_signal(payload_input, signal_info[0], ldw_alert_status_new_value)
show_modified_pdu(payload_input, modified_pdu1, signal_info[0][0], ldw_alert_status_new_value)


modified_pdu2 = modify_signal(payload_input2, signal_info[2], dw_follow_up_time_display_new_value)
show_modified_pdu(payload_input2, modified_pdu2, signal_info[2][0], dw_follow_up_time_display_new_value)


modified_pdu3 = modify_signal(payload_input3, signal_info[1], lca_override_display_new_value)
show_modified_pdu(payload_input3, modified_pdu3, signal_info[1][0], lca_override_display_new_value)