import sys # sys 선언하여 사용하기 위함
import cv2

print('Hello, OpenCV', cv2.__version__) #cv2 버전 출력 코드

#imread: imageread의 약자, (폴더에 존재하는)파일 이름을 img로 불러오기
img = cv2.imread('cat.bmp')

#예외처리, 만일 img로 파일 불러오기가 실패했을 경우
if img is None:
    print('Image load failed!')
    sys.exit()

"""
- namedWindow(): OpenCV에서 지원하는 창(window)을 만드는 함수
- imshow(): imageshow 의 약자, 특정 wibndow에 영상을 보여주는 함수
    - 첫 번째 인자: 어떤 wondow에 보여줄 것인지, 
    - 두 번째 인자: 어떤 영상을 보여줄 것인지
- waitKey(): 키보드 입력을 기다리는 함수 + 영상이 화면에 보여줄 수 있게끔 함
- destroyAllWindows(): 기존의 모든 창 닫기
"""
cv2.namedWindow('image') #image라는 창을 하나 만든다.
cv2.imshow('image', img) #image 창에 img 영상을 보여주기
cv2.waitKey()

cv2.destroyAllWindows()