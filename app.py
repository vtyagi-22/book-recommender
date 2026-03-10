import streamlit as st
import pickle
import pandas as pd

# Load files
# Ensure movies.pkl contains the 'title' and 'img' columns
book = pickle.load(open('movies.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))
vectors = pickle.load(open('vectors.pkl', 'rb'))
bk=pickle.load(open('bk.pkl', 'rb'))


@st.cache_data
def get_poster(title):
    try:
        # Find the URL in the 'img' column for the matching title
        # We use .iloc[0] to get the actual string value
        url = bk[bk['title'] == title]['img'].values[0]

        # Streamlit Cloud requires HTTPS
        if isinstance(url, str):
            return url.replace("http://", "https://")
    except Exception:
        pass
    # Fallback placeholder if URL is missing or broken
    return "https://placehold.co/128x195?text=No+Cover"


def recom(bk_title):
    # Find index of the book
    indx = book[book['title'].str.contains(bk_title, case=False)].index[0]
    distance, indices = model.kneighbors(vectors[indx], n_neighbors=6)

    recomnd_book = []
    book_cover = []

    for i in indices[0][1:]:
        title = book.iloc[i].title
        recomnd_book.append(title)
        # Fetch the cover URL directly from our function
        book_cover.append(get_poster(title))

    return recomnd_book, book_cover


# UI Code
st.title('Book Recommender System')

book_list = book['title'].values
slect_book = st.selectbox("Select a book", book_list)

if st.button("Recommend"):
    recommendation, covers = recom(slect_book)

    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            # Use the covers list returned by recom()
            st.image(covers[i])
            st.text(recommendation[i])