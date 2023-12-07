with open('day_4.txt') as f:
    ans = 0
    for line in f:
        parsed_line = line.split()

        winning_nums = parsed_line[2:12]
        our_nums = parsed_line[13:]

        win_count = 0
        for num in our_nums:
            if num in winning_nums:
                win_count += 1
        
        ans += 2**(win_count - 1) if win_count != 0 else 0
    print(ans)