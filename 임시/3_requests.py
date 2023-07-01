# pip install requests
import requests

# ----------------------------------------------------------------------
res = requests.get("https://google.com")
res.raise_for_status() # 200이면 다음 코드를 실행하고 403이면 에러 발생.
# ----------------------------------------------------------------------

print("응답코드:", res.status_code) # 200 이면 정상
# if res.status_code == requests.codes.ok:
#     print("정상입니다")
# else:
#     print("문제가 생겼습니다. [에러코드] ", res.status_code, "]")


print(len(res.text))
print(res.text)

with open("mygoogle.html","w",encoding="utf8") as f:
    f.write(res.text)