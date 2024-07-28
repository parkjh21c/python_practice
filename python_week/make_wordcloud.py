import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# CSV 파일에서 댓글 데이터 로드 
df = pd.read_csv('categories_and_comments.csv')

# 그룹화
grouped_comments = df.groupby('Category')['Comment'].apply(' '.join).reset_index()

# 각 카테고리에 대한 워드 클라우드를 생성하는 함수
def generate_wordcloud(text, category):
    wordcloud = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf', width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title(f'Category : {category}')
    plt.axis('off')
    plt.xlabel(f'count : ')
    plt.show()

# 각 카테고리에 대한 워드 클라우드를 생성하고 표시
for index, row in grouped_comments.iterrows():
    generate_wordcloud(row['Comment'], row['Category'])


# 카테고리 추출
categories = df['Category'].values

# 문자열로 변환
text = ' '.join(categories)

positive = df['Category'].value_counts()['Positive']
negative = df['Category'].value_counts()['Negative']
neutral = df['Category'].value_counts()['Neutral']

# 워드 클라우드 생성
category = ['Positive', 'Negative', 'Neutral']
count = [positive, negative, neutral]

plt.figure(figsize=(10, 5))
plt.title('Count')
bar = plt.bar(category, count, color=['r','g','b'])
for rect in bar:
    height = rect.get_height()
    plt.text(rect.get_x()+rect.get_width()/2.0,height,  height, ha = 'center',va='bottom',size=12)
plt.show()