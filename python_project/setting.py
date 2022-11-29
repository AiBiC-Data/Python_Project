from turtle import Turtle
import json  # 딕셔너리 형태 자료형 사용


class SetApt(Turtle):  # 터틀 클래스 상속
    def __init__(self):  # 초기 실행
        super().__init__()  # 터틀 클래스의 init 실행
        self.speed(0)
        with open('info.json', 'r', encoding='UTF-8') as f:
            json_d = json.load(f)
            self.draw(json_d)

    def draw(self, json_data):
        structure = ("2h", "60j", "5h", "lib", "law", "west",
                     "nav", "1h", "hitech", "std", "9h")  # 튜플(변경되지 않을 건물 정보)로 각 건물 저장
        for j in structure:
            self.color("white")
            self.goto(json_data[j]['xy'][0], json_data[j]
                      ['xy'][1])  # 건물 좌표로 이동(이동 정보가 json 파일에 2차원으로 저장되어 있음)
            self.color("black")
            for i in range(len(json_data[j]['draw'])):  # 건물 외벽 그리기
                self.goto(json_data[j]['draw'][i][0],
                          json_data[j]['draw'][i][1])
            self.write(json_data[j]['name'])  # 건물 이름 출력
