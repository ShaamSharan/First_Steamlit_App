
import pandas
streamlit.title('Hi my 1st Python program')
streamlit.header(' Hi my 1st Python program Header')

streamlit.text('🥣 🐔 🍞Hi my 1st Python program Text1')

streamlit.text('🥗Hi my 1st Python program Text2')
streamlit.text('🥑Hi my 1st Python program Text3')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
