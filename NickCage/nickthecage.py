import pandas as pd
import matplotlib.pyplot as plt
import wordcloud as wc
import streamlit as st

# load dataset
df = pd.read_csv("imdb-movies-dataset.csv")

# data cleaning
df = df.dropna(subset=["Year"])
df["Year"] = df["Year"].astype(int)
df["Votes"] = df["Votes"].fillna("0").str.replace(",", "").astype(int)

# filter by nicolas cage
df_nick_cage = df[df["Cast"].str.contains("Nicolas Cage", na=False)]
# print(df_nick_cage)

# data analysis using streamlit
movies_per_year = df_nick_cage["Year"].value_counts().sort_index()
average_rating_per_year = df_nick_cage.groupby("Year")["Rating"].mean()
genres = df_nick_cage["Genre"].dropna().str.split(", ").explode()
genre_counts = genres.value_counts()
all_reviews = " ".join(df_nick_cage["Review"].dropna())

# Create a set of stopwords
stopwords = set(wc.STOPWORDS)
custom_stopwords = {"Movies", "Film", "story"}
stopwords.update(custom_stopwords)

wordcloud = wc.WordCloud(width=800, height=600, stopwords=stopwords).generate(all_reviews)

#streamlit interface
st.title("Nicolas Cage Filmography")

# Introduction
st.markdown("""
## Introduction
Welcome to the Nicolas Cage Filmography insight page!
**Note**: You can find the [GitHub repository](your_github_repository_link) for this project here.
""")

st.header("Movies per year")
st.bar_chart(movies_per_year)
st.markdown("**Insight**: Did you know? Nicolas Cage has been consistently active in the film industry for almost 60 years, with 8 movies in 2014 alone..!")


st.header("Average ratings per year")
st.line_chart(average_rating_per_year)
st.markdown("**Insight**: On average, Nicolas Cage's movies have seen fluctuating ratings over the years, hitting a lowest score of 2.9 in 1995, and a highest of 7.5 in 2008! He only starred in 1 movie in 2008 though... but let's not hate!")


st.header("Genre")
st.bar_chart(genre_counts)
st.markdown("**Fun Fact**: It's clear that Nicolas Cage loves the thrill of action, drama, and thrillers. Maybe he's just practicing for a real-life escape plan... or a dramatic monologue at the next family dinner!")


st.header("Wordcloud")
st.image(wordcloud.to_array(), use_column_width=True)
st.markdown("**Insight**: The most common words in reviews of Nicolas Cage's movies give us a glimpse into what viewers find most memorable about his performances.")



