tall = 6

tall += 1
endLine = ''
for lineNr in range(1, tall):
    # print left part
    hashes = lineNr
    spaces = tall - lineNr - 1
    line = ''

    for s in range(spaces):
        line += ' '
    for h in range(hashes):
        line += '#'
    for rightHash in range(lineNr - 1):
        line += '#'
    if endLine == '':
        endLine = line
    print(line)

print(endLine)

