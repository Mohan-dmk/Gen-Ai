import json
import time
import re
from datetime import datetime
from collections import Counter
from googleapiclient.discovery import build
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd

# Replace with your API key and video ID
API_KEY = 'AIzaSyBff9qL2zsyjL2ejS3dShOzTJmrwB_Qd5o'
VIDEO_ID = 'LY87Kmem5XM'
MAX_COMMENTS = 100000

youtube = build('youtube', 'v3', developerKey=API_KEY)

def get_comments(video_id, max_comments):
    comments = []
    next_page_token = None

    while len(comments) < max_comments:
        request = youtube.commentThreads().list(
            part='snippet,replies',
            videoId=video_id,
            maxResults=100,
            pageToken=next_page_token,
            textFormat='plainText'
        )
        response = request.execute()

        for item in response.get('items', []):
            top = item['snippet']['topLevelComment']['snippet']
            flat = {
                'author': top['authorDisplayName'],
                'comment': top['textDisplay'],
                'likes': top.get('likeCount', 0),
                'published_at': top['publishedAt'],
            }
            flat['polarity'] = TextBlob(flat['comment']).sentiment.polarity
            flat['sentiment'] = (
                'positive' if flat['polarity'] > 0
                else 'negative' if flat['polarity'] < 0
                else 'neutral'
            )
            comments.append(flat)

            for reply in item.get('replies', {}).get('comments', []):
                reply_snip = reply['snippet']
                r = {
                    'author': reply_snip['authorDisplayName'],
                    'comment': reply_snip['textDisplay'],
                    'likes': reply_snip.get('likeCount', 0),
                    'published_at': reply_snip['publishedAt'],
                }
                r['polarity'] = TextBlob(r['comment']).sentiment.polarity
                r['sentiment'] = (
                    'positive' if r['polarity'] > 0
                    else 'negative' if r['polarity'] < 0
                    else 'neutral'
                )
                comments.append(r)

            if len(comments) >= max_comments:
                break

        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break
        time.sleep(1)

    return comments

# Step 1: Scrape and save comments
all_comments = get_comments(VIDEO_ID, MAX_COMMENTS)

with open('yt_comments_flat.json', 'w', encoding='utf-8') as f:
    json.dump(all_comments, f, indent=2, ensure_ascii=False)

print(f"✅ Done. {len(all_comments)} comments saved to 'yt_comments_flat.json'")

# Step 2: Load JSON and convert to DataFrame
df = pd.DataFrame(all_comments)
df['published_at'] = pd.to_datetime(df['published_at']).dt.date

# Step 3: Sentiment pie chart
sentiment_counts = df['sentiment'].value_counts()
plt.figure(figsize=(6,6))
plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=140)
plt.title("Sentiment Distribution")
plt.savefig("sentiment_pie_chart.png")
plt.show()

# Step 4: Comment frequency by date
date_counts = df['published_at'].value_counts().sort_index()
plt.figure(figsize=(10, 5))
plt.plot(date_counts.index, date_counts.values, marker='o')
plt.xticks(rotation=45)
plt.title("Comments per Day")
plt.xlabel("Date")
plt.ylabel("Number of Comments")
plt.tight_layout()
plt.savefig("comment_activity.png")
plt.show()

# Step 5: Word cloud
all_text = ' '.join(df['comment'])
clean_text = re.sub(r'http\S+|www\S+|[^a-zA-Z\s]', '', all_text)
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(clean_text)
plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Word Cloud of Comments")
plt.savefig("wordcloud.png")
plt.show()
