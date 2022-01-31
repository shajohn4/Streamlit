import sys
import streamlit as st
import pickle
import numpy as np
import warnings
warnings.filterwarnings('ignore')


# Reading the model pickle file
with open('C:/Shaji/Python_Practice/Stream_Lit_Model_Linear_Regression/linear_regression_model_pickle_Colab', 'rb') as f:
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
