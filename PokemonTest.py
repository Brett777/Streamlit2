import pokemontcgsdk as pk
import streamlit as st
from forex_python.converter import CurrencyRates

pk.RestClient.configure('21b4e399-5973-4bf5-b9be-009df2d6b396')

try:
    cardName = st.text_input("Card Name", "Guzzlord")
    cardNumber = st.text_input("Card Number", "116")
    myCard = pk.Card.where(q='name:' + str(cardName) + ' number:' + str(cardNumber))
    st.image(myCard[0].images.small)
    st.write("30 Day Average  $" +str(round(int(myCard[0].cardmarket.prices.avg30)*1.4502,2)))
    st.write("Alltime Average $" +str(round(int(myCard[0].cardmarket.prices.averageSellPrice)*1.4502,2)))
    st.write(str(myCard[0].rarity))
except:
    print("Enter a card name and number.")
