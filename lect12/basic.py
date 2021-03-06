'''
0. pillow 다루기 -> RGB사용 , 출력시 width:height
'''
from PIL import Image
import requests


#2.  웹 상에 있는 이미지 가져오기
url = "https://cdn.pixabay.com/photo/2020/05/24/08/40/machine-5213060__340.jpg"
img = Image.open(requests.get(url, stream=True).raw)
img.save("sample.jpg") # 웹 상이미지를 jpg형태로 내 컴퓨터에 저장하기


#1. 내 컴퓨터 폴더에 있는 이미지 가져오기 및 수정
img = Image.open("c:\\test\\sample.jpg") # Image를 열어서 img에 넣기
#img.show()
print(img.size)
img = img.rotate(45).show() # 이미지 45도 회전시키기
#img.save("sample.png") # 확장자가 jpg인것을 png로 바꾸기

'''
1. openCV 다루기 -> BGR 사용 , 출력시 height:width
'''
import cv2
import requests
import numpy # 고성능 연산을 위한 라이브러리

#2.  웹 상에 있는 이미지 가져오기
url = "https://cdn.pixabay.com/photo/2020/07/01/19/40/heidelberg-5360729__340.jpg"
arr = numpy.asarray(bytearray(requests.get(url).content), dtype=numpy.uint8) # 부호가 없는 8비트 정수형 타입으로 numpy 배열 생성
img =cv2.imdecode(arr, cv2.IMREAD_COLOR)

cv2.imshow("A", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 1. 내 컴퓨터 폴더에 있는 이미지 가져오기 및 수정
img = cv2.imread("sample.jpg", cv2.IMREAD_COLOR) # IMREAD_COLOR으로 읽겠다
print(img.shape) # 출력시 (340, 510, 3) -> 높이, 폭, _ 를 의미
cv2.imshow("A",img) # 'A'라는 자체 창 이름을 가진 뷰어로 열기
cv2.waitKey(0) # 다른 키 입력전까지 무한대로 화면에 뷰어떠 있게 하기
cv2.destroyAllWindows() # 다른 키를 입력하면 창 꺼지게 하기

'''
3. pillow와 openCV 호환하여 사용하기
'''
import cv2
import requests
import numpy
from PIL import Image

pil_image = Image.open("sample.jpg")
opencv_image = numpy.array(pil_image)
opencv_image = cv2.cvtColor(opencv_image, cv2.COLOR_RGB2BGR)

cv2.imshow("A", opencv_image)
cv2.waitKey(0)
cv2.destroyAllWindows()