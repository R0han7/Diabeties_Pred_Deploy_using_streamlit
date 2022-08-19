import numpy as np
import pickle
import streamlit as st

filename = r"C:/Users/91931/Downloads/trained.sav"
loaded_model = pickle.load(open(filename, 'rb'))


def predicti(input_data):
    input_data = np.array(input_data).reshape(1, -1)
    pred = loaded_model.predict(input_data)
    if pred[0] == 0:
        return ("not diabetic")
    else:
        return ('diabetic')


def main():
    st.title('Diabeties PRed')

    pregnancies = st.text_input('No of Pregnencies')
    glucose = st.text_input('Glucose level')
    bp = st.text_input('BP level')
    skinthickness = st.text_input('Skin Thcikness')
    insulin = st.text_input('Insulin level')
    bmi = st.text_input('BMI')
    diabetiesfn = st.text_input('Diabepregifn')
    age = st.text_input('Age')

    diagnosis = ''
    if st.button("Daibeties Test result"):
        diagnosis = predicti([preg, glu, bp, skinth, insu, bmi, diabefn, age])
    st.success(diagnosis)


if __name__ == '__main__':
    main()
