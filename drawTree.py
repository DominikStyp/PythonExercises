tall = 5

endLine = ''
for lineNr in range(1, tall+1):
    spaces = tall - lineNr
    line = ''
    for s in range(spaces):
        line += ' '
    for leftHash in range(lineNr):
        line += '#'
    for rightHash in range(lineNr - 1):
        line += '#'
    if endLine == '':
        endLine = line
    print(line)

print(endLine)

