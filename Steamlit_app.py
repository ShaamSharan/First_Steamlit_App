import streamlit
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page.
streamlit.dataframe(fruits_to_show)
streamlit.title('Hi my 1st Python program')
streamlit.header(' Hi my 1st Python program Header')

streamlit.text('🥣 🐔 🍞Hi my 1st Python program Text1')

streamlit.text('🥗Hi my 1st Python program Text2')
streamlit.text('🥑Hi my 1st Python program Text3')

streamlit.header("Fruityvice Fruit Advice!")
import requests
# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
# streamlit.text(fruityvice_response.json())

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/kiwi")
fruityvice.normalize=pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice.normalize)


# write your own comment -what does the next line do? 
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
#streamlit.dataframe(fruityvice_normalized)
