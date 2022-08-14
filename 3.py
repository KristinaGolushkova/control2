with open('text.txt') as f:
    a = f.read()
    print(sum(map(str.isalpha, a)), 'letters')
    print(a.count('\n') + 1, 'lines')