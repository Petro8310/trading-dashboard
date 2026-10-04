import streamlit as st
import pandas as pd
import numpy as np
import time

# Oldal konfiguráció
st.set_page_config(
    page_title="Mester Kvant - Kereskedési Dashboard",
    page_icon="📈",
    layout="wide"
)

# Címsor
st.title("📈 Mester Kvant Kereskedési Dashboard")
st.markdown("Üdvözlöm a kereskedési bot élő irányítópultján!")

# Oldalsáv (Sidebar) beállításai
st.sidebar.header("Vezérlőpult")
bot_status = st.sidebar.toggle("Bot futtatása (Live)", value=True)
selected_symbol = st.sidebar.selectbox("Kiválasztott eszköz", ["BTC/USDT", "ETH/USDT", "SOL/USDT"])
risk_level = st.sidebar.slider("Kockázati szint (%)", 1, 10, 3)

if bot_status:
    st.sidebar.success("Státusz: FUT🟢")
else:
    st.sidebar.warning("Státusz: LEÁLLÍTVA🔴")

# Főoldali adatok / Metrikák
col1, col2, col3, col4 = st.columns(4)
col1.metric("Egyenleg", "$12,450.80", "+$340.20 (2.8%)")
col2.metric("Nyitott pozíciók", "3 db", "-1")
col3.metric("Mai Profit", "$185.50", "+5.4%")
col4.metric("Kockázati arány", f"{risk_level}%", "Optimális")

st.markdown("---")

# Szimulált grafikon és adatok
st.subheader(f"Árfolyam grafikon és teljesítmény: {selected_symbol}")

# Véletlenszerű adatok generálása a grafikonhoz
chart_data = pd.DataFrame(
    np.random.randn(50, 2) * 50 + 1000,
    columns=['Portfólió érték ($)', 'Piaci Ár ($)']
)

st.line_chart(chart_data)

# Táblázat a legutóbbi ügyletekről
st.subheader("Legutóbbi Kötések")
history_data = pd.DataFrame({
    "Időpont": ["2026-10-04 19:10", "2026-10-04 18:45", "2026-10-04 17:20"],
    "Eszköz": [selected_symbol, selected_symbol, "ETH/USDT"],
    "Típus": ["BUY", "SELL", "BUY"],
    "Mennyiség": [0.5, 0.5, 1.2],
    "Ár ($)": [61200, 61550, 2450],
    "Eredmény": ["+$175.00", "+$175.00", "-$30.00"]
})

st.table(history_data)
