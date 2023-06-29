import streamlit as st
from streamlit_chat import message
# To Create the Interface

from bardapi import Bard
# To Use Generative Model Bard

import pickle
# To extract Token number from a bin file


# Generate Response from the User
def generate_response(prompt):
    with open('Bard_token.bin', 'rb') as file:
        token = pickle.load(file)

    # Bard Initialization
    Bard_Model = Bard(token=token)

    # Ask Question and Return Response
    return Bard_Model.get_answer(prompt)['content']

# Recieve Request from the User
def get_text():
    input_text = st.text_input("Welcome ! I'm Kasper. How can I help you ?", "", key='input')
    return input_text

# Title
st.title('Personal Tutoring Bot')

# Changing the GUI of the StreamLit App
changes = '''
<style>
[data-testid = "stAppViewContainer"]
{
    background-image: url('https://images.pexels.com/photos/378277/pexels-photo-378277.jpeg');
    background-size: cover;
}

div.esravye2 > iframe 
{
    background-color: transparent;
}
</style>
'''
# Apply Changes
st.markdown(changes, unsafe_allow_html=True)

print(st.session_state)

# States Initialization
if 'generated_response' not in st.session_state:
    st.session_state['generated_response'] = []
if 'user_questions' not in st.session_state:
    st.session_state['user_questions'] = []

user_input = get_text()
if user_input:
    #print(user_input)
    response = generate_response(user_input)
    #print(response)

    st.session_state['user_questions'].append(user_input)
    st.session_state['generated_response'].append(response)

if st.session_state['generated_response']:
    for i in range(len(st.session_state['generated_response'])-1, -1, -1):
        message(st.session_state['generated_response'][i], key="A"+str(i))
        message(st.session_state['user_questions'][i], key="B"+str(i), is_user=True)



