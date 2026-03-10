import streamlit as st
import pickle
import pandas as pd
import sklearn as sk
import requests
from urllib.parse import  quote


book=pickle.load(open('movies.pkl','rb'))
model=pickle.load(open('model.pkl','rb'))
vectors=pickle.load(open('vectors.pkl','rb'))


@st.cache_data
def poster(title):
    search_title=quote(title[:50])
    url= book[book['title']==title['img'].values[0]]
    data= requests.get(url).json()
    try:

        response = requests.get(url, timeout=5)
        data = response.json()

        if 'items' in data:

            volume_info = data['items'][0].get('volumeInfo', {})
            image_links = volume_info.get('imageLinks', {})
            cover = image_links.get('thumbnail')

            if cover:
                return cover.replace("http://", "https://")
    except Exception as e:
        print(f"Error for {title}: {e}")


    return "https://placehold.co/128x195?text=No+Cover"





def recom(bk_title):
    indx = book[book['title'].str.contains(bk_title, case=False)].index[0]
    distance, indices = model.kneighbors(vectors[indx], n_neighbors=6)
    recomnd_book=[]
    book_cover=[]
    for i in indices[0][1:]:
        recomnd_book.append(book.iloc[i].title)
        book_cover.append(poster(book.iloc[i].title))

    return recomnd_book,book_cover


book_list=book['title'].values

st.title('Book Recommender System')

slect_book=st.selectbox("Select a book",book_list)

if st.button("Recommend"):
    recommendation,covers=recom(slect_book)
    cols=st.columns(5)
    for i in range(5):
        with cols[i]:
            img_url=poster(recommendation[i])
            st.image(img_url)
            st.text(recommendation[i])


