import streamlit as st
import datetime
import requests
import pandas as pd
import numpy as np
#pickup_date = st.date_input(“Date and time”, datetime.date(2019, 7, 6))
#pickup_time = st.time_input(‘Time’, datetime.time(8, 45))
#pickup_datetime = str(pickup_date) +' ’+ str(pickup_time)
#pickup_longitude = st.number_input(‘pickup longitude’, -73.941)
#pickup_latitude = st.number_input(‘pickup latitude’, 40.711)
#dropoff_longitude = st.number_input(‘dropoff longitude’,-74.100)
#dropoff_latitude = st.number_input(‘dropoff latitude’, 40.711)
#passenger_count = st.number_input(‘passenger count’)
columns = st.columns(3)
pickup_date = columns[0].date_input('Date',datetime.date(2019, 7, 6))
columns[0].write('')
pickup_time = columns[1].time_input('Time', datetime.time(8, 45))
columns[1].write('')
passenger_count = columns[2].number_input('Number of passenger', 1)
columns[2].write('')
passenger_count = int(passenger_count)
pickup_datetime = str(pickup_date) + ' ' + str(pickup_time)
columns = st.columns(4)
pickup_latitude = columns[0].number_input('pickup latitude', 40.711)
columns[0].write('')
pickup_longitude = columns[1].number_input('pickup longitude', -74.100)
columns[1].write('')#
dropoff_latitude = columns[2].number_input('dropoff latitude', 40.711)
columns[2].write('')
dropoff_longitude = columns[3].number_input('dropoff longitude', -74.100)
columns[3].write('')
def get_map_data():
    return pd.DataFrame([[pickup_latitude, pickup_longitude],
                         [dropoff_latitude, dropoff_longitude]],
                        columns=['lat', 'lon'])
df = get_map_data()
st.map(df)
print(pickup_datetime)
url = 'https://taxifare.lewagon.ai/predict'
X = {
  #  “key”: [“2013-07-06 17:18:00.000000119"],
    'pickup_datetime': pickup_datetime,
    'pickup_longitude': pickup_longitude,
    'pickup_latitude': pickup_latitude,
    'dropoff_longitude': dropoff_longitude,
    'dropoff_latitude': dropoff_latitude,
    'passenger_count': passenger_count
}
params = X
if st.button('Estimation'):
    # print is visible in the server output, not in the page
    request = requests.get(url, params).json()
    st.balloons()
    st.write('Prix')
    st.write('$', str(request['prediction']))
else:
    st.write('Estimation')
