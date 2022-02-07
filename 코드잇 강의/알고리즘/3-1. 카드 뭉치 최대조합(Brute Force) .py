#내가 직접푼거
# def max_product(left_cards, right_cards):
#     # 코드를 작성하세요.
#     max_list = []
#     for i in left_cards:
#         for j in right_cards:
#             max_list.append(i*j)
#     return max(max_list)

#다른 사람 해답1
# def max_product(left_cards, right_cards):
#     max = 0
#     for l in left_cards:
#         for r in right_cards:
#             if l*r > max:
#                 max = l*r
#             else:
#                 continue
#     return max

#다른 사람 해답2
def max_product(left_cards, right_cards):
    # 현재까지 최댓값을 담기 위한 변수
    # 처음에는 임시로 각 리스트의 첫 번째 요소의 곱으로 설정
    max_product = left_cards[0] * right_cards[0]

    # 가능한 모든 조합을 보기 위한 중첩 반복문
    for left in left_cards:
        for right in right_cards:
            # 현재까지의 최댓값 값과 지금 보고 있는 곱을 비교해서 더 큰 값을 최댓값 변수에 담아준다
            max_product = max(max_product, left * right)

    # 찾은 최댓값을 리턴한다
    return max_product

# 테스트
print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))