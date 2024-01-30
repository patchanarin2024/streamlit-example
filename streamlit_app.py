import streamlit as st
import pandas as pd
import plotly.express as px
import re

st.set_page_config(page_title=" CEHCK CARD", page_icon=":bar_chart:", layout="wide")


def convert_google_sheet_url(url):
    # Regular expression to match and capture the necessary part of the URL
    pattern = r'https://docs\.google\.com/spreadsheets/d/([a-zA-Z0-9-_]+)(/edit#gid=(\d+)|/edit.*)?'

    # Replace function to construct the new URL for CSV export
    # If gid is present in the URL, it includes it in the export URL, otherwise, it's omitted
    replacement = lambda m: f'https://docs.google.com/spreadsheets/d/{m.group(1)}/export?' + (f'gid={m.group(3)}&' if m.group(3) else '') + 'format=csv'

    # Replace using regex
    new_url = re.sub(pattern, replacement, url)

    return new_url


# Replace with your modified URL
url = 'https://docs.google.com/spreadsheets/d/1ED8Mj5bY629NlTNvAOQXoVkSDHVKYnLwyTpzXaSLJ60/edit#gid=0'

new_url = convert_google_sheet_url(url)


df = pd.read_csv(new_url)


st.sidebar.header("Please Filter Here:")
tent = st.sidebar.multiselect(
    "Select the Tent:",
    options=df["Tent"].unique()
    
)

df_selection = df.query(
    "Tent == @tent"
)

total  = int(df_selection["card_code"].sum())

st.title(f"Total   {total:,}")


custom_css = """
    .centered-header th {
        text-align: center;
    }
    
    .centered-text td {
        text-align: center;
    }
"""

st.write(f"<style>{custom_css}</style>", unsafe_allow_html=True)
st.write(df_selection.to_html(classes=["centered-header", "centered-text"],index=False, escape=False), unsafe_allow_html=True)



 

st.markdown("""---""")

