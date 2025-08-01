import pandas as pd
import re
import nltk
import spacy
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Setup
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')
nlp = spacy.load("en_core_web_sm")

# Step 1: Paste your commentary here directly
raw_text = """The England players take their positions. Woakes has the new ball in his hands. KL and Jaiswal ready with their willows. Three slips and a gully to start us off
Teams line up for the anthems. India's Jana Gana Mana is followed by God Save the King.
DYK: The last time India won a toss in the Men's internationals was in January in a T20I match against England in Rajkot. Since then, they have lost 14 consecutive tosses.
Longest gaps between Test appearances
142 - Gareth Batty (ENG)
118 - Jaydev Unadkat (IND)
114 - Martin Bicknell (ENG)
109 - Floyd Reifer (WI)
104 - Younis Ahmed (PAK)
103 - Derek Shackleton (ENG)
102 - Liam Dawson (ENG)**
India has not won a Test match in Manchester on nine previous occasions. Whereas England has lost just 2 out of 20 Tests (14 won, 4 draws) at Old Trafford in this century.
England has won all four tosses in this Test series. No team winning the toss and bowling first has ever won an Old Trafford Test previously (3 lost, 8 draws).
In 1990, Anil Kumble was the last Indian to make his Test debut in Manchester. coincidentally, both Anil Kumble & Anshul Kamboj have a 10-wicket haul in FC Cricket.
All four tosses have gone England's way in this series, although Gill didn't seem to mind today as he was unsure about what to do. Interesting that India have decided to make the switch between Karun Nair and Sai Sudharsan. They both played at Leeds, Sudharsan was then left out, and he's now back in after Karun wasn't able to go big in the three Tests he played.
Teams:
India (Playing XI): Yashasvi Jaiswal, KL Rahul, Sai Sudharsan, Shubman Gill(c), Rishabh Pant(w), Ravindra Jadeja, Washington Sundar, Shardul Thakur, Anshul Kamboj, Jasprit Bumrah, Mohammed Siraj
England (Playing XI): Zak Crawley, Ben Duckett, Ollie Pope, Joe Root, Harry Brook, Ben Stokes(c), Jamie Smith(w), Liam Dawson, Chris Woakes, Brydon Carse, Jofra Archer
Shubman Gill: I was actually confused. Good toss to lose. The way we've played in the last three Tests has been outstanding. Some crunch moments we've lost, but we've won more sessions than them. You need a bit of a break. All three Tests were intense. Looks like a good surface. Nice and hard. There's some forecast around for the four-five days. Three changes: Sai Sudharsan comes in place of Karun. Kamboj and Shardul are in as well for Akash Deep and Reddy who are injured.
Ben Stokes: We're going to have a bowl. Decent overhead conditions for bowling. We've had a good break in between. Good chance for everyone to head back home and get the batteries recharged. Everyone left everything out on the field at Lord's. We've had three games go down to the final session, which says a lot about the quality of the teams. Typical Manchester wicket. Quite firm. Some grass. Dawson back in the team - long time since the last Test but he's gone well over the years.
England have won the toss and have opted to field
Pitch report | Michael Atherton: Four championship games and all four have been drawn. Hard to force a result. Groundsman has left grass on the surface. That combined with the overcast conditions, captains may want to bowl first. However, no team has won a Test here after opting to bowl, ever.
10.12am local, 2.42pm IST: "Cap presentation has just happened. Kamboj time!" Kaushik confirms. "Also see Sai in the gully. So that's the other change." Kamboj, a 24-year old seamer from Haryana, played the two unofficial Tests against England Lions as part of the India A squad before this series. What a big day for him.
Clues from warmups: "Seeing Prasidh bowling quite a bit on the side wicket. But it looks like Anshul Kamboj just marked his runup but it's at the other end. So my view is obstructed. Can tell for sure that Shardul Thakur is marking his runup," says Kaushik.
9.55am local, 2.25pm IST: Our correspondent Kaushik Rangarajan greets us with some good news from Old Trafford. "Good morning from Old Trafford. It's hazy and cool but it's not raining. Which means it's a great summers day in Manchester." Peak summer.
England have already named their XI, making just the one change from Lord's. The injured Shoaib Bashir has made way for Liam Dawson who returns to the Test side after eight years. They're far from a settled team, though, with a couple of batters under pressure and in desperate need of a big score. Zak Crawley's flaws have seemed obvious right through the series, and so have Ollie Pope's. However, this pitch might be more to their liking.
India might be trailing 1-2, but they've been the better team across many metrics. It's been an unfortunate pattern with them over the last few years, and the challenge of breaking it is going to be a formidable one with all the injuries in the camp. Akash Deep, Nitish Reddy and Arshdeep Singh have been ruled out, with Anshul Kamboj flown in as a backup seamer. The visitors will be forced to make at least two changes from the previous Test, one of those being a seamer in place of Akash Deep. The other change, for Reddy, is anyone's guess. It also remains to be seen if they stick with both their spin-bowling allrounders in these conditions. There has been a lot of rain in Manchester leading up to the game, and the pitch might not see much sun.
The players gave everything they had at Lord's - mentally, physically and verbally. England didn't have anything left in the tank to celebrate their dramatic win in the final session. In that regard, the break was much needed to recharge the batteries and get going again, and it has served its purpose going by the pressers yesterday. Shubman Gill couldn't even wait for game day to fire his shots.
9.30am local, 2pm IST: After an eight-day break in this hotly contested series, it's time for everyone to warm up again. From a hot and sunny London to a gloomy and possibly wet Manchester. From a slow and wearing pitch to one that's expected to have good pace and bounce. And from an England team with Shoaib Bashir's overspin to an England team without Shoaib Bashir's overspin. Hello and welcome to our coverage of the fourth Test at Old Trafford. Not 10, not 20, but 90 minutes left for play to begin.
England (Playing XI): Zak Crawley, Ben Duckett, Ollie Pope, Joe Root, Harry Brook, Ben Stokes(c), Jamie Smith(w), Liam Dawson, Chris Woakes, Brydon Carse, Jofra Archer
Preview by Kaushik Rangarajan

Old Trafford was unusually quiet two days out from the Test. The air, grey and heavy, carried little of the usual match-week bustle, apart from the players, who at this point of the series, appeared to be operating on autopilot. Outside, in nearby Deansgate, preparations were in motion for Manchester Day, the city's annual burst of parades and performance, set to unfold over the weekend. Inside, though, it was about restraint and restarts, as if both teams were still catching their breath eight days after the storm at Lord's.

After the heat of the last Test - both literal and metaphorical - it fell to Rishabh Pant to lighten the mood when the teams crossed paths for the first time in Manchester. As India wrapped up training, England were just beginning theirs, with Ollie Pope trying to get himself padded up. Walking along the boundary toward the team bus, the Indian vice-captain spotted a stray football. With a gentle swing of his boot, a technique perhaps refined after a recent trip to Manchester United's Carrington training centre, Pant sent the ball skimming along the ground and struck Pope's legs from about 20 yards out. As a startled Pope turned, Pant crouched down in a mock appeal for LBW, much to his own amusement.

After 15 days of high-intensity cricket, this eight-day break couldn't have come at a better time. Both teams have taken on heavy tolls. Ben Stokes emptied himself with two lung-busting spells of nine and 10 overs on that final day at Lord's and stayed true to his claims of not wanting to leave his bed for a few days. Jofra Archer, playing his first Test in four years, didn't wait to get to a bed; he collapsed to the ground, in relief and exhaustion, immediately after that last wicket fell. On the other side, Jasprit Bumrah's workload had stretched beyond his bowling, as he faced 54 pressure-soaked deliveries trying to salvage a lost cause. Each team has lost a player to injury, and each has had to summon for reinforcements.

The mental weight is still harder to measure, but Mohammed Siraj did his best to describe how difficult it had been to move past the image of that final ball, a solid forward defence, middled, yet somehow bowled. Three Tests in, the margins have been both fine and brutal. And so here we are at 2-1, weighing what-ifs that could just as easily have flipped the numbers on the other side of the hyphen.

But after the pause comes the push and Shubman Gill dialled the intensity right back up a day before the game when he invoked 'spirit of cricket' referring to England's time-wasting tactics. The series has shifted back north, not just on the map, but in consequence. The hosts are one win away from sealing the series. India can still win it - for the first time in England since 2007 - but must take both remaining Tests to do so. That's no easy task for a side with just two wins from their last 11 Tests, a stretch defined by inconsistency and transition. But like the skies above Old Trafford, heavy and waiting, the tension hangs thick. The fourth chapter is about to unfold.

When: England vs India, 4th Test, July 23-27 2025, 15:30 IST, 11:00 Local

Where: Old Trafford, Manchester

What to expect: Light rain is forecast over the next five days and some disruptions are likely. The surface has seen big first-innings totals in County games earlier this season, though the last of those came in May. There's been a lot of rain in the lead-up, and with overcast conditions expected, teams may prefer to bowl first, but it comes with a dilemma - no team winning the toss and bowling first has ever won an Old Trafford Test.

Team News:

England

England have confirmed their XI, with Liam Dawson replacing the injured Shoaib Bashir in the only change from Lord's. The 35-year-old Dawson, playing his first Test since 2017, adds left-arm orthodox variety to the attack and adds to the team's batting depth with 18 first-class centuries to his name.

Playing XI: Zak Crawley, Ben Duckett, Ollie Pope, Joe Root, Harry Brook, Ben Stokes (c), Jamie Smith (wk), Chris Woakes, Liam Dawson, Brydon Carse, Jofra Archer

India

The visitors have a few selection calls to make, but Jasprit Bumrah's inclusion is not one of them, almost enforced by the series scoreline. One of them is the third seamer's slot, which is up for grabs, after Akash Deep was ruled out with a groin injury. Gill confirmed that it will be a last-minute toss-up between Prasidh Krishna, who has featured twice this series, and Anshul Kamboj, a recent arrival in the UK. With rain forecast through the Test, India will also weigh the need for a second spinner. And with Nitish Reddy set to make way for a specialist batter - potentially Sai Sudharsan - the bigger question might be whether they can afford to swap the all-round value of Washington Sundar at No. 8 for the seam-bowling heft of Shardul Thakur.

Probable XI: Yashasvi Jaiswal, KL Rahul, Karun Nair, Shubman Gill (c), Rishabh Pant (wk), Sai Sudharsan, Ravindra Jadeja, Washington Sundar/Shardul Thakur, Jasprit Bumrah, Mohammed Siraj, Prasidh Krishna/Anshul Kamboj

Did you know?

- Sachin Tendulkar's maiden Test century is the last individual hundred scored by an Indian at Old Trafford. India have played here just once in the last 30 years.

- Joe Root needs only 120 runs to go past Ricky Ponting's run-tally and into second place in the all-time Test match run charts

- Liam Dawson made his debut in the Chennai Test of 2016, the game in which Karun Nair hit 303*

What they said:

"I don't think it's one of those things where we're going to necessarily just go out and start at it. I don't think either team's really looked to do that. I think there's just always going to be a moment in a Test series where something does heat up. It's a massive series and there's a lot of pressure on both teams to perform. The environment when you're out there, obviously there's going to be some moments and some heat showing." - Ben Stokes, on the needle between teams on the last three days of the Lord's Test.

"It is not ideal when you have to, after every match, kind of have to go back and have a different combination. But it was something that I was prepared before the series that there would be a scenario where I would have to have a different combination for every match. So, I kind of planned it before the series how we are going to go about it." - Shubman Gill on having to change his bowling attack for every game.
Squads:
England Squad: Zak Crawley, Ben Duckett, Ollie Pope, Joe Root, Harry Brook, Ben Stokes(c), Jamie Smith(w), Liam Dawson, Chris Woakes, Brydon Carse, Jofra Archer, Josh Tongue, Gus Atkinson, Jacob Bethell
India Squad: Yashasvi Jaiswal, KL Rahul, Karun Nair, Shubman Gill(c), Rishabh Pant(w), Ravindra Jadeja, Washington Sundar, Anshul Kamboj, Akash Deep, Jasprit Bumrah, Mohammed Siraj, Abhimanyu Easwaran, Kuldeep Yadav, Shardul Thakur, Prasidh Krishna, Sai Sudharsan, Dhruv Jurel"""

