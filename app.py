import streamlit as st
import pickle
import pandas as pd


book = pickle.load(open('book.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))
vectors = pickle.load(open('vectors.pkl', 'rb'))
bk=pickle.load(open('bk.pkl', 'rb'))


@st.cache_data
def get_poster(title):
    try:

        url = bk[bk['title'] == title]['img'].values[0]


        if isinstance(url, str):
            return url.replace("http://", "https://")
    except Exception:
        pass

    return "https://placehold.co/128x195?text=No+Cover"


def recom(bk_title):

    indx = book[book['title'].str.contains(bk_title, case=False)].index[0]
    distance, indices = model.kneighbors(vectors[indx], n_neighbors=6)

    recomnd_book = []
    book_cover = []

    for i in indices[0][1:]:
        title = book.iloc[i].title
        recomnd_book.append(title)

        book_cover.append(get_poster(title))

    return recomnd_book, book_cover



st.title('Book Recommender System')

book_list = book['title'].values
slect_book = st.selectbox("Select a book", book_list)

if st.button("Recommend"):
    recommendation, covers = recom(slect_book)

    cols = st.columns(5)
    for i in range(5):
        with cols[i]:

            st.image(covers[i])
            st.text(recommendation[i])