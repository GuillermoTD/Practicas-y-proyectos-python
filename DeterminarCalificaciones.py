def getGrade(n):
    nota = ["+A", "A", "B+", "B", "B-", "C", "D", "F"]
    min = [0, 45, 50, 55, 60, 65, 70, 75, 80]
    mx = [44, 49, 54, 59, 64, 69, 74, 79, 100]


t = int(input())

for i in range(t):
    m = int(input())
    lt = getGrade(m)
    print(f"Case{i+1}",lt)
    print("Case",lt).format()


