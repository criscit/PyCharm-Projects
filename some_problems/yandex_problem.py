def check(first: list, second: list):
    for el in first:
        if not el.isdigit():
            return False
    for el in second:
        if not el.isdigit():
            return False
    return True


try:
    with open('input_yandex_problem.txt') as file:
        answer = []
        employees_matches = file.readline().strip()
        if len(employees_matches.split()) == 2 and employees_matches.split()[0].isdigit() and employees_matches.split()[
            1].isdigit():
            employees_number = int(employees_matches.split()[0])
            matches_number = int(employees_matches.split()[1])
            for _ in range(matches_number):
                match_result = file.readline().strip().split()
                team = file.readline().strip().split()
                if check(match_result, team):
                    match_result = list(map(int, match_result))

                    if match_result[0] == match_result[1]:
                        answer.append(0)
                    elif match_result[0] > match_result[1]:
                        if team.index("0") < 5:
                            answer.append(0)
                        else:
                            answer.append(5)
                    elif match_result[0] < match_result[1]:
                        if team.index("0") > 5:
                            answer.append(0)
                        else:
                            answer.append(5)
                else:
                    answer.append(0)
        else:
            answer.append(0)
    answer = list(map(str, answer))
    answer = [element + '\n' for element in answer]
    with open('output_yandex_problem.txt', 'w') as file:
        file.writelines(answer)
except IndexError:
    print(0)
