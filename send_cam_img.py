import cv2
import requests
import numpy as np
# from retinaface import RetinaFace
import os

'''
def cropface(frame):
    faces = RetinaFace.detect_faces(frame)
    for faceNum in faces.keys():
        identity = faces[f'{faceNum}']
        facial_area = identity["facial_area"]
        landmarks = identity["landmarks"]

        # highlight facial area
        cv2.rectangle(frame, (facial_area[0], facial_area[1])
                      , (facial_area[2], facial_area[3]), (255, 255, 255), 1)

    facial_img = frame[facial_area[1]: facial_area[3], facial_area[0]: facial_area[2]]
    return facial_img
'''

def send(filename):
    # Flask 서버로 1번 파일만 업로드
    upload_url = 'http://172.16.82.127:5000/uploads'
    list_url = 'http://172.16.82.127:5000/files'

    images = []
    images.append(filename)

    for image_path in images:
        # 파일이 존재하는지 확인합니다.
        if not os.path.exists(image_path):
            print(f"File not found: {image_path}")
            continue

        with open(image_path, 'rb') as img_file:
            files = {'file': img_file}
            response = requests.post(upload_url, files=files)
            print(response.status_code, response.text)

    response = requests.get(list_url)
    if response.status_code == 200:
        files = response.json().get('files', [])
        print('Uploaded files on server:', files)
    else:
        print("Failed to retrieve file list from server")
    '''
    # 서버에서 업로드된 파일 삭제 요청
    delete_url = 'http://172.16.135.2:5000/delete'
    delete_response = requests.post(delete_url, json={'files': uploaded_files})
    
    if delete_response.status_code == 200:
        print("Files successfully deleted from server.")
    else:
        print("Failed to delete files from server.")
    '''