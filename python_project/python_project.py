from setting import SetApt
from print import *
from find_des import find_des

# 출발지 입력 / 전역 프레임에서 print_start호출 이후 print_start 함수가 stack 방식으로 실행되고 변수가 스택에 생성됨
# 함수를 호출하면 함수의 아래쪽 방향으로 함수가 추가되고 끝나면 위쪽 방향으로 사라짐
start_point = print_start()

print_strt_list()  # 도착지 목록 출력

end_point = print_end()  # 도착지 입력

set_f = SetApt()  # 초기 건물 그리기 / setting.py의 setApt 클래스

keyword_dict = {'start': start_point, 'end': end_point}
# 출발지에서 목적지까지 이동하는 터틀 그리기(키워드 인수와 딕셔너리 언패킹을 사용해 출발지와 목적지 매개변수 전달)
find_des(**keyword_dict)
