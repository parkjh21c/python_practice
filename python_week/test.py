import openai
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# OpenAI API 키 설정
openai.api_key = 'key'

# 크롬 드라이버 시작
driver = webdriver.Chrome()

try:
    # 원하는 유튜브 링크에 접속하기
    driver.get("https://www.youtube.com/watch?v=MuAl5oNPvSA")

    # 댓글 섹션이 로드될 때까지 대기
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#comments")))

    # 스크롤을 내려서 댓글을 로드
    last_height = driver.execute_script("return document.documentElement.scrollHeight")
    
    while True:
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(2)  # 페이지 로드 시간 대기

        new_height = driver.execute_script("return document.documentElement.scrollHeight")
        
        if new_height == last_height:
            break
        last_height = new_height

    # 충분히 스크롤을 내린 후 대기 시간을 추가하여 댓글 로드
    time.sleep(5)
    
    # 현재의 HTML 가져오기
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # 해당 영상의 댓글 태그 가져오기
    comments = soup.select("#content #content-text")

    # 댓글 내용을 리스트에 저장
    comment_list = [comment.get_text() for comment in comments]

finally:
    driver.quit()

# 댓글 리스트를 데이터프레임으로 변환
df = pd.DataFrame(comment_list, columns=["Comment"])

# 데이터프레임을 엑셀 파일로 저장
df.to_csv("youtube_comments1.csv", index=False)

print("댓글을 csv 파일로 저장했습니다.")

# 엑셀 파일에서 댓글 불러오기
df = pd.read_csv("youtube_comments1.csv")
comments = df["Comment"].tolist()

# 댓글 데이터 전처리: 공백이나 개행 문자 제거
comments = [str(comment).strip() for comment in comments]

print(comments)

# 댓글을 ChatGPT에게 전달하여 요약 요청
def get_summary_from_chatgpt(comments):
    # 댓글을 하나의 문자열로 합치기
    comments_str = "\n".join(comments)
    
    # ChatGPT에게 요약 요청
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"아래에 유튜브 영상 댓글을 모두 수집해 봤는데 이 댓글들의 대표적인 반응을 분류해서 요약해줄 수 있어?:\n\n{comments_str}"}
        ]
    )
    
    summary = response.choices[0].message.content
    return summary

# 요약된 결과 받기
summary = get_summary_from_chatgpt(comments)

# 요약된 결과 출력
print("댓글의 대표적인 반응 요약:")
print(summary)