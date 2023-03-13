def result(final_budget, initial_budget, slots):
    total_used = 0

    #? difference[0], cost[1], reward[2]
    slots = [(slot[1] - slot[0], slot[0], slot[1]) for slot in slots]
    slots.sort(key=lambda slot: slot[0], reverse=True)
    while initial_budget <= final_budget:
        for i in range(len(slots) - 1):

            if initial_budget >= final_budget:
                return total_used

            if slots[i][1] <= initial_budget:
                initial_budget += slots[i][0]
                total_used += 1
                break

    return total_used


# example of input:
# 1
# 6 392 13
# 11 12
# 13 27
# 13 17
# 16 35
# 30 41
# 38 42

# Explanation
# In the first test case we start with an initial budget Bi of 13 and we have to reach a final budget Bf of
# 392. To reach the goal we have 6 different slot machines:
# • Slot machine 1 with a cost Ci of 11 and reward Ri of 12
# • Slot machine 2 with a cost Ci of 13 and reward Ri of 27
# • Slot machine 3 with a cost Ci of 13 and reward Ri of 17
# • Slot machine 4 with a cost Ci of 16 and reward Ri of 35
# • Slot machine 5 with a cost Ci of 30 and reward Ri of 41
# • Slot machine 6 with a cost Ci of 38 and reward Ri of 42
# A possible optimal solution is:
# • Use once the 2nd slot machine, increasing the budget from 13 to 27
# • Use 20 times the 4th slot machine, increasing the budget from 27 to 407, thus reaching the final
# budget Bf of 392

if __name__ == "__main__":
    f = open("input-slotmachine-2a6b.txt")
    testcases = f.readline()

    for testcase in range(1, int(testcases) + 1):
        number_of_slots, final_budget, initial_budget = f.readline().split(" ")
        number_of_slots, final_budget, initial_budget = int(
            number_of_slots), int(final_budget), int(initial_budget)
        slots = [
            list(map(int,
                     f.readline().split(" "))) for _ in range(number_of_slots)
        ]
        with open("output", "a") as fo:
            #? Output first car id
            fo.write(
                f"Case #{testcase}: {result(final_budget, initial_budget, slots)}\n"
            )

    f.close()