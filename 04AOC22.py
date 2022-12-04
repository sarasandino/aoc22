fully=0
overlaps=0
with open('04-1-aoc22.txt') as inp:
    mylist=list(inp)
    for line in mylist:
        line=line.replace("-", ",")
        line=line.split(",")
        if int(line[0])<=int(line[2]) and int(line[1])>=int(line[3]):
            fully=fully+1
        elif int(line[2]) <= int(line[0]) and int(line[3])>=int(line[1]):
            fully=fully+1
        if int(line[0])<=int(line[2])<=int(line[1]):
            overlaps=overlaps+1
        elif int(line[1])<=int(line[3])<=int(line[1]):
            overlaps=overlaps+1
        elif int(line[2])<=int(line[0])<=int(line[3]):
            overlaps=overlaps+1
        elif int(line[2])<=int(line[1])<=int(line[3]):
            overlaps=overlaps+1
print(fully)
print(overlaps)