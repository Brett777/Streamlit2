import pokemontcgsdk as pk
import streamlit as st
pk.RestClient.configure('21b4e399-5973-4bf5-b9be-009df2d6b396')

cardName = st.text_input("Card Name", "Guzzlord")
cardNumber = st.text_input("Card Number", "116")

myCard = pk.Card.where(q='name:' + cardName + 'number:' + cardNumber)


st.write("This is a Pokemon Card")
st.write("It is worth: " +str(myCard[0].cardmarket.prices.averageSellPrice))