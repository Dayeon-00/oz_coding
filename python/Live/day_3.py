#문자열
# #startwith
# print("python")
# print("python".startswith("p"))
# print("python".startswith("ff"))
# #find
# print("python hello")
# print("pytho hello".find("world")) #우리가 찾고자 하는 값이 없으면 -1을 출력합니,
# print("python hello".find("hello"))

# #islower / isupper
# print("hello".islower())
# print("Hello".islower())
# print("Hello".isupper())
# print("hello".isupper())

# #upper / lower
# print("hello".upper())
# print("HELLO".lower())

# #in 왼쪽에 있는 값이 오른쪽에 들어있는지를 확인해주는 기능을 가지고 있습니다.
# print("a" in "apple")
# print("f" in "apple")
# print("마르" in "동해물과 백두산이 마르고 닳도록") #값을 찾으면 그 값이 시작하는 인덱스를 알려주는 find

# my_strimg = "jarson"
# print(my_strimg[0:5:3])

#request


import requests
#2. 검색받은 키워드가 들어간 url을 만들어주세요

keyword = input("검색어를 입력하세요: ")
url = "https://search.naver.com/search.naver?ssc=tab.cafe.all&sm=tab_jum&query=" + keyword

html = requests.get(url) #get 요청이란?? 가져와. 내가 주소를 줄테니 사이트에 들어갈 수 있도록 화면을 구성할 수 있는 
print(html.text)