
strt_list = ["나빌레관", "서호관", "5호관", "2호관", "60주년",
             "하이테크센터", "정석학술정보관", "본관", "학생회관", "9호관", "로스쿨"]


def print_start():
    start = input("출발지를 입력해주세요(정문 or 후문): ")
    #start=start.strip()
    if start not in ["정문", "후문"]:
        print("입력이 잘못 되었습니다. 종료합니다.")
        exit()
    return start  # return을 통해 출발지 정보 반환 -> 길찾기 터틀로 변수 전달 위해


def print_strt_list():
    for i in strt_list:  # 반복문으로 strt_list에 있는 원소 하나씩 출력
        if i == strt_list[-1]:
            print(i)
        else:
            print(i, end=", ")


def print_end():
    end = input("도착지를 선택해주세요: ")
    #start=end.strip()
    if end not in strt_list:
        print("입력이 잘못 되었습니다. 종료합니다.")
        exit()
    return end
