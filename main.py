def choose_landmarks(money:int, landmarks_data:list[str]) -> list[str]:
    for n, el in enumerate(landmarks_data):
        landmarks_data[n] += ';'+ str(n)
    landmarks= sorted(landmarks_data, key=lambda m : m[0], reverse=True)
    result = []
    matrix = []
    money_list=list(range(50, money+50, 50))
    for landmark in landmarks:
        matrix.append([])
        data_landmark=landmark.split(";")
        for mn in money_list:
            if int(data_landmark[1]) <= mn:
                if len(matrix) != 1:
                    bug=line_bug(matrix, mn, data_landmark)
                    bug_interest=interst_bug(bug)
                    current_max_bug = matrix[-2][len(matrix[len(matrix)-1])]
                    if current_max_bug:
                        if interst_bug(current_max_bug) < bug_interest:
                            matrix[-1].append(bug)
                        else:
                            matrix[-1].append(matrix[-2][len(matrix[len(matrix) - 1])])
                    else:
                        matrix[-1].append(bug)
                else:
                    matrix[-1].append(line_bug(matrix, mn, data_landmark))
            else:
                if len(matrix) != 1:
                    matrix[-1].append(matrix[-2][len(matrix[len(matrix) - 1])])
                else:
                    matrix[-1].append([])
    result=matrix[-1][-1]
    result = sorted(result, key=lambda m:m[-1])
    result_str=""
    for element in result:
        result_str += element[-2] + ';'
    result_str = result_str[:-1]
    return result_str

def line_bug(matrix, bug_size, landmark):
    result = []
    reserve=bug_size-int(landmark[1])
    if reserve >=50:
        bug_index = (reserve // 50) - 1
        for num_string in range(len(matrix)-2, -1, -1):
            if num_string == -1:
                break
            if len(matrix[num_string][bug_index]) <= 31:
                additional_landmark = matrix[num_string][bug_index]
                for elem in additional_landmark:
                    result.append(elem)
                break
    result.append(landmark)
    return result


def interst_bug(bug):
    interest=0
    for landmark in bug:
        interest=interest+int(landmark[0])
    return interest
#if __name__=="main":
    # money=int(input())
    # count=int(input())
    # lms = []
    # for _ in range(count):
    #     lms.append(input())
    # print(choose_landmarks(money,
    #                  lms))