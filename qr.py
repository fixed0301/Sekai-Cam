# qrcode generator
import qrcode
import cv2
import ftplib
import os
import time
import hashlib


def getMD5(text):
    text = text.encode()
    enc = hashlib.md5()
    enc.update(text)
    return enc.hexdigest()


def urltoQR(path, url):
    img = qrcode.make(url)
    img.save(path)
    cvimg = cv2.imread(path)
    cv2.imshow('QRcode openCV',cvimg)
    cv2.waitKey(0)
    # return qrcode path name


def connectServer(ftp):
    host, user, pw = 'sada.dothome.co.kr', 'sada', 'gbshs2024!!'
    ftp.connect(host=host, port=21)
    ftp.encoding = 'utf-8'
    s = ftp.login(user=user, passwd=pw)


def uploadtoServer(upload, name):  # upload 파일 경로를 넣으면 된다. 그러면 서버에 업로드
    try:
        with ftplib.FTP() as ftp:
            connectServer(ftp)
            ftp.cwd('/html/photo/')  # mkd: new folder generate
            with open(upload, 'rb') as file:
                ftp.storbinary('STOR ' + name + '.png', file)
    except Exception as e:
        print(e)

    URL = 'http://sada.dothome.co.kr/photo/' + name + '.png'
    return URL  # return server URL

# print(uploadtoServer('naver.png',getMD5(str(time.time()))[:10]))
