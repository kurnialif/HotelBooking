import numpy as np
import pandas as pd
import streamlit as st 
import joblib

classifier=joblib.load('Hotel Prediction model.pkl')


def welcome():
    return "Welcome All"


def predict_hotel(hotel,lead_time,stays_in_weekend_nights,stays_in_week_nights,market_segment,distribution_channel,is_repeated_guest,previous_cancellations,previous_bookings_not_canceled,reserved_room_type,booking_changes,deposit_type,customer_type,total_of_special_requests,Total_Guests,Seasons,Total_Days):
    prediction=classifier.predict(pd.DataFrame({'hotel':[hotel],'lead_time':[lead_time],'stays_in_weekend_nights':[stays_in_weekend_nights],'stays_in_week_nights':[stays_in_week_nights],'market_segment':[market_segment],'distribution_channel':[distribution_channel],'is_repeated_guest':[is_repeated_guest],'previous_cancellations':[previous_cancellations],'previous_bookings_not_canceled':[previous_bookings_not_canceled],'reserved_room_type':[reserved_room_type],'booking_changes':[booking_changes],'deposit_type':[deposit_type],'customer_type':[customer_type],'total_of_special_requests':[total_of_special_requests],'Total_Guests':[Total_Guests],'Seasons':[Seasons],'Total_Days':[Total_Days]}))
    print(prediction)
    label = ['Canceled','Check-Out',]
    return label[prediction[0]]
  
      
def main():
    st.title("Hotel")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Hotel ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    hotel = st.text_input("Hotel")
    lead_time = st.text_input("Lead Time")
    stays_in_weekend_nights = st.text_input("Stays In weekend Nights")
    stays_in_week_nights = st.text_input("Stays In Week Nights")
    market_segment = st.text_input("Market Segment")
    distribution_channel = st.text_input("Distribution Channel")
    is_repeated_guest = st.text_input("Is Repeated Guest (Ex,0 or 1)")
    previous_cancellations = st.text_input("Previous Cancellations")
    previous_bookings_not_canceled = st.text_input("Previous Bookings Not Canceled")
    reserved_room_type = st.text_input("Reserved Room Type")
    booking_changes = st.text_input("Booking Changes")
    deposit_type = st.text_input("Deposit Type")
    customer_type = st.text_input("Customer Type")
    total_of_special_requests = st.text_input("Total Of Special Requests")
    Total_Guests = st.text_input("Total Guests")
    Seasons = st.text_input("Season")
    Total_Days = st.text_input("Total Days")
    result=""
    if st.button("Predict"):
        result=predict_hotel(hotel,lead_time,stays_in_weekend_nights,stays_in_week_nights,market_segment,distribution_channel,is_repeated_guest,previous_cancellations,previous_bookings_not_canceled,reserved_room_type,booking_changes,deposit_type,customer_type,total_of_special_requests,Total_Guests,Seasons,Total_Days)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Cancellation Predection Model")
        st.text("Built with Streamlit")
if __name__=='__main__':
    main()        
