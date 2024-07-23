import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 예시 파일에서 댓글 데이터 로드
df = pd.read_csv('./example_comments.csv')

# DataFrame에 'category'와 'comment' 열이 있다고 가정합니다.
# 댓글을 카테고리별로 그룹화합니다.
grouped_comments = df.groupby('category')['comment'].apply(' '.join).reset_index()

# 각 카테고리에 대한 워드 클라우드를 생성하는 함수
def generate_wordcloud(text, category):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title(f'카테고리: {category}의 워드 클라우드')
    plt.axis('off')
    plt.show()

# 각 카테고리에 대한 워드 클라우드를 생성하고 표시합니다.
for index, row in grouped_comments.iterrows():
    generate_wordcloud(row['comment'], row['category'])
