import turtle as t
import json

t.speed(0)
with open('info.json', 'r', encoding='UTF-8') as f:
    json_data = json.load(f)

t.color("white")
t.goto(json_data['4h']['xy'][0], json_data['4h']['xy'][1])
t.color("black")
for i in range(len(json_data['4h']['draw'])):
    t.goto(json_data['4h']['draw'][i][0], json_data['4h']['draw'][i][1])
t.write(json_data['4h']['name'])

t.color("white")
t.goto(json_data['60j']['xy'][0], json_data['60j']['xy'][1])
t.color("black")
for i in range(len(json_data['60j']['draw'])):
    t.goto(json_data['60j']['draw'][i][0], json_data['60j']['draw'][i][1])
t.write(json_data['60j']['name'])

t.color("white")
t.goto(json_data['5h']['xy'][0], json_data['5h']['xy'][1])
t.color("black")
for i in range(len(json_data['5h']['draw'])):
    t.goto(json_data['5h']['draw'][i][0], json_data['5h']['draw'][i][1])
t.write(json_data['5h']['name'])

t.color("white")
t.goto(json_data['lib']['xy'][0], json_data['lib']['xy'][1])
t.color("black")
for i in range(len(json_data['lib']['draw'])):
    t.goto(json_data['lib']['draw'][i][0], json_data['lib']['draw'][i][1])
t.write(json_data['lib']['name'])

t.color("white")
t.goto(json_data['law']['xy'][0], json_data['law']['xy'][1])
t.color("black")
for i in range(len(json_data['law']['draw'])):
    t.goto(json_data['law']['draw'][i][0], json_data['law']['draw'][i][1])
t.write(json_data['law']['name'])

t.color("white")
t.goto(json_data['west']['xy'][0], json_data['west']['xy'][1])
t.color("black")
for i in range(len(json_data['west']['draw'])):
    t.goto(json_data['west']['draw'][i][0], json_data['west']['draw'][i][1])
t.write(json_data['west']['name'])
'''
t.color("white")
t.goto(json_data['west2']['xy'][0], json_data['west2']['xy'][1])
t.color("black")
for i in range(len(json_data['west2']['draw'])):
    t.goto(json_data['west2']['draw'][i][0], json_data['west2']['draw'][i][1])
t.write(json_data['west2']['name'])


'''
