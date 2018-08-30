# https://qiita.com/yori1029/items/a0ddd25c9571b28f3e1c
import cv2

if __name__ == '__main__':
    im = cv2.imread('test.png',0)
    #新しい配列に入力画像の一部を代入
    # dst = im[738:1028,563:1079]
    dst = im[500:770,560:1080]
    #書き出し
    cv2.imwrite('test_result.png',dst)
