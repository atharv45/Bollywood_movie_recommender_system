import pandas as pd
import numpy as np
import streamlit as st
import pickle


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True, key= lambda x:x[1])[1:6]

    movie_name = []
    poster_path = []

    for i in movie_list:
        movie_name.append(movies.iloc[i[0]].title)
        poster_path.append(movies.iloc[i[0]].poster_path)
    return movie_name,poster_path


movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

st.title(':blue[Bollywood Recommender System]')
# :sunglasses:

selected_movie = st.selectbox(
    'Select a movie',
    movies['title'].values)
st.write('You selected:', selected_movie)


if st.button('Recommend',type='primary'):
    names, posters = recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])










































