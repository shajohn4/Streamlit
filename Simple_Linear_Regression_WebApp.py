import sys
import os
import streamlit as st
import pickle
import numpy as np
import warnings
warnings.filterwarnings('ignore')

absolute_path = os.path.abspath(__file__)
# print(absolute_path)
file_directory = os.path.dirname(absolute_path)
# print(file_directory)
file_path = os.path.join(
    file_directory, 'linear_regression_model_pickle_Colab')

# print(file_path)
# Reading the model pickle file
with open(file_path, 'rb') as f:
    new_model = pickle.load(f)


def main():
    # Giving Title for our Page
    st.title('Simple Linear Regrssion WebApp')

    # getting input from the user
    House_Median_Age_Var = st.text_input('House Median Age')

    dummy_var = ''

    # Creating a Button on Scren for submission
    if st.button('Predict'):
        # Since the model expects an array to be passed across, converting the scalar value passed by user into matrix/array
        dummy_var = np.array(int(House_Median_Age_Var)).reshape(1, -1)

    # Showing the Predicted value on screen.
    st.success(new_model.predict(dummy_var))


if __name__ == '__main__':
    main()
