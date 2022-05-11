#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def max_coins(rows, cols, coins, curr_row, curr_col):
    if curr_row == rows - 1:
        if curr_col == cols - 1:
            return coins[curr_row][curr_col]
        elif curr_col < cols - 1:
            return coins[curr_row][curr_col] + max_coins(
                rows, cols, coins, curr_row, curr_col + 1
            )

    elif curr_row < rows - 1:
        if curr_col == cols - 1:
            return coins[curr_row][curr_col] + max_coins(
                rows, cols, coins, curr_row + 1, curr_col
            )
        elif curr_col < cols - 1:
            return coins[curr_row][curr_col] + max(
                max_coins(rows, cols, coins, curr_row + 1, curr_col),
                max_coins(rows, cols, coins, curr_row, curr_col + 1)
            )


if __name__ == "__main__":
    n = 10
    m = 10
    coins = []
    for _ in range(n):
        row = list(map(int, input().split()))
        assert len(row) == m
        coins.append(row)

    rows = len(coins)
    cols = len(coins[0])

    max_value = max_coins(rows, cols, coins, 0, 0)

    neg_coins = []
    for row in coins:
        neg_coins.append([-value for value in row])

    min_value = -max_coins(rows, cols, neg_coins, 0, 0)

    print(f"{max_value}{min_value}")
