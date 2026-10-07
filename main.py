# 1. 변수 만들기: 공지 한 건의 정보
title = "2026학년도 2학기 수강신청 안내" # 문자열(str)
department = "컴퓨터공학과"
category = "학사공지"
views = 152 # 정수(int)
is_new = True # 불리언(bool)



# 2. 봇 설정값
bot_name = "강원대 IT 소식봇"
check_interval = 1.5 # 실수(float): 수집 주기(시간 단위)
max_notices = 10 # 한 번에 보낼 최대 공지 수
is_running = False # 봇 작동 여부

# 3. type()으로 자료형 확인
print(type(title)) # <class 'str'>
print(type(views)) # <class 'int'>
print(type(check_interval)) # <class 'float'>
print(type(is_new)) # <class 'bool'>

# 4. 변수 값 바꾸기 / 연산
views = views + 1 # 조회수 1 증가 -> 153
print(view)

# 5. 문자열 다루기
message = "[" + department + "]" + title # 문자열 이어 붙이기
print(message)

line = "-" * 20 # 문자열 반복
print(line)

# 6. 형 변환
# 숫자는 문자열과 바로 이어 붙일 수 없어서 str()로 바꿔야 함
views_text = "조회수: " + str(views)
print(views_text)

# 웹에서 가져온 값은 "152"처럼 문자열로 오는 경우가 많음
views_from_web = "152"
views_number = int(views_from_web) # 문자열 -> 정수
print(views_number + 1) # 153

# 7. 값이 아직 없는 상태
attachment = None # 첨부 파일이 없는 공지
print(attachment)

# 8. 산술 연산자: 수집 주기와 페이지 계산
interval_minutes = check_interval * 60 # 시간 -> 분 (90.0)
print("수집 주기(분):", interval_minutes)

total_notices = 47 # 게시판에 쌓인 공지 수
per_page = 10 # 한 페이지에 보이는 공지 수
full_pages = totalnotice // per_page # 몫 : 4 (꽉 찬 페이지 수)
remain = total_notices % per_page # 나머지 : 7 (마지막 페이지의 공지 수)

# 나머지는 이어서 작성
