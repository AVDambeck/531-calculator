orm = int(input("What is your ORM?\n"))

# The outer array is the full schedule. The nessted array is each week. Each value is a set.
template = [
        [0.65, 0.75, 0.85],
        [0.7, 0.8, 0.9],
        [0.75, 0.85, 0.95],
        [0.4, 0.5, 0.6]
    ]

schedule = []

for week in template:
    ls = []
    for lift in week:
        weight = lift * orm
        ls.append(weight)
    schedule.append(ls)

# Output

output_hort = f"""
\tSet 1\tSet 2\tSet3
Week 1\t{schedule[0][0]}\t{schedule[0][1]} \t{schedule[0][2]} 
Week 2\t{schedule[1][1]}\t{schedule[1][1]} \t{schedule[1][2]} 
Week 3\t{schedule[2][1]}\t{schedule[2][1]} \t{schedule[2][2]} 
Week 4\t{schedule[3][1]}\t{schedule[3][1]} \t{schedule[3][2]} 
"""

output_vert = f"""
\tWeek 1\t Week 2\tWeek 3\tWeek 4
Set 1\t{int(schedule[0][0])}x5\t{int(schedule[1][0])}x3\t{int(schedule[2][0])}x5\t{int(schedule[3][0])}x5
Set 2\t{int(schedule[0][1])}x5\t{int(schedule[1][1])}x3\t{int(schedule[2][1])}x3\t{int(schedule[3][1])}x5
Set 3\t{int(schedule[0][2])}x5\t{int(schedule[1][2])}x3\t{int(schedule[2][2])}x1\t{int(schedule[3][2])}x5
"""

print(output_vert)



