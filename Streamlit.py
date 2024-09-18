import streamlit as st
from streamlit_login_auth_ui.widgets import __login__


st.title("Tågbiljet")
st.header("Programmen räknar ut biljet priset beroende på ålder")

Saldo = 0
Saldo = st.number_input("Hur mycket pengar vill du sätta in? ")

UppSaldo = Saldo
Biljet_pris = 0

Ålder = st.slider("Ålder?",min_value=0,max_value=66)
st.write(f"Saldo", Saldo)
if st.button("Köp"):
    if Ålder <= 18:
        Biljet_pris = 130
        st.write(Biljet_pris)
        Saldo = Saldo-Biljet_pris

    elif Ålder > 18 and Ålder < 64:
        Biljet_pris = 230
        st.write(230)
        Saldo = Saldo-Biljet_pris


    elif Ålder >= 65:
        Biljet_Pris = 100
        st.write(100)
        Saldo = Saldo-Biljet_Pris
    
    else: st.write(f"Du har inte tillräcklig pengar{Saldo-Ålder}")
    
    st.write(f"Ditt saldo {Saldo}")
    st.write(f"Transaktion lyckades {Ålder} års Biljet ")
