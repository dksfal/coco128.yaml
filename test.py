import os
import json

path = r'C:\Users\tnd07\Desktop\project\yolov5\coco128\labels\train2017\football.json'

# json_list = os.listdir(path)   #경로안에 파일 리스트 불러오기\
with open(f'{path}', 'r') as json1:    #경로안의 파일을 열고 읽을(r)수있게 함/with=with 블록을 벗어나는 순간 열린 파일 객체 f가 자동으로 닫힌다.(파일을 열면 항상 닫아줘야되기 때문)
        with open('football.txt', 'w') as f:
                json_data = json.load(json1)    #json 문자열을 파이썬객체로 변환
                json_shape = json_data['shapes']    #shapes리스트를 불러옴
                xywh_list = []    #xywh 빈 리스트 생성
                for shape in json_shape:    #json_shape 내의 모든 shape 를 반복
                        json_label = shape['label']    #label리스트를 반복적으로 불러옴
                        json_point = shape['points']    #points리스트를 반복적으로 불러옴
                        x_list = []     #x 빈 리스트생성
                        y_list = []     #y 빈 리스트생성
                        for xy in json_point:   #json_point 내의 모든 xy 반복
                                x_list.append(xy[0])    #x_list에 xy값중 x값에 해당하는 첫번째 좌표값을 추가
                                y_list.append(xy[1])    #y_list에 xy값중 y값에 해당하는 두번째 좌표값을 추가
                        x1, y1, x2, y2 = min(x_list), min(y_list), max(x_list), max(y_list)    #변수 x1,y1,x2,y2에 x1(x최솟값), y1(y최솟값), x2(x최댓값), y2(y최댓값)을 지정
                        xyxy = str(x1) + ',' + str(y1) + ',' + str(x2) + ',' + str(y2)    #x1,y1,x2,y2 값을 문자열로 바꿔 xyxy에 저장
                        x, y, w, h = (float(x1) + float(x2)) / 2, (float(y1) + float(y2)) / 2, float(x2) - float(x1), float(y2) - float(y1)     # 중심점 좌표와 너비, 높이 값을 계산
                        xywh = str(x) + ' ' + str(y) + ' ' + str(w) + ' ' + str(h)      #x,y,w,h 값을 문자열로 바꿔 xywh에 저장
                        if json_label == 'people':
                                json_label = 0
                        elif json_label == 'Half Line':
                                json_label = 1
                        f.write(f"{json_label} {x / json_data['imageWidth']} {y / json_data['imageHeight']} {w / json_data['imageWidth']} {h / json_data['imageHeight']}\n")    #x,y 각 가로 세로 길이에 대한 중심점 좌표값의 상대적 비율/ w,h각 가로 세로 길이에 대한 너비,높이의 상대적 비율





# import json
# import os
#
# with open(r'C:\Users\tnd07\Desktop\project\yolov5\coco128\labels\train2017\football.json','r') as f:
#     data = json.load(f)
#     data_shapes=data['shapes']
#     data_label=data_shapes[0]['label']
#     data_points=data_shapes[0]['points']
#     print(data_points)


# os.getcwd()
# os.listdir(r'C:\Users\tnd07\Desktop\project\yolov5\coco128\labels\train2017')
# files = os.listdir(r'C:\Usersshapes\tnd07\Desktop\project\yolov5\coco128\labels\train2017')
# len(files)
#
# for i in os.listdir(r'C:\Users\tnd07\Desktop\project\yolov5\coco128\labels\train2017'):
#     if i.endswith('json'):
#         print(i)

# for i in data_points:
#     print(i)

# import os
# import json
#
# path = r'C:\Users\tnd07\Desktop\project\yolov5\coco128\labels\train2017'
#
# json_list = os.listdir(path)    #경로안에 파일 리스트 불러오기
#
# for json_file in json_list:
#      with open(f'{path}/{json_file}', 'r') as json1:    #경로안의 파일을 열고 읽을(r)수있게 함/with=with 블록을 벗어나는 순간 열린 파일 객체 f가 자동으로 닫힌다.(파일을 열면 항상 닫아줘야되기 때문)
#         json_data = json.load(json1)    #json 문자열을 파이썬객체로 변환
#         json_shape = json_data['shapes']    #shapes리스트를 불러옴
#         json_label = json_shape[0]['label']    #label리스트를 불러옴/[0]= shapes 리스트 안에 label,points 리스트가 들어가있기 떄문
#         json_point = json_shape[0]['points']    #points리스트를 불러옴/[0]= shapes 리스트 안에 label,points 리스트가 들어가있기 떄문
#         x_list = []
#         y_list = []
#         for xy in json_point:
#             x_list.append(xy[0])    #x_list에 xy값중 x값에 해당하는 첫번째 좌표값을 추가
#             y_list.append(xy[1])    #y_list에 xy값중 y값에 해당하는 두번째 좌표값을 추가
#         x1, y1, x2, y2 = min(x_list), min(y_list), max(x_list), max(y_list)    #변수 x1,y1,x2,y2에 x1(x최솟값), y1(y최솟값), x2(x최댓값), y2(y최댓값)을 지정
#         xyxy = str(x1) + ',' + str(y1) + ',' + str(x2) + ',' + str(y2)
#         print('파일명 :', json_file)   #데이터를 뽑아왔을때
#         print('x1y1x2y2 : ',xyxy)
#         x, y, w, h = (int(x2)+int(x1))/2, (int(y1)+int(y2))/2, int(x2)-int(x1), int(y2)-int(y1)
#         xywh = str(x) + ',' + str(y) + ',' + str(w) + ',' + str(h)
#         print('xywh : ', xywh)