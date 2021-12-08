def read_input(filename='inputs/day08.txt'):
    with open(filename) as f:
        text = [line.strip() for line in f.readlines()]
    return text

def part1(text):
    total = 0
    for line in text:
        output = line.split(' | ')[1].split(' ')
        for digits in output:
            unique = len(digits)
            if unique in [2, 4, 3, 7]:
                total += 1
    return total

def part2(text):
    unique_to_number = {2 : {1}, 3: {7}, 4: {4}, 5: {2,3,5}, 6: {6,9,0}, 7: {8}}
    total = 0
    for line in text:
        inp, out = line.split(' | ')
        inp = [''.join(sorted(digits)) for digits in inp.split(' ')]
        out = [''.join(sorted(digits)) for digits in out.split(' ')]
        number_to_digits = {i : [] for i in range(10)}
        for digits in inp:
            for i in unique_to_number[len(digits)]:
                number_to_digits[i].append(digits)
        for digits in number_to_digits[6]:
            if len(set(digits).intersection(set(number_to_digits[1][0]))) == 1:
                number_to_digits[6] = [digits]
                number_to_digits[0].remove(digits)
                number_to_digits[9].remove(digits)
        for digits in number_to_digits[9]:
            if len(set(digits).intersection(set(number_to_digits[4][0]))) == 4:
                number_to_digits[9] = [digits]
                number_to_digits[0].remove(digits)
        for digits in number_to_digits[3]:
            if len(set(digits).intersection(set(number_to_digits[1][0]))) == 2:
                number_to_digits[3] = [digits]
                number_to_digits[2].remove(digits) 
                number_to_digits[5].remove(digits)       
        for digits in number_to_digits[5]:
            if len(set(digits).intersection(set(number_to_digits[6][0]))) == 5:
                number_to_digits[5] = [digits]
                number_to_digits[2].remove(digits)     
        digits_to_number = {x[0] : i for i,x in number_to_digits.items()}
        for i, digits in enumerate(out):
            total += 10**(3-i) * digits_to_number[digits]
    return total

text = read_input()
print(part1(text))
print(part2(text))