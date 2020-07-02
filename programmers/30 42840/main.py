def solution(answer_sheet):
    students = {
        1: [1, 2, 3, 4, 5],
        2: [2, 1, 2, 3, 2, 4, 2, 5],
        3: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    }

    scores = dict()

    for student in students:
        index = 0
        score = 0
        for a_answer in answer_sheet:
            if students[student][index] == a_answer:
                score += 1
            index = (index + 1) % len(students[student])

        scores[student] = score

    maximum_score = max(scores.values())
    answer = []

    for key in scores:
        if scores[key] == maximum_score:
            answer.append(key)

    answer.sort()

    return answer