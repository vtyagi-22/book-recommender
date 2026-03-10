import streamlit as st
import pickle
import pandas as pd
import sklearn as sk
import requests




book=pickle.load(open('movies.pkl','rb'))
model=pickle.load(open('model.pkl','rb'))
vectors=pickle.load(open('vectors.pkl','rb'))

def poster(title):
    url=  f"https://www.googleapis.com/books/v1/volumes?q={title}"
    data= requests.get(url).json()
    try:
         cover=data['items'][0]['volumeInfo']['imageLinks']['thumbnail']
    except:
         cover="https://via.placeholder.com/128x195.png?text=No+Cover"
    return cover





def recom(bk_title):
    indx = book[book['title'].str.contains(bk_title, case=False)].index[0]
    distance, indices = model.kneighbors(vectors[indx], n_neighbors=6)
    recomnd_book=[]
    book_cover=[]
    for i in indices[0][1:]:
        recomnd_book.append(book.iloc[i].title)
        url = book.iloc[i].image_url_l
        url = url.replace("http://", "https://")

        book_cover.append(url)

    return recomnd_book,book_cover


book_list=book['title'].values

st.title('Book Recommender System')

slect_book=st.selectbox("Select a book",book_list)

if st.button("Recommend"):
    recommendation,covers=recom(slect_book)
    cols=st.columns(5)
    for i in range(5):
        with cols[i]:
            st.image(covers[i])
            st.write(recommendation[i])


