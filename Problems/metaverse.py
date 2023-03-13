def result(guys, days_in_month, interval):
    count = 1

    temp = 0
    for days in range(2, days_in_month + 2):
        for num in interval:
            if (days - 1) % num == 0:
                temp += 1
                if temp == guys:
                    count += 1
                    temp = 0
        temp = 0

    return count


# example of input:
# 1
# 3 17
# 2 3 4

if __name__ == "__main__":
    with open("input-metaverse-fb03.txt") as file:
        content = file.readlines()
    testcases = int(content[0])
    tcase = 0
    for testcase in range(0, testcases):
        guys, days_in_month = content[testcase * 2 + 1].split(" ")
        guys, days_in_month = int(guys), int(days_in_month)
        interval = [int(n) for n in content[(testcase + 1) * 2].split(" ")]
        tcase += 1
        with open("output", "a") as f:
            o = result(guys, days_in_month, interval)
            f.write(f"Case #{tcase}: " + str(o) + "\n")
