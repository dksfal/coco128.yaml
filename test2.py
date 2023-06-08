import os
import random
import shutil

folder_path = r'C:\Users\tnd07\Desktop\Labelimg\data\image'    # 라벨화된txt파일을 불러올 폴더의 경로
train_folder = r'C:\Users\tnd07\Desktop\Labelimg\dataset\train\labels'    # train파일들이 저장될 폴더의 경로
train_image_folder = r'C:\Users\tnd07\Desktop\Labelimg\dataset\train\images'    # train이미지 파일들이 저장될 폴더의 경로

val_folder = r'C:\Users\tnd07\Desktop\Labelimg\dataset\val\labels'    # val파일들이 저장될 폴더의 경로
val_image_folder = r'C:\Users\tnd07\Desktop\Labelimg\dataset\val\images'    # val이미지 파일들이 저장될 폴더의 경로

test_folder = r'C:\Users\tnd07\Desktop\Labelimg\dataset\test\labels'    # test파일들이 저장될 폴더의 경로
test_image_folder = r'C:\Users\tnd07\Desktop\Labelimg\dataset\test\images'    #test이미지 파일들이 저장될 폴더의 경로

label_files = []    #라벨 파일을 저장할 리스트
moved_files = set()    #이미 이동된 파일을 기록할 집합

for file_name in os.listdir(folder_path):
    if file_name.endswith('.txt'):    #.txt 확장자를 가진 파일만 선택
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r') as label_file:    #file_path의 경로안의 파일들을 읽을수 있게 해줌
            label_data = label_file.read()    #라벨파일의 내용을 읽음
            label_files.append((file_name, label_data))    #라벨파일 이름, 라벨파일 내용형태로 리스트에 추가

random.shuffle(label_files)    #랜덤하게 파일 분할

total_files = len(label_files)    #분할 비율 계산
train_ratio = int(total_files * 0.7)
val_ratio = int(total_files * 0.2)
test_ratio = total_files - train_ratio - val_ratio

def move_files(source_folder, destination_label_folder, destination_image_folder, files):   #라벨 파일과 이미지 파일을 소스 폴더로부터 주어진 대상 라벨 폴더와 대상 이미지 폴더로 이동
    for file_name, label_data in files:
        source_label_path = os.path.join(source_folder, file_name)    #이동할 라벨 파일의 원본 경로
        destination_label_path = os.path.join(destination_label_folder, file_name)    #이동할 라벨 파일의 대상 경로
        shutil.move(source_label_path, destination_label_path)  # 라벨 파일 이동

        source_image_path = os.path.join(source_folder, file_name.replace('.txt', '.png'))    #이동할 이미지 파일의 원본 경로
        destination_image_path = os.path.join(destination_image_folder, file_name.replace('.txt', '.png'))    #이동할 이미지 파일의 대상 경로
        shutil.move(source_image_path, destination_image_path)  # 이미지 파일 이동

move_files(folder_path, train_folder, train_image_folder, label_files[:train_ratio])    #train폴더로 라벨 파일과 이미지 파일 이동
move_files(folder_path, val_folder, val_image_folder, label_files[train_ratio:train_ratio + val_ratio])    #val폴더로 라벨 파일과 이미지 파일 이동
move_files(folder_path, test_folder, test_image_folder, label_files[train_ratio + val_ratio:])    #test폴더로 라벨 파일과 이미지 파일 이동

