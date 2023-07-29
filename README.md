# 회사 별점 추출 프로그램

사람인에서 검색한 회사들의 잡플래닛 평점을 엑셀 파일로 추출하는 프로그램이다.

## 실행 순서

1. import되어 있는 코드들에 해당하는 패키지를 모두 설치. (pip install 패키지명)

   - pip install beautifulsoup4 : 스크래핑을 위한 패키지
   - pip install lxml : 구문 분석 파서하는 패키지
   - pip install openpyxl : 엑셀 사용하는 패키지

2. 사람인에 직업별 기준 원하는 키워드를 넣어서 검색.
3. 검색 결과, 3번째 페이지 url을 company버전.py 파일의 URLS.append(f'여기') 여기에 넣고 검색 결과의 총 페이지 개수를 PAGE_COUNT에 입력하기.
4. url에서 'page=숫자' 를 'page={index}' 로 변경
5. company버전.py 실행 -> 엑셀 파일 생성되는 것 확인
6. ratings버전.py 실행
7. 엑셀 파일 확인.

ratings버전.py는 검색한 회사 개수에 따라 완료까지의 시간이 상이하다.
Traceback이나 TypeError 등의 다른 문구가 뜨지않고 멈춰있는 것처럼 보인다면 실행되고 있는 것이다.

### [경로 및 파일명 수정하고 싶은 경우]

'./result/company2.2(2023-07-29).xlsx' 와 같은 경로들을 복사한 후 '[Ctrl] + h'로 원하는 대로 변경.

## ver 2.2

- 채용 기한 항목 추가
- 기업명에서 '(주)', '㈜' 문자로 인해 잡플래닛에서 정상적으로 검색되지 않는 경우가 있어 정규식으로 필터링

## ver 2.1

별점과 회사를 같이 보는 건 좋았으나, 여전히 공고를 들어가면 신입/경력 필터를 했음에도 불구하고 다른 결과가 나오는 경우가 발생하는 점에서 착안.

- 엑셀 파일에 공고명 항목 추가
- 검색 키워드가 달라지는 경우, 회사명이 정상적으로 추출되지 않는 경우가 발생하여 데이터 스크래핑 코드를 조건문으로 실행
- 개수 단위 변경하여 데이터 스크래핑해야 하는 과정 생략

## ver 2.0

- 브라우저 검색 방식에서 BeautifulSoup으로 데이터 스크래핑하는 방식으로 변경
- 엑셀 파일에 개수 항목 추가
  - 회사명 매칭에 따른 잘못된 별점이 추출되는 경우가 있어, 비슷한 회사명이 있는 경우 별점을 0.0으로 통일하는 대신 개수 항목에 비슷한 회사명 개수 저장

## ver 1.2.1

- 새 시트 추가하지 않고 파일 생성 시 기존 시트에서 수정
- URLS 리스트를 for 반복문으로 생성

## ver 1.2

- 검색 기준이 직업별인 경우, 회사 추출 코드가 일부 달라져 수정.

## ver 1.1

- 추출한 회사와 평점을 아래로 쭉 나열

## ver 1.0

- 40, 60, 80, 100개 등 개수 단위로 회사와 평점을 오른쪽으로 나열
- → 엑셀 필터 걸때 일부는 보이고 나머지는 안보이는 불편함 발생.
