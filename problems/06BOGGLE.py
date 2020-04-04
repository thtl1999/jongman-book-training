SIZE = 5

def run_boggle():
    boggle = list()
    for _ in range(SIZE):
        boggle.append(list(input()))

    n_of_words = int(input())
    words = list()
    for _ in range(n_of_words):
        words.append(input())

    for word in words:
        postfix = ''
        if cal_boggle(boggle, word):
            postfix = 'YES'
        else:
            postfix = 'NO'

        print(word, postfix)


def cal_boggle(boggle, word):
    starts = find_init(boggle, word[0])
    memo = dict()

    for pos in starts:
        if find_next(boggle, word, memo, pos, 0):
            return True

    return False


def find_next(boggle, word, memo, pos, seq):
    if not (0 <= pos[0] < SIZE and 0 <= pos[1] < SIZE):
        return False
    if (pos, seq) in memo:
        return False

    if boggle[pos[0]][pos[1]] == word[seq]:
        seq = seq + 1
    else:
        return False

    if seq == len(word):
        return True

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue

            if find_next(boggle, word, memo, (pos[0]+i, pos[1]+j), seq):
                return True

    memo[pos, seq] = False
    return False


def find_init(boggle, c):
    starts = list()
    for row in range(SIZE):
        for col in range(SIZE):
            if boggle[row][col] == c:
                starts.append((row,col))
    return starts


if __name__ == '__main__':
    n_of_problems = int(input())

    for _ in range(n_of_problems):
        run_boggle()