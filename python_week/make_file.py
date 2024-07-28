import pandas as pd
import openai
import csv

# 엑셀 파일 불러오기
file_path = 'youtube_comments.xlsx'
comments_df = pd.read_excel(file_path)

# 댓글이 들어있는 열 이름이 "Comment"인지 확인
comments = comments_df['Comment'].tolist()

# OpenAI API 키 초기화
openai.api_key = 'key' 

filtered_comments = [comment for comment in comments if isinstance(comment, str) and comment.strip()]
# 댓글을 분류하는 함수
def classify_comment(comment):
    try:
        clean_comment = comment.replace('\n', ' ')  # '\n' 문자를 공백으로 대체
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Classify the following comment into one of [Positive, Negative, Neutral]:\n\n{clean_comment}"}
            ]
        )
        classification = response.choices[0].message.content.strip()
        if classification not in ["Positive", "Negative", "Neutral"]:
            classification = "Neutral"  # 인식되지 않은 응답은 중립으로 기본 설정
        return classification
    except Exception as e:
        return "Neutral"

# 각 댓글을 분류
categories = [classify_comment(comment) for comment in filtered_comments]

# 댓글과 분류 결과를 포함한 데이터프레임 생성
result_df = pd.DataFrame({
    'Category': categories,
    'Comment': filtered_comments
})

# 데이터프레임을 CSV 파일로 저장
output_csv_path = 'categories_and_comments.csv'
result_df.to_csv(output_csv_path, index=False, encoding='utf-8')

print(f'CSV 파일이 생성되었습니다: {output_csv_path}')
