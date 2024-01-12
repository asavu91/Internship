def extract_last_word(logcat_txt):
    result = []

    with open(logcat_txt, 'r') as file:
        for line in file:
            timestamp_str = line.split()[0] + ' ' + line.split()[1]

            if '03-14 17:56:07.996' <= timestamp_str <= '03-14 17:56:08.357':
                last_word = line.split()[-1]
                result.append(last_word)
            elif '03-14 17:56:08.357' < timestamp_str:
                break

    return result


logcat_txt = 'logcat.txt'
last_words = extract_last_word(logcat_txt)
print(last_words)
