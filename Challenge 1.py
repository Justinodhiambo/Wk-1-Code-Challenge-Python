def solution1(A):
    total_bricks = sum(A)
    n = len(A)

    if total_bricks % n != 0 or total_bricks / n != 10:
        return -1

    moves = 0
    for i in range(n - 1):
        diff = A[i] - 10
        A[i] -= diff
        A[i + 1] += diff
        moves += abs(diff)

    return moves
