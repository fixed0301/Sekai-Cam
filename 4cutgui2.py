import pygame
import pygame.camera
import pygame.image
from PIL import Image
import cv2
import time
# import playsound
from frameGen import *
from qr import *
from printers import *
# initialize game
pygame.init()

# screen option setting
# 1536, 864
size = [1920, 1080]
icon = pygame.image.load('gui_imgs/SADA_logo.png')
screen = pygame.display.set_mode(size)
pygame.display.set_icon(icon)
pygame.display.set_caption('사다네컷')


# game setting


class Obj:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.sx = 0
        self.sy = 0

    def put_img(self, img_path):
        if img_path[-3:] == 'png':
            self.img = pygame.image.load(img_path).convert_alpha()
        else:
            self.img = pygame.image.load(img_path)
        self.sx, self.sy = self.img.get_size()

    def change_size(self, sx, sy):
        self.img = pygame.transform.scale(self.img, (sx, sy))
        self.sx, self.sy = self.img.get_size()

    def show(self):
        screen.blit(self.img, (self.x, self.y))


# object setting

slide1 = Obj()
slide1.put_img('gui_imgs_v2/슬라이드1.png')
slide1.change_size(size[0], size[1])
slide1.x, slide1.y = 0, 0

slide2 = Obj()
slide2.put_img('gui_imgs_v2/슬라이드2.png')
slide2.change_size(size[0], size[1])
slide2.x, slide2.y = 0, 0

slide3 = Obj()
slide3.put_img('gui_imgs_v2/슬라이드3.png')
slide3.change_size(size[0], size[1])
slide3.x, slide3.y = 0, 0

slide4 = Obj()
slide4.put_img('gui_imgs_v2/슬라이드4.png')
slide4.change_size(size[0], size[1])
slide4.x, slide4.y = 0, 0

slide5 = Obj()
slide5.put_img('gui_imgs_v2/슬라이드5.png')
slide5.change_size(size[0], size[1])
slide5.x, slide5.y = 0, 0

slide6 = Obj()
slide6.put_img('gui_imgs_v2/슬라이드6.png')
slide6.change_size(size[0], size[1])
slide6.x, slide6.y = 0, 0

# check img
check1 = Obj()
check1.put_img('gui_imgs/check.png')
check1.change_size(250, 250)

check2 = Obj()
check2.put_img('gui_imgs/check.png')
check2.change_size(250, 250)

check3 = Obj()
check3.put_img('gui_imgs/check.png')
check3.change_size(250, 250)

bool1, bool2, bool3 = False, False, False

# slide event, frame
SB = 0
SN = 1
slide1.show()
FRAME_NUM = 0
ANIME_NUM = 0
mx, my = 0, 0
counter = 0
CUT = 1

# camera setting
codec = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(6, codec)
cam.set(5, 30)
cam.set(3, 1920)
cam.set(4, 1080)
cap = cam
width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Time
myFont = pygame.font.SysFont("malgungothic", 100, True, False)
number = myFont.render("8", True, (0, 0, 0))
number_rect = number.get_rect()
number_rect.centerx = 967
number_rect.y = 50

clock = pygame.time.Clock()

