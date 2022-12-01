import turtle as t
import json

strt_dict = {"2호관": "2h", "60주년": "60j", "5호관": "5h", "정석학술정보관": "lib", "로스쿨": "law", "서호관": "west",
             "나빌레관": "nav", "본관": "1h", "하이테크센터": "hitech", "학생회관": "std", "9호관": "9h"}


def find_des(start, end):
    if start == "정문":  # 출발지로 정문을 입력했으면
        with open('front.json', 'r', encoding='UTF-8') as f:  # front.json파일을 열어 json_data에 저장
            json_data = json.load(f)
        t.color("white")  # 터틀을 해당 좌표로 이동
        t.goto(95, -275)  # 인스턴스를 통한 메소드 호출
        t.color("red")  # 터틀의 색을 빨갛게 하고 길 이동
        for i in range(len(json_data[strt_dict[end]]['go'])):  # 건물 외벽 그리기
            t.goto(json_data[strt_dict[end]]['go'][i][0],
                   json_data[strt_dict[end]]['go'][i][1])

    elif start == "후문":  # 출발지로 후문을 입력했으면
        with open('back.json', 'r', encoding='UTF-8') as f:  # back.json파일을 열어 json_data에 저장
            json_data = json.load(f)
        t.color("white")
        t.goto(170, 215)
        t.color("red")
        for i in range(len(json_data[strt_dict[end]]['go'])):  # 건물 외벽 그리기
            t.goto(json_data[strt_dict[end]]['go'][i][0],
                   json_data[strt_dict[end]]['go'][i][1])
