import numpy as np
import pickle
import pandas as pd
import streamlit as st
from sklearn.preprocessing import StandardScaler
from PIL import Image
pickle_in = open("clustering_model.pkl","rb")
model=pickle.load(pickle_in)
def predict_label(a,s,d):
    data = pd.read_csv('road-accidents.csv', comment='#', sep='|')
    X = data.drop(['state', 'drvr_fatl_col_bmiles'], axis=1)
    scaler = StandardScaler()
    X.loc[-1]=[a,s,d]
    X_scaled = scaler.fit_transform(X)
    prediction = model.predict([X_scaled[-1]])
    print(prediction)
    return prediction
def main():
    st.title("Reducing Traffic Mortality")
    sp=st.slider('Percent of drivers involved in fatal collision who were speeding',0,100)
    al=st.slider('Percent of drivers involved in fatal collision who were Alcohol Impaired',0,100)
    pr=st.slider('Percent of drivers involved in fatal collision who had not been involved in any previous accident',0,100)
    result=[]
    if st.button("Predict the cluster for above data"):
        result = predict_label(sp,al,pr)
        st.success('Cluster {}'.format(result[0]))
    st.text("Developed by: Mohammad Tariq")
    
if __name__ == '__main__':
    main()
