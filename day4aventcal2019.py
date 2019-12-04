INPUT_RANGE = [382345, 843167]

if __name__ == "__main__":
    count = 0
    for num in range(INPUT_RANGE[0], INPUT_RANGE[1]):
        d1 = num // 100000
        d2 = (num // 10000) % 10
        d3 = (num // 1000) % 10
        d4 = (num // 100) % 10
        d5 = (num // 10) % 10
        d6 = num % 10
        # 1st criteria part
        if (d1 <= d2 <= d3 <= d4 <= d5 <= d6):
            if (d1 == d2) or (d2 == d3) or (d3 == d4) or (d4 == d5) or (d5 == d6):
                # 2nd criteria part
                if (d4 < d5) and (d5 == d6):
                    count += 1
                elif (d3 < d4) and (d4 == d5) and (d5 < d6):
                    count += 1
                elif (d2 < d3) and (d3 == d4) and (d4 < d5):
                    count += 1
                elif (d1 < d2) and (d2 == d3) and (d3 < d4):
                    count += 1
                elif (d1 == d2) and (d2 < d3):
                    count += 1

    print(count)
