import streamlit
streamlit.title ('My parents New Healthy Dinner')
streamlit.header ('Breakfast Menu')
streamlit.text ('Omega 3 & Blueberry oatmeal')
streamlit.text ('Kale, spinach & Rocket Smoothie ')
streamlit.text ('Hard bolied free-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

                