# Step 2: Preprocessing
def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words("english"))
    tokens = [t for t in tokens if t not in stop_words]
    return " ".join(tokens)

cleaned_text = preprocess(raw_text)

# Step 3: Bag of Words (Word Frequencies)
bow_vectorizer = CountVectorizer()
bow_matrix = bow_vectorizer.fit_transform([cleaned_text])
bow_df = pd.DataFrame(bow_matrix.toarray(), columns=bow_vectorizer.get_feature_names_out()).T
bow_df.columns = ["Word Frequency"]
bow_df = bow_df.sort_values("Word Frequency", ascending=False)
bow_df.to_csv("bow_frequencies.csv")

# Step 4: TF-IDF
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform([cleaned_text])
tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=tfidf_vectorizer.get_feature_names_out()).T
tfidf_df.columns = ["TF-IDF Score"]
tfidf_df = tfidf_df.sort_values("TF-IDF Score", ascending=False)
tfidf_df.to_csv("tfidf_scores.csv")

# Step 5: Named Entity Recognition
doc = nlp(raw_text)
entities = [(ent.text, ent.label_) for ent in doc.ents]
entities_df = pd.DataFrame(entities, columns=["Entity", "Label"])
entities_df.drop_duplicates().to_csv("named_entities.csv", index=False)

# Step 6: Sentiment Analysis
sia = SentimentIntensityAnalyzer()
sentiment_scores = sia.polarity_scores(raw_text)
pd.DataFrame([sentiment_scores]).to_csv("sentiment_summary.csv", index=False)

# Step 7: Word Cloud
wordcloud = WordCloud(width=1000, height=500, background_color='white').generate(cleaned_text)
plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud from Commentary")
plt.savefig("wordcloud_output.png")
plt.close()

print("✅ All outputs saved: CSVs + word cloud image.")
