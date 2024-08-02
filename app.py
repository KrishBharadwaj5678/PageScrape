import streamlit as st
import requests

st.set_page_config(
    page_title="Web Scraper",
    page_icon="icon.png",
    menu_items={
        "About":"PageScrape allows you to enter any website URL and instantly retrieve the HTML code, complete with a download option."
    }
)

st.write("<h2 style='color:#EA632A';>Retrieve HTML Code from Any URL</h2>",unsafe_allow_html=True)

url=st.text_input("Enter website url",placeholder="https://www.google.com")
btn=st.button("Extract")

if "load_state" not in st.session_state:
    st.session_state.load_state=False

if btn or st.session_state.load_state:
    st.session_state.load_state=True
    try:
        url=requests.get(url)
        content=url.content
        st.download_button("Download File",content,"scraper.html")

        with open("scraper.html","wb+") as file:
            file.write(content)

        with open("scraper.html","r",encoding='utf-8') as file:
            st.code(file.read())
    except:
        st.warning("URL Not Found")
