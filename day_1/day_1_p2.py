number_words = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
keywords = [
    ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
    [],
    ['one', 'two', 'six'],
    ['four', 'five', 'nine'],
    ['three', 'seven', 'eight']
]

def find_words(sentence, keywords):
    words = []
    for i in range(len(sentence)):
        for buffer in range(len(keywords)):
            for keyword in keywords[buffer]:
                if sentence[i:i+buffer+1] == keyword:
                    words.append(keyword)
    return words

with open("day_1.txt") as f:
    sum_ans = 0
    for line in f:
        words = find_words(line, keywords)
        first, last = words[0], words[-1]
        if first not in keywords[0]:
            first = number_words[first]
        if last not in keywords[0]:
            last = number_words[last]

        sum_ans += int(first + last)
    print(sum_ans)
