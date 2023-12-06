with open("day_1.txt") as f:
    sum_ans = 0
    for line in f:
        num = ""
        for i in range(len(line)):
            if line[i].isdigit():
                num = line[i]
                break
        
        for i in reversed(range(len(line))):
            if line[i].isdigit():
                num += line[i]
                break
        sum_ans += int(num)
    print(sum_ans)