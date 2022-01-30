import sys
import streamlit as st
# +

# Write a page title
st.title('Hello Chris. I am Christopher Columbus')
# Subheader
st.subheader('I like animals and one pet')

# Text
st.text('All my friends have a pet.I also want a pet so that I can play with it.But my mummy "Pushpa" is very scared of pet. she is not getting me a dog')
# Using st.write

st.radio('Choose your option', options=('Option 1', 'Option 2', 'Option 3'))

# Slider
st.slider('<-- Slide to the sides -->', min_value=0,
          max_value=10, value=5, step=1)

# Multiselect
st.text('Checkbox')
st.multiselect('What are your favorite colors',
               ['Green', 'Yellow', 'Red', 'Blue'],
               ['Blue', 'Green'])  # pre-selected


# Selectbox
st.selectbox('Select Box', options=('Option 1', 'Option 2', 'Option 3'))

# text input
title = st.text_input('My App Text Input', 'Write Something...')
st.write('You wrote:  ', title)

# Adding a text in the sidebar
st.sidebar.text('Your Text Here')
# Add a radio button
st.sidebar.radio('label', options=[])
# The other gadgets follow the same syntax.
