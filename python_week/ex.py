import pandas as pd
import random as r

# 데이터 예시 생성
data = {
    'category': ['Positive', 'Negative', 'Positive', 'Neutral', 'Negative', 'Positive'],
    'comment': [
        'I really love this product!',
        'I did not like it at all.',
        'Thank you for the excellent customer service.',
        'It was okay.',
        'I will never buy this again.',
        'Highly recommend!'
    ],
    'count' : [r.randint(1,10), r.randint(1,10), r.randint(1,10), r.randint(1,10), r.randint(1,10), r.randint(1,10)]
}

# 데이터프레임 생성
df = pd.DataFrame(data)

# CSV 파일로 저장
df.to_csv('example_comments.csv', index=False)
