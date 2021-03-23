# 각 응답에 따라 후보들이 획득할 점수, 지금은 5지선다에 문제 3개인 상황
# category의 넘버는 0:후보자개인 1:부동산 2:경제 3:복지 4:청년 5:사회적가치
POINT_SET = [
    {
        # Question 1
        'category': [0],
        'points': [[1, 0, 0, 0, 0],
                   [0, 1, 0, 0, 0]]
    },
    {
        # Question 2
        'category': [0],
        'points': [[0.71, 0.85, 1, 1, 0],
                   [1, 1, 1, 1, 0]]
    },
    {
        # Question 3
        'category': [1],
        'points': [[1, 0, 0, 0, 0],
                   [0, 1, 0, 0, 0]]
    },
    {
        # Question 4
        'category': [1],
        'points': [[1, 0, 1, 0, 0],
                   [1, 1, 0, 0, 0]]
    },
    {
        # Question 5
        'category': [1, 5],
        'points': [[1, 0, 0, 0, 0],
                   [0, 1, 0, 0, 0]]
    },
    {
        # Question 6
        'category': [1],
        'points': [[1, 0, 0, 0, 0],
                   [0, 1, 0, 0, 0]]
    },
    {
        # Question
        'category': [1],
        'points': [[0, 1, 0, 0, 0],
                   [1, 0, 0, 0, 0]]
    },
    {
        # Question 8
        'category': [2, 3],
        'points': [[1, 0, 0, 0, 0],
                   [0, 0, 1, 0, 0]]
    },
    {
        # Question 9
        'category': [3, 4],
        'points': [[0, 0, 1, 0, 0],
                   [1, 0, 0, 0, 0]]
    },
    {
        # Question 10
        'category': [2, 3, 4],
        'points': [[0, 1, 0, 0, 0],
                   [1, 0, 0, 0, 0]]
    },
    {
        # Question 11
        'category': [3, 5],
        'points': [[1, 0, 0, 0, 0],
                   [0, 1, 0, 0, 0]]
    },
    {
        # Question 12
        'category': [4, 5],
        'points': [[1, 0, 0, 0, 0],
                   [0, 1, 0, 0, 0]]
    },
    {
        # Question 13
        'category': [2, 4],
        'points': [[0, 1, 0, 0, 0],
                   [1, 0, 0, 0, 0]]
    },
    {
        # Question 14
        'category': [2, 3],
        'points': [[1, 0, 0, 0, 0],
                   [0, 1, 0, 0, 0]]
    },
    {
        # Question 15
        'category': [2, 4],
        'points': [[0, 1, 0, 0, 0],
                   [1, 0, 0, 0, 0]]
    },
    {
        # Question 16
        'category': [4, 5],
        'points': [[0.5, 0.5, 0, 0, 0],
                   [0, 1, 0, 0, 0]]
    },
    {
        # Question 17
        'category': [3, 5],
        'points': [[1, 0, 0, 0, 0],
                   [0, 1, 0, 0, 0]]
    },
    {
        # Category
        # TODO : points는 초기 가중치, set_category_weight에서 전역변수로 호출 후 수정됨
        'category': [-1],
        'points': [0.167, 0.313, 0.133, 0.140, 0.118, 0.128]
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


def set_category_weight(target):  # target은 맨 마지막 문제에서 고르는 선택지
    num_q = [2, 5, 5, 6, 6, 5]
    if POINT_SET[-1]['category'] == [-1]:
        category_list = POINT_SET[-1]['points'].copy()
        total_weight = 0
        for i in range(CATEGORY_NUM):
            total_weight += category_list[i]
        total_weight -= category_list[target]
        for i in range(CATEGORY_NUM):
            category_list[i] = category_list[i]*(0.65/(total_weight*num_q[i]))
        category_list[target] = 0.35/num_q[target]
        print('가중치')
        print(category_list)

    else:
        print('Category wight error detected')
    return category_list


def get_score(response_list):
    output = [[0., 0.] for _ in range(CATEGORY_NUM)]
    # 카테고리별로 얻은 점수 이러면 output이 [[1,1] [0,1]...]이런식으로 나오나?
    for index in range(len(response_list) - 1):  # response_list는 응답을 모아놓은 리스트
        response = response_list[index]  # response는 index번째 질문의 응답
        for cat in range(len(POINT_SET[index]['category'])):
            # category가 여러 개로 바뀜
            for cand in range(2):
                output[POINT_SET[index]['category'][cat]][cand] = output[POINT_SET[index]['category'][cat]][cand] +\
                    POINT_SET[index]['points'][cand][response - 1]
        # 여기서 149번쨰 줄에 \는 왜 들어간거지? +라는 문자를 살리고 싶어서?
    # print(output) #카테고리별 얻은 점수
    return output


def apply_weight(score_set, category_list):  # score_set은 응답을 모아놓은 리스트
    category_weight = category_list
    score_copy = score_set.copy()
    for i in range(len(score_copy)):
        score_copy[i] = [s*category_weight[i] for s in score_copy[i]]
    return score_copy  # 가중치를 곱한 응답의 리스트


def sum_score(score_sum):
    score_sum_copy = score_sum.copy()
    score_cand1, score_cand2 = 0, 0
    for set in score_sum_copy:
        score_cand1 += set[0]
        score_cand2 += set[1]
    return score_cand1, score_cand2


if __name__ == "__main__":
    response_list = [2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, ]
    result = calculate(response_list)
    print(result)  # OUTPUT : 가중치 곱하기 전 카테고리 별 점수 획득, 가중치 곱한 후 카테고리 별 점수 획득
