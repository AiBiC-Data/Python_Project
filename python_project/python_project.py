import turtle as t
import json
from setting import SetApt

start = input("출발지를 입력해주세요(정문 or 후문): ")
print(start)
if start != ("정문" or "후문"):
    print("입력이 잘못 되었습니다. 종료합니다.")
    exit()

strt_list = ["나빌레관", "서호관", "5호관", "2호관", "60주년",
             "하이테크센터", "정석학술정보관", "본관", "학생회관", "9호관", "로스쿨"]
for i in strt_list:
    if i == strt_list[-1]:
        print(i)
    else:
        print(i, end=", ")

end = input("도착지를 선택해주세요: ")
if end not in strt_list:
    print("입력이 잘못 되었습니다. 종료합니다.")
    exit()

strt_dict = {"2호관": "2h", "60주년": "60j", "5호관": "5h", "정석학술정보관": "lib", "로스쿨": "law", "서호관": "west",
             "나빌레관": "nav", "본관": "1h", "하이테크센터": "hitech", "학생회관": "std", "9호관": "9h"}

set_f = SetApt()  # 초기 건물 그리기

if start == "정문":
    with open('front.json', 'r', encoding='UTF-8') as f:
        json_data = json.load(f)
    t.color("white")
    t.goto(95, -275)
    t.color("red")
    for i in range(len(json_data[strt_dict[end]]['go'])):  # 건물 외벽 그리기
        t.goto(json_data[strt_dict[end]]['go'][i][0],
               json_data[strt_dict[end]]['go'][i][1])

elif start == "후문":
    with open('back.json', 'r', encoding='UTF-8') as f:
        json_data = json.load(f)
    t.color("white")
    t.goto(170, 215)
    t.color("red")
    for i in range(len(json_data[strt_dict[end]]['go'])):  # 건물 외벽 그리기
        t.goto(json_data[strt_dict[end]]['go'][i][0],
               json_data[strt_dict[end]]['go'][i][1])
