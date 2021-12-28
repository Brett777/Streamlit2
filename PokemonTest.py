import pokemontcgsdk as pk
import streamlit as st

pk.RestClient.configure('21b4e399-5973-4bf5-b9be-009df2d6b396')

myCard = pk.Card.where(q='name:Guzzlord number:116')


myCard[0].cardmarket.prices.averageSellPrice


st.write("This is a Pokemon Card")
st.write("It is worth: " +str(myCard[0].cardmarket.prices.averageSellPrice))