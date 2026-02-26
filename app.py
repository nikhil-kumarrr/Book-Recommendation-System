import streamlit as st
import pickle
import pandas as pd
import os

# ----------- PAGE CONFIG -----------
st.set_page_config(
    page_title="AI Book Recommender",
    layout="wide",
)

# ----------- DARK THEME WITH SOFTER SIDEBAR -----------
st.markdown("""
<style>

/* MAIN BACKGROUND */
html, body, .stApp {
    background-color: #000000 !important;
    color: #FFFFFF !important;
}

/* TOP HEADER */
header[data-testid="stHeader"] {
    background-color: #000000 !important;
}

/* TOOLBAR */
div[data-testid="stToolbar"] {
    background-color: #000000 !important;
}

/* SIDEBAR (MORE FADED) */
section[data-testid="stSidebar"] {
    background-color: #141416 !important;
    border-right: 1px solid #1C1C1E;
}

/* TEXT */
h1, h2, h3, h4, p, span, label {
    color: #FFFFFF !important;
}

/* BUTTON */
.stButton>button {
    background-color: #111111;
    color: white;
    border-radius: 8px;
    border: 1px solid #333;
}
.stButton>button:hover {
    background-color: #1f1f1f;
}

/* SELECTBOX */
div[data-baseweb="select"] {
    background-color: #111111 !important;
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

# ----------- HEADER -----------
st.title("AI-Powered Book Recommendation System")
st.write("Discover personalized book suggestions using collaborative filtering.")

# ----------- LOAD FILES -----------
def load_file(file):
    if not os.path.exists(file):
        st.error(f"{file} missing")
        st.stop()
    return pickle.load(open(file, "rb"))

popular_df = load_file("popular.pkl")
pt = load_file("pt.pkl")
books = load_file("books.pkl")
similarity_scores = load_file("similarity_scores.pkl")

# ----------- SIDEBAR -----------
st.sidebar.title("Navigation")
menu = st.sidebar.radio("", ["Popular Books", "Get Recommendations"])

# ----------- POPULAR BOOKS -----------
if menu == "Popular Books":
    st.header("Trending Books")

    cols = st.columns(5)

    for i in range(10):
        with cols[i % 5]:
            st.image(popular_df.iloc[i]['Image-URL-M'])
            st.markdown(f"**{popular_df.iloc[i]['Book-Title']}**")
            st.caption(popular_df.iloc[i]['Book-Author'])

# ----------- RECOMMENDATIONS -----------
if menu == "Get Recommendations":
    st.header("Find Similar Books")

    selected_book = st.selectbox(
        "Choose a book you like",
        pt.index.values
    )

    if st.button("Recommend Books"):
        index = list(pt.index).index(selected_book)

        similar_items = sorted(
            list(enumerate(similarity_scores[index])),
            key=lambda x: x[1],
            reverse=True
        )[1:6]

        st.subheader("Recommended for You")

        cols = st.columns(5)

        for i, item in enumerate(similar_items):
            temp_df = books[books['Book-Title'] == pt.index[item[0]]]

            with cols[i]:
                st.image(
                    temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values[0]
                )
                st.markdown(
                    f"**{temp_df.drop_duplicates('Book-Title')['Book-Title'].values[0]}**"
                )
                st.caption(
                    temp_df.drop_duplicates('Book-Title')['Book-Author'].values[0]
                )