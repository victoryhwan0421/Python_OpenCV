import sys # sys 선언하여 사용하기 위함
import cv2

print('Hello, OpenCV', cv2.__version__) #cv2 버전 출력 코드

"""
*imread(): image_read의 약자, (폴더에 존재하는)파일 이름을 img로 불러오기
"""
img = cv2.imread('cat.bmp')
img_gray = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE) # 흑백 출력

"""
예외처리, 만일 img로 파일 불러오기가 실패했을 경우(항상 이 예외처리 추가해주기!)
"""
if img is None:
    print('Image load failed!')
    sys.exit()

"""
* imwrite(): image_write의 약자, read한 내용이 담긴 img변수를 지정한 포맷으로 저장 
"""
cv2.imwrite('cat_origin.png', img) # .png, .jpg 등등 확장자 포맷 설정 가능
cv2.imwrite('cat_gray.jpg', img_gray)

"""
* namedWindow(winname, flags=None): OpenCV에서 지원하는 창(window)을 만드는 함수
    - 첫 번째 인자: 창 이름
    - 두 번째 인자: 창 크기
        - cv2.WINDOW_NORMAL: 영상 크기를 창 크기에 맞게 지정
        - cv2.WINDOW_AUTOSIZE: 창 크기를 영상 크기에 맞게 변경(기본값)


* imshow(): imageshow 의 약자, 특정 wibndow에 영상을 보여주는 함수
    - 첫 번째 인자: 어떤 wondow에 보여줄 것인지, 
    - 두 번째 인자: 어떤 영상을 보여줄 것인지

* waitKey(): 키보드 입력을 기다리는 함수 + 영상이 화면에 보여줄 수 있게끔 함

* destroyAllWindows(): 기존의 모든 창 닫기
"""
cv2.namedWindow('image') #image라는 창을 하나 만든다.
cv2.imshow('image', img) #image 창에 img 영상을 보여주기
cv2.waitKey()

cv2.destroyAllWindows()