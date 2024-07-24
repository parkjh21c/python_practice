import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('./example_comments.csv')

# Combine comments for each category
comments_by_category = df.groupby('category')['comment'].apply(lambda x: ' '.join(x)).to_dict()

# Generate word clouds for each category
wordclouds = {}
for category, comments in comments_by_category.items():
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(comments)
    wordclouds[category] = wordcloud

# Plot word clouds
fig, axs = plt.subplots(len(wordclouds), 1, figsize=(10, 5 * len(wordclouds)))

for i, (category, wordcloud) in enumerate(wordclouds.items()):
    axs[i].imshow(wordcloud, interpolation='bilinear')
    axs[i].set_title(f'Word Cloud for {category} Comments')
    axs[i].axis('off')

plt.tight_layout()
plt.show()
