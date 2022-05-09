def getPuzzle(filename):
    fish = []
    f = open(filename, 'r')
    for line in f:
        for i in line:
            try:
                fish.append(int(i))
            except:
                continue
    return fish

def calculate_fish_growth_with_80(fish):
    days = 0
    while days < 80:
        for i in range(len(fish)):
            if fish[i] == 0:
                fish[i] = 6
                fish.append(8)
            else:
                fish[i] -= 1
        days += 1
    return len(fish)


def calculate_fish_growth_with_256(fish):
    days = 0
    while days < 256:

       # temp = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        temp = 0
        for amount in range(len(fish)):
             if amount == 0:
                 temp = fish[amount]
                #temp[6] += fish[amount]
                #temp[8] += fish[amount]
             else:
                 fish[amount-1] = fish[amount]

             fish[8] = temp
             fish[6] += temp
        days += 1
    fish.append(0)
    return fish


puzzle = getPuzzle('6dec.txt')
f = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in puzzle:
    f[i] += 1
print(f)
amount = calculate_fish_growth_with_256(f)
for a in range(len(amount)-1):
    amount[len(amount)-1] += amount[a]
#print(amount[len(amount)-1])

# 1632146183902
