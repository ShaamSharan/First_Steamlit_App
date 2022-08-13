import streamlit
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)
streamlit.title('Hi my 1st Python program')
streamlit.header(' Hi my 1st Python program Header')

streamlit.text('🥣 🐔 🍞Hi my 1st Python program Text1')

streamlit.text('🥗Hi my 1st Python program Text2')
streamlit.text('🥑Hi my 1st Python program Text3')
