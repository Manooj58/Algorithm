# Fractional Knapsack using brute-force
def knapSackFractional(length, data, size, initial):
    if initial == length or size <= 0:
        return 0

    # recursive calculation of profit
    if data[initial]["weight"] <= size:
        inclusive_profit = data[initial]["profit"] + \
            knapSackFractional(len(data), data, size -
                               data[initial]["weight"], initial+1)
        exclusive_profit = knapSackFractional(len(data), data, size, initial+1)

    # fractional profit calculation
    else:
        inclusive_profit = data[initial]["profit"] * \
            (size / data[initial]["weight"])
        exclusive_profit = knapSackFractional(len(data), data, size, initial+1)
    return max(inclusive_profit, exclusive_profit)


# 0/1 Knapsack using brute-force
def knapSack01(length, data, size, initial):
    if initial == length or size <= 0:
        return 0
    # recursive calculation of profit
    if data[initial]["weight"] <= size:
        inclusive_profit = data[initial]["profit"] + \
            knapSack01(len(data), data, size -
                       data[initial]["weight"], initial+1)
        exclusive_profit = knapSack01(len(data), data, size, initial+1)
        return max(inclusive_profit, exclusive_profit)
    else:
        exclusive_profit = knapSack01(len(data), data, size, initial+1)
        return exclusive_profit


# fractional Knapsack using greedy method
def greedy(box, size,):
    profit = 0

    # calculating profit-weight ratio
    for i in box:
        i["profit/weight"] = round(i["profit"] / i["weight"], 2)

    # sorting the data in reverse order
    box.sort(key=lambda x: x["profit/weight"], reverse=True)

    for i in box:
        if size <= 0:
            break
        # profit calculation
        if i["weight"] <= size:
            profit = profit + i["profit"]
            size = size-i["weight"]

        # fractional profit calculation
        else:
            profit = profit + i["profit"] * (size/i["weight"])
            size = 0
    return profit
