import streamlit as st
import pandas as pd
import numpy as np
import pickle
import base64
import warnings
warnings.filterwarnings('ignore')
st.set_page_config(layout='wide')


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
        unsafe_allow_html=True
    )
add_bg_from_local('Images/bg1.jpg')

head1,head2,head3=st.columns([1.5,2,1])
with head2:
    st.markdown("<h2 style= 'color: #07A9F3;font-size: 46px;font-family:Arial ;font-weight: bold;'> <strong>Car Price Prediction</strong></h2>", unsafe_allow_html=True)

st.markdown('#')

pipe=pickle.load(open('pipe.pkl','rb'))
df=pickle.load(open('df.pkl','rb'))
df['CarName']=df['CarName'].str.title()


col0,col1,col2,col3,col4=st.columns([0.5,1.5,2,1.5,0.5])
with col1:
    st.markdown("<h2 style= 'color: white;font-size: 22px;'>Enter the Car Name</h2>", unsafe_allow_html=True)
    carname=st.selectbox('',df['CarName'].unique())
    carname=carname.lower()
    st.markdown("<h2 style= 'color: white;font-size: 22px;'>Enter the Car Body</h2>", unsafe_allow_html=True)
    carbody=st.selectbox('',df['carbody'].unique())
    st.markdown("<h2 style= 'color: white;font-size: 22px;'>Enter the Drive Wheel</h2>", unsafe_allow_html=True)
    drivewheel=st.selectbox('',['rwd','fwd','4wd'])
    st.markdown("<h2 style= 'color: white;font-size: 22px;'>Enter the Engine Location</h2>", unsafe_allow_html=True)
    engloc=st.selectbox('',['front','rear'])
    st.markdown("<h2 style= 'color: white;font-size: 22px;'>Select the Fuel Type</h2>", unsafe_allow_html=True)
    fueltype=st.selectbox('',['gas','diesel'])
    st.markdown("<h2 style= 'color: white;font-size: 22px;'>Enter the Aspiration</h2>", unsafe_allow_html=True)
    aspiration=st.selectbox('',['std','turbo'])
    st.markdown("<h2 style= 'color: white;font-size: 22px;'>Enter the Door Number</h2>", unsafe_allow_html=True)
    doornumber=st.selectbox('',['two','four'])
    st.markdown("<h2 style= 'color: white;font-size: 22px;'>Enter the Cylinder Number</h2>", unsafe_allow_html=True)
    cylindernum=st.selectbox('',df['cylindernumber'].unique())
    st.markdown("<h2 style= 'color: white;font-size: 22px;'>Enter the Engine Type</h2>", unsafe_allow_html=True)
    engtype=st.selectbox('',df['enginetype'].unique())
    st.markdown("<h2 style= 'color: white;font-size: 22px;'>Enter the Fuel System</h2>", unsafe_allow_html=True)
    fuelsystem=st.selectbox(' ',df['fuelsystem'].unique())
    st.markdown("<h2 style= 'color: white;font-size: 22px;'>Enter the Symboling</h2>", unsafe_allow_html=True)
    symbol=st.number_input('',min_value=0)
    st.markdown("<h2 style= 'color: white;font-size: 22px;'>Enter the Wheel Base</h2>", unsafe_allow_html=True)
    wheelbase=st.number_input('',min_value=30.0)
with col3:
    st.markdown("<h2 style= 'color: white;font-size: 22px;'>Enter the Car Length</h2>", unsafe_allow_html=True)
    carlength=st.number_input('',min_value=130.0)
    st.markdown("<h2 style= 'color: white;font-size: 22px;'>Enter the Car Width</h2>", unsafe_allow_html=True)
    carwidth=st.number_input('',min_value=20.0)
    st.markdown("<h2 style= 'color: white;font-size: 22px;'>Enter the Car Height</h2>", unsafe_allow_html=True)
    carheight=st.number_input(' ',min_value=10.0)
    st.markdown("<h2 style= 'color: white;font-size: 22px;'>Enter the Curb Weight</h2>", unsafe_allow_html=True)
    curbweight=st.number_input('',min_value=1000)
    st.markdown("<h2 style= 'color: white;font-size: 22px;'>Enter the Engine Size</h2>", unsafe_allow_html=True)
    engsize=st.number_input('',min_value=40)
    st.markdown("<h2 style= 'color: white;font-size: 22px;'>Enter the Bore Ratio</h2>", unsafe_allow_html=True)
    boreratio=st.number_input('')
    st.markdown("<h2 style= 'color: white;font-size: 22px;'>Enter the Stroke</h2>", unsafe_allow_html=True)
    stroke=st.number_input('',min_value=0.5)
    st.markdown("<h2 style= 'color: white;font-size: 22px;'>Enter the Compression Ratio</h2>", unsafe_allow_html=True)
    compratio=st.number_input(' ',min_value=1)
    st.markdown("<h2 style= 'color: white;font-size: 22px;'>Enter the Horse Power</h2>", unsafe_allow_html=True)
    horsepow=st.number_input('',min_value=30)
    st.markdown("<h2 style= 'color: white;font-size: 22px;'>Enter the Peak RPM</h2>", unsafe_allow_html=True)
    peakrpm=st.number_input('',min_value=2000)
    st.markdown("<h2 style= 'color: white;font-size: 22px;'>Enter the City MPG</h2>", unsafe_allow_html=True)
    citympg=st.number_input('',min_value=8)
    st.markdown("<h2 style= 'color: white;font-size: 22px;'>Enter the Highway MPG</h2>", unsafe_allow_html=True)
    highwaympg=st.number_input('',min_value=10)


    def encdrive(drivewheel):
        if drivewheel=='rwd':
            return 0
        elif drivewheel=='fwd':
            return 1
        elif drivewheel=='4wd':
            return 2
    def encengloc(value):
        if value=='front':
            return 0
        elif value=='rear':
            return 1
    def encfueltype(type):
        if type=='gas':
            return 0
        elif type=='diesel':
            return 1
    def encasp(asp):
        if asp=='std':
            return 0
        elif asp=='turbo':
            return 1
    def encdoor(dnum):
        if dnum=='two':
            return 0
        elif dnum=='four':
            return 1

drivewheel=encdrive(drivewheel)
engloc=encengloc(engloc)
fueltype=encfueltype(fueltype)
aspiration=encasp(aspiration)
doornumber=encdoor(doornumber)
st.markdown('#')
st.markdown('#')
st.markdown('#')
btn1,btn2,btn3=st.columns([2.5,1,2])
with btn2:
    predictbtn=st.button('Predict')
if predictbtn==True:
    values = [carname, carbody, drivewheel, engloc, fueltype, aspiration, doornumber, cylindernum, engtype, fuelsystem,
              symbol, wheelbase,
              carlength, carwidth, carheight, curbweight, engsize, boreratio, stroke, compratio, horsepow, peakrpm,
              citympg, highwaympg]
    result=pipe.predict([values])
    res1,res2,res3=st.columns([1.8,2,1])
    with res2:
        st.markdown('#')
        st.markdown("<h2 style= 'color: white;font-size: 44px;'>{} Price - ${}</h2>".format(carname.title(),round(result[0])), unsafe_allow_html=True)
