carrying=[]
calories=0
with open('01-1-aoc22.txt') as inp:
    mylist = list(inp)
    for line in mylist:
        line=line.replace("\n", "")
        if line.isnumeric():
            calories=calories+int(line)
        else:
            carrying.append(calories)
            calories=0
print(max(carrying))
print(sum(sorted(carrying,reverse=True)[:3]))