from frame_utils import hex_to_binary, binary_to_hex
from frame_utils import frame_to_bytes, split_frame_into_pdus


frame_1 = "00 06 02 08 80 00 00 00 00 00 00 00 00 05 D0 08 FF 60 00 00 02 00 00 00 00 06 01 08 80 00 00 00 00 00 00 00 00 00 10 C7 77 8A 70 AB AF 88 2A 8C"
frame_2 = "00 06 02 08 40 00 00 10 00 00 00 00 00 05 D0 08 21 20 00 00 02 00 00 00 00 06 01 08 80 00 00 00 00 00 00 00 00 00 00 11 29 FB 84 33 1D E5 5E 9D"

# Split frames into PDUs

pdus_1 = split_frame_into_pdus(frame_1)
pdus_2 = split_frame_into_pdus(frame_2)


signal_info = [
    ["LDW_AlertStatus", 2, 5, 2],
    ["DW_FollowUpTimeDisplay", 4, 7, 6],
    ["LCA_OverrideDisplay", 5, 2, 1]
]

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

# New values for signals
ldw_alert_status_new_value = 2
dw_follow_up_time_display_new_value = 45
lca_override_display_new_value = 1

# Modify signals in frame 1
modified_pdu1 = modify_signal(pdus_1[0], signal_info[0], ldw_alert_status_new_value)
show_modified_pdu(pdus_1[0], modified_pdu1, signal_info[0][0], ldw_alert_status_new_value)

modified_pdu2 = modify_signal(pdus_1[1], signal_info[1], dw_follow_up_time_display_new_value)
show_modified_pdu(pdus_1[1], modified_pdu2, signal_info[1][0], dw_follow_up_time_display_new_value)

modified_pdu3 = modify_signal(pdus_1[2], signal_info[2], lca_override_display_new_value)
show_modified_pdu(pdus_1[2], modified_pdu3, signal_info[2][0], lca_override_display_new_value)

# Modify signals in frame 2
modified_pdu4 = modify_signal(pdus_2[0], signal_info[0], ldw_alert_status_new_value)
show_modified_pdu(pdus_2[0], modified_pdu4, signal_info[0][0], ldw_alert_status_new_value)

modified_pdu5 = modify_signal(pdus_2[1], signal_info[1], dw_follow_up_time_display_new_value)
show_modified_pdu(pdus_2[1], modified_pdu5, signal_info[1][0], dw_follow_up_time_display_new_value)

modified_pdu6 = modify_signal(pdus_2[2], signal_info[2], lca_override_display_new_value)
show_modified_pdu(pdus_2[2], modified_pdu6, signal_info[2][0], lca_override_display_new_value)
