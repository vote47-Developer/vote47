# 각 응답에 따라 후보들이 획득할 점수, 지금은 5지선다에 문제 3개인 상황
POINT_SET = [
    {
        # Question 1
        'category' : 0,
        'points' : [[1, 0.5, 0.5, 0, 0],
                    [1, 1, 0, 0, 0]]
    },
    {
        # Question 2
        'category': 1,
        'points': [[0.71, 0.85, 1, 1, 0],
                   [1, 1, 1, 1, 0]]
    },
    {
        # Question 3
        'category': 3,
        'points': [[0, 1, 0, 0, 0],
                   [0, 0, 1, 0, 0]]
    },
    {
        # Question 4
        'category': 0,
        'points': [[1, 0, 1, 0, 0],
                   [1, 1, 0, 0, 0]]
    },
    {
        # Question 5
        'category': 0,
        'points': [[1, 0, 0, 0, 0],
                   [0, 1, 0, 0, 0]]
    },
    {
        # Question 6
        'category': 5,
        'points': [[0, 1, 0, 0, 0],
                   [0, 0, 1, 0, 0]]
    },
    {
        # Question 7
        'category': 0,
        'points': [[0, 0, 1, 0, 0],
                   [0, 1, 0, 0, 0]]
    },
    {
        # Question 8
        'category': 0,
        'points': [[1, 0, 0, 0, 0],
                   [0, 0, 1, 0, 0]]
    },
    {
        # Question 9
        'category': 2,
        'points': [[0, 0, 1, 0, 0],
                   [0, 1, 0, 0, 0]]
    },
    {
        # Question 10
        'category': 0,
        'points': [[0, 1, 0, 0, 0],
                   [1, 0, 0, 0, 0]]
    },
    {
        # Question 11
        'category': 5,
        'points': [[0, 1, 0, 0, 0],
                   [0, 0, 1, 0, 0]]
    },
    {
        # Question 12
        'category': 3,
        'points': [[1, 0, 0, 0, 0],
                   [0, 0, 1, 0, 0]]
    },
    {
        # Question 13
        'category': 0,
        'points': [[1, 0, 0, 0, 0],
                   [0, 0, 1, 0, 0]]
    },
    {
        # Question 14
        'category': 0,
        'points': [[0, 1, 0, 0, 0],
                   [0, 0, 1, 0, 0]]
    },
    {
        # Question 15
        'category': 0,
        'points': [[0, 0, 1, 0, 0],
                   [0, 1, 0, 0, 0]]
    },
    {
        # Question 16
        'category': 1,
        'points': [[0, 0, 0, 0, 0],
                   [0, 1, 0, 0, 0]]
    },
    {
        # Question 17
        'category': 0,
        'points': [[1, 0, 0, 0, 0],
                   [0, 1, 0, 0, 0]]
    },
    {
        # Category
        # TODO : points는 초기 가중치, set_category_weight에서 전역변수로 호출 후 수정됨
        'category': -1,
        'points': [1, 1, 1, 1, 1, 1]
    },
]
CATEGORY_NUM = 6

# 함수의 input인 response_list는 (질문의 수) 크기의 1D list. candidate_num은 후보의 수
def calculate(response_list):
    category_list = set_category_weight(response_list[-1])
    score_set = get_score(response_list)
    score_weight = apply_weight(score_set, category_list)
    score_sum = sum_score(score_weight)
    return score_set, score_weight, score_sum

def set_category_weight(target):
    if POINT_SET[-1]['category'] == -1:
        category_list = POINT_SET[-1]['points'].copy()
        category_list[target] = category_list[target] * 1.5
    else:
        print('Category wight error detected')
    return category_list

def get_score(response_list):
    output = [[0., 0.] for _ in range(CATEGORY_NUM)] #카테고리별로 얻은 점수
    for index in range(len(response_list) - 1):
        response = response_list[index]
        for cand in range(2):
            output[POINT_SET[index]['category']][cand] = output[POINT_SET[index]['category']][cand] +\
                                                         POINT_SET[index]['points'][cand][response - 1]
    #print(output) #카테고리별 얻은 점수
    return output

def apply_weight(score_set, category_list):
    category_weight = category_list
    score_copy = score_set.copy()
    for i in range(len(score_copy)):
        score_copy[i] = [s*category_weight[i] for s in score_copy[i]]
    return score_copy

def sum_score(score_sum):
    score_sum_copy = score_sum.copy()
    score_cand1, score_cand2 = 0, 0
    for set in score_sum_copy:
        score_cand1 += set[0]
        score_cand2 += set[1]
    return score_cand1, score_cand2

if __name__ == "__main__":
    response_list = [3, 2, 2, 1, 2, 3, 5, 2, 1, 5, 2, 4, 1, 1, 2, 1, 2, 1,]
    result = calculate(response_list)
    print(result) # OUTPUT : 가중치 곱하기 전 카테고리 별 점수 획득, 가중치 곱한 후 카테고리 별 점수 획득


