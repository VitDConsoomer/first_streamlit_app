import streamlit
import pandas

streamlit.title("Who knows how Magnets work? A story of the 1964 Harlem riots")
streamlit.header('A story in three parts')
streamlit.text('Part one: Discovering Magnetism and gravity')
streamlit.text('Part two: Siphoning gas')
streamlit.text('Part three: Magnetic gas siphons and the impact of the 1972 oil crisis')

streamlit.header('And now, a list of fruits:')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
