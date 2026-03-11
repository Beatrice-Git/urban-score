import streamlit as st
import pandas as pd
from pathlib import Path
from final_project_package.embeddings.embeddings import load_clip_model, get_text_embeddings, similarity

@st.cache_data
def get_clip():
    return load_clip_model()

@st.cache_data
def get_images():
    return pd.read_csv(Path.cwd() / "data_dump/images_cleaned_embedding.csv")

@st.cache_data
def get_listings():
    return pd.read_csv(Path.cwd() / "data_dump/listings_with_scores.csv")

model, processor = get_clip()
images_df = get_images()
listings_df = get_listings()

'''
# UrbanScore
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Please enter the parameters of the search
'''

query = st.text_input("Image Query", value="skandenavian kitchen")

variable = st.selectbox("Variable", listings_df.columns, value="Square Meters")

min_value = st.number_input("Minimum value of Variable", min_value=0.0, max_value=100000000.0, value=0.0, step=0.1)

text_embedding = get_text_embeddings(model, processor, [query])

similarity = 0.1

df = pd.DataFrame({
    "lon": listings_df["longitude"],
    "lat": listings_df["latitude"]
})

st.map(df)


'''
## Predicted fare for this ride

'''

#@st.cache_data


st.write("Similarity: ", similarity)
