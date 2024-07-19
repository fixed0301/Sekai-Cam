import cv2

img = cv2.imread("./test2.png")
h = len(img)
w = len(img[0])

if w*2/3 > h:
    h_f = h - h%6
    w_f = int(h_f*3/2)
    img = img[:h_f, ((w-w_f)//2):((w-w_f)//2+w_f)]

else:
    w_f = w - w%6
    h_f = int(w_f*2/3)
    img = img[((h-h_f)//2):((h-h_f)//2+h_f), :w_f]
print(img.shape)

cv2.imshow("arst", img)
if cv2.waitKey(0):
    quit()