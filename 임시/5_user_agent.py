# 브라우저가 웹사이트 접속할 때 주는 헤더 정보에 따라서 모바일 페이지, PC 페이지 분류되어 보여짐
# pip install requests
import requests
url = "https://nadocoding.tistory.com";
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

res = requests.get(url, headers=headers) # 이렇게 해야 403에러 안뜨고 정상적으로 받아옴.
res.raise_for_status() # 200이면 다음 코드를 실행하고 403이면 에러 발생.



with open("nadocoding.html","w",encoding="utf8") as f:
    f.write(res.text)