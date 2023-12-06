with open('day_2.txt') as f:
    ans = 0
    for line in f:

        parsed_line = line.split()


        min_blue = 0
        min_red = 0
        min_green = 0
        for i in range(2, len(parsed_line), 2):
            if parsed_line[i + 1][:3] == 'red':
                min_red = max(min_red, int(parsed_line[i]))
            elif parsed_line[i + 1][:4] == 'blue':
                min_blue = max(min_blue, int(parsed_line[i]))
            elif parsed_line[i + 1][:5] == 'green':
                min_green = max(min_green, int(parsed_line[i]))

        ans += min_blue * min_green * min_red
    print(ans)