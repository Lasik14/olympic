from collections import  namedtuple


Landmark = namedtuple("landmark", "interest cost name position")
def choose_landmarks(money:int, landmarks_data:list[str]) -> str:
    landmarks = transformation(landmarks_data)
    bag = {}
    for mn in range(50, money + 50, 50):
        bag[mn] = []
    for landmark in landmarks:
        for inner_bag in bag.keys():
            if len(bag[inner_bag]) == 0:
                if landmark.cost <= inner_bag:
                    bag[inner_bag].append([landmark])
                else:
                    bag[inner_bag].append([Landmark(0, 0, "", -1)])
            else:
                cell = introduction_landmark(inner_bag, landmark, bag)
                bag[inner_bag].append(cell)
    return prepear_answer(bag[-1][-1])

def transformation(data_landmarks:list) -> list:
    list_of_landmark = []
    for n, str_landmark in enumerate(data_landmarks):
        list_str_landmark = str_landmark.split(";")
        list_of_landmark.append(Landmark(int(list_str_landmark[0]), int(list_str_landmark[1]), list_str_landmark[2], n))
    landmarks = sorted(list_of_landmark, key=lambda m: m.interest, reverse=True)
    return landmarks

def introduction_landmark(inner_bag:int, landmark, bag):
    # cell = []
    if landmark.cost < inner_bag:
        #вмещается и остается место
        rest = inner_bag - landmark.cost #ищет остаток
        filling_bag = bag[rest][-1] #ищет сумку размером с этот остаток
        if len(filling_bag) <= 31: #если в сумке размером с остаток меньше или ровно 31 элемент
            filling_bag_interest = interest_bag(filling_bag) #считаем инетерес в сумке размером с остаток
            if landmark.interest + filling_bag_interest <= bag[inner_bag-50].interest:
                cell = bag[inner_bag][-1] #если предыдущая интереснее, то вписываем предыдущую
            else:
                cell = filling_bag.append(landmark) #если нынешняя интереснее всписываем ее
    elif landmark.cost == inner_bag:
        # вмещается и места не остается
        if landmark.interest <= interest_bag(bag[inner_bag - 50][-1]):
            cell = bag[inner_bag][-1]  # если предыдущая интереснее, то вписываем предыдущую
        else:
            cell = [landmark]  # если нынешняя интереснее всписываем ее
    else:
        cell = bag[inner_bag][-1]
        #не вмещается
    return cell

def interest_bag (landmarks):
    interest = 0
    for landmark in landmarks:
        interest += landmark.interest
    return interest

def prepear_answer (landmark:list)-> str:
    """"преобразует список в строку ответа"""
    return landmark

choose_landmarks(3000,
                            ["15;2100;Ermitazh",
                            "10;1500;Zimnij dvorec",
                            "10;1200;Isaakievskij sobor",
                            "8;1200;Kazanskij sobor v Peterburge",
                            "6;750;Krejser Avrora"])