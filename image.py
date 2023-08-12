import streamlit as st
from PIL import Image
import requests
from io import BytesIO
import yfinance as yf
def main():
    try:
        newsc=st.text_input('Enter a Company')
        stocknews=yf.Ticker(newsc)
        
        st.title(f":blue[Trending News]")
        i=0
        j=0
        for new in stocknews.news:
            st.write()
            st.subheader(stocknews.news[i]['title'])
            image_url=stocknews.news[i]['thumbnail']['resolutions'][0]['url']
            try:
                response = requests.get(image_url)
                img = Image.open(BytesIO(response.content))
                st.image(img, caption=stocknews.news[i]['publisher'], use_column_width=True)
            except Exception as e:
                st.error("Error loading the image. Please check the URL and try again.")
            st.write()
                
            st.write(stocknews.news[i]['link'])
            i=i+1
        st.write(stocknews.actions)
    except:
        st.write('Thank you')

        
if __name__ == "__main__":
    main()