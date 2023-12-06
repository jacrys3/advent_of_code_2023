with open('day_2.txt') as f:
    num_ans = 0
    for line in f:
        parsed_line = line.split()
        good_game = True
        for i in range(2, len(parsed_line), 2):
            if (parsed_line[i + 1][:3] == 'red' and int(parsed_line[i]) > 12) \
                or (parsed_line[i + 1][:5] == 'green' and int(parsed_line[i]) > 13) \
                or (parsed_line[i + 1][:4] == 'blue' and int(parsed_line[i]) > 14):
                good_game = False
        if good_game:
            num_ans += int(parsed_line[1][:-1])
    print(num_ans)