while SB == 0:
    # FPS setting
    pygame.time.delay(10)
    # update
    # pygame.display.flip()
    pygame.display.update()
    mx, my = 0, 0
    # sense inputs
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            print(mx, my)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()
    if SN == 1:
        slide1.show()
        if 768 < mx < 1153 and 641 < my < 760:
            SN = 2
    elif SN == 2:
        slide2.show()
        # check1
        if not bool1:
            if 189 < mx < 348 and 178 < my < 577:
                FRAME_NUM = 1
                check1.x, check1.y = 194, 263
                bool1 = True
            elif 353 < mx < 768 and 178 < my < 577:
                FRAME_NUM = 2
                check1.x, check1.y = 505, 263
                bool1 = True
            elif 807 < mx < 1077 and 178 < my < 577:
                FRAME_NUM = 3
                check1.x, check1.y = 830, 263
                bool1 = True
            elif 1118 < mx < 1387 and 178 < my < 577:
                FRAME_NUM = 4
                check1.x, check1.y = 1130, 263
                bool1 = True
            elif 1432 < mx < 1697 and 178 < my < 577:
                FRAME_NUM = 5
                check1.x, check1.y = 1440, 263
                bool1 = True
        # check2
        if bool2 and not bool3:
            if 189 < mx < 348 and 752 < my < 964:
                ANIME_NUM = [ANIME_NUM, 1]
                check3.x, check3.y = 194, 724
                bool3 = True
            elif 353 < mx < 768 and 753 < my < 963:
                ANIME_NUM = [ANIME_NUM, 2]
                check3.x, check3.y = 505, 724
                bool3 = True
            elif 807 < mx < 1077 and 753 < my < 963:
                ANIME_NUM = [ANIME_NUM, 3]
                check3.x, check3.y = 830, 724
                bool3 = True
            elif 1118 < mx < 1387 and 753 < my < 963:
                ANIME_NUM = [ANIME_NUM, 4]
                check3.x, check3.y = 1130, 724
                bool3 = True
            elif 1432 < mx < 1697 and 753 < my < 963:
                ANIME_NUM = [ANIME_NUM, 5]
                check3.x, check3.y = 1440, 724
                bool3 = True
        if not bool2:
            if 189 < mx < 348 and 752 < my < 964:
                ANIME_NUM = 1
                check2.x, check2.y = 194, 724
                bool2 = True
            elif 353 < mx < 768 and 753 < my < 963:
                ANIME_NUM = 2
                check2.x, check2.y = 505, 724
                bool2 = True
            elif 807 < mx < 1077 and 753 < my < 963:
                ANIME_NUM = 3
                check2.x, check2.y = 830, 724
                bool2 = True
            elif 1118 < mx < 1387 and 753 < my < 963:
                ANIME_NUM = 4
                check2.x, check2.y = 1130, 724
                bool2 = True
            elif 1432 < mx < 1697 and 753 < my < 963:
                ANIME_NUM = 5
                check2.x, check2.y = 1440, 724
                bool2 = True
        if bool1:
            check1.show()
        if bool2:
            check2.show()
        if bool3:
            check3.show()

        if bool1 and bool2 and bool3:
            SN = 3

    elif SN == 3:
        slide3.show()
        pygame.display.flip()
        pygame.time.delay(3000)
        SN = 4
        begin = time.time()

    elif SN == 4:
        slide4.show()
        ret, img = cap.read()
        #img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)
        #img_bgr = cv2.cvtColor(view, cv2.COLOR_RGB2BGR)
        crop_img = img[:,150:1920-150,:]
        surf = cv2.cvtColor(crop_img, cv2.COLOR_RGB2BGR)
        #surf = crop_img.transpose([0, 1, 2])
        surf = pygame.surfarray.make_surface(surf)
        nimg = pygame.transform.flip(surf, True, False)
        nimg = pygame.transform.rotate(nimg,90)

        tt = 8 # time sec
        end = time.time()
        number = myFont.render(str(tt-int(end-begin))+'          '+str(CUT)+'/2', True, (0, 0, 0))
        if int(end-begin) == tt:
            if not ret:
                print("failed to grab frame")

            img_name = 'photos/img' + str(CUT) + '.jpg'

            cv2.imwrite(img_name, crop_img)
            print("{} written!".format(img_name))
            CUT += 1
            begin = time.time()
            pygame.time.delay(1500)
            if CUT == 3:
                SN = 5

            '''ret, frame = cam.read()
            if not ret:
                print("failed to grab frame")
            img_name = 'photos/img'+str(CUT)+'.jpg'
            cv2.imwrite(img_name, frame)
            #print("{} written!".format(img_name))
            CUT += 1
            begin = time.time()
            pygame.time.delay(1500)
            if CUT == 5:
                SN = 5'''
        screen.blit(number, number_rect)
        print(crop_img.shape)
        screen.blit(pygame.transform.scale(nimg, (1620*0.71, 1080*0.71)), (381, 190))
        pygame.display.flip()

    elif SN == 5:
        slide6.show()
        pygame.display.flip()
        loc = generateImage(FRAME_NUM, ANIME_NUM) # 완성본 파일경로
        for _ in range(FRAME_NUM//2):
            printFile(loc)
        pygame.time.delay(5000)
        SN = 1
        slide1.show()
        FRAME_NUM = 0
        PEOPLE_NUM = 0
        mx, my = 0, 0
        counter = 0
        CUT = 1
        ANIME_NUM = []

pygame.quit()
