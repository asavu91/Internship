from frame_utils import hex_to_binary, binary_to_hex

frames = {
    "payload_1": {
        "Header": "06 02",
        "DLC": "08",
        "PDU": "80 00 00 00 00 00 00 00"
    },
    "payload_2": {
        "Header": "05 D0",
        "DLC": "08",
        "PDU": "FF 60 00 00 02 00 00 00"
    },
    "payload_3": {
        "Header": "06 01",
        "DLC": "08",
        "PDU": "80 00 00 00 00 00 00 00"
    },
    "payload_4": {
        "Header": "06 02",
        "DLC": "08",
        "PDU": "40 00 00 10 00 00 00 00"
    },
    "payload_5": {
        "Header": "D0",
        "DLC": "08",
        "PDU": "21 20 00 00 02 00 00 00"
    },
    "payload_6": {
        "Header": "06 01",
        "DLC": "08",
        "PDU": "80 00 00 00 00 00 00 00"
    }
}


signal_info = [
    ["LDW_AlertStatus", 2, 5, 2],
    ["LCA_OverrideDisplay", 5, 2, 1],
    ["DW_FollowUpTimeDisplay", 4, 7, 6]
]

def modify_signal(frame, signal_info, new_value):
    binary_frame = hex_to_binary(frame["PDU"])

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

# Frame 1 & 4 for LDW_AlertStatus
modified_pdu1 = modify_signal(frames["payload_1"], signal_info[0], ldw_alert_status_new_value)
show_modified_pdu(frames["payload_1"]["PDU"], modified_pdu1, signal_info[0][0], ldw_alert_status_new_value)

modified_pdu4 = modify_signal(frames["payload_4"], signal_info[0], ldw_alert_status_new_value)
show_modified_pdu(frames["payload_4"]["PDU"], modified_pdu4, signal_info[0][0], ldw_alert_status_new_value)

# Frame 2 & 5 for DW_FollowUpTimeDisplay
modified_pdu2 = modify_signal(frames["payload_2"], signal_info[2], dw_follow_up_time_display_new_value)
show_modified_pdu(frames["payload_2"]["PDU"], modified_pdu2, signal_info[2][0], dw_follow_up_time_display_new_value)

modified_pdu5 = modify_signal(frames["payload_5"], signal_info[2], dw_follow_up_time_display_new_value)
show_modified_pdu(frames["payload_5"]["PDU"], modified_pdu5, signal_info[2][0], dw_follow_up_time_display_new_value)

# Frame 3 & 6 for LCA_OverrideDisplay
modified_pdu3 = modify_signal(frames["payload_3"], signal_info[1], lca_override_display_new_value)
show_modified_pdu(frames["payload_3"]["PDU"], modified_pdu3, signal_info[1][0], lca_override_display_new_value)

modified_pdu6 = modify_signal(frames["payload_6"], signal_info[1], lca_override_display_new_value)
show_modified_pdu(frames["payload_6"]["PDU"], modified_pdu6, signal_info[1][0], lca_override_display_new_value)
