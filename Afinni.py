import pandas as pd
import streamlit as st
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
import pypickle

#load the model
loaded_model = pypickle.load('Afinni_chun.pkl')


#create a function that called prediction that will take in cfunctions entered by the users

def prediction(data):
    
 #create a dataframe for the data
    df=pd.DataFrame(data)

#convert the categorical columns to numerical
    label = LabelEncoder()
# create a list of the categorical colum
    cat_cols = [0,1,2,14,16]

    for i in cat_cols:
        df.iloc[i] = label.fit_transform(df.iloc[i])

#create a variable that will convert the data to a numpy array
    num_data = df. drop([0, 11, 12, 13]).values.reshape(1,-1)

#predicting the model
    pred = loaded_model.predict(num_data)

    if pred[0] == 0:
        return "The client will not CHURN"
    else:
        return "The client will CHURN"
    

def main():
    st.title("Expresso Churn Prediction Model")
    user_id = st.number_input("Please enter your ID no: ")
    REGION = st.text_input("Please enter your region: ")
    TENURE  = st.radio("Please select your tenure: ", ( '9-12 months', '12-15 months', '15-18 months', '18-21 months', '21 -24 months', '> 24 months'))
    MONTANT = st.number_input("Please enter your top-up amount: ")
    FREQUENCE_RECH = st.number_input("Please enter the number of times you refilled: ")
    REVENUE = st.number_input("How much do you earn monthly?: ")
    ARPU_SEGMENT = st.number_input("Please enter your income over 90days/3: ")
    FREQUENCE = st.number_input("Please enter the number of times you made an income: ")
    DATA_VOLUME = st.number_input("Please enter the number of connections: ")
    ON_NET = st.number_input ("How many inter Expresso calls did you make? ")
    ORANGE = st.number_input ("How many calls did you make to Orange: ")
    TIGO = st.number_input ("How many calls did you make to Tigo: ")
    ZONE1 = st.number_input ("How many calls did you make to zonw 1: ")
    ZONE2 = st.number_input ("How many calls did you make to zonw 2: ")
    MRG = st.radio("Are you going? select yes or no ", ("yes" , "no"))
    REGULARITY = st.number_input("Please enter the number of times you have been active in the last 90 days: ")
    TOP_PACK = st.text_input("Please enter your most active packs")
    FREQ_TOP_PACK =st.number_input("Please enter the number of times you acivated the top-up package: ")

    CHURN  = ""

    if st.button("Result"):
        CHURN = prediction([user_id, REGION, TENURE, MONTANT, FREQUENCE_RECH, REVENUE, ARPU_SEGMENT, FREQUENCE, DATA_VOLUME,
        ON_NET, ORANGE, TIGO, ZONE1, ZONE2, MRG, REGULARITY, TOP_PACK, FREQ_TOP_PACK])
    st.success(CHURN)
if  __name__ == "__main__":
            main() 

    

