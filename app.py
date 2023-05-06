import streamlit as st

# Název aplikace
st.title("Kalkulačka důchodu")

# Vstupní pole pro zadání věku
vek = st.number_input("Věk:", min_value=18, max_value=100)

# Vstupní pole pro zadání průměrného měsíčního příjmu
prijem = st.number_input("Průměrný měsíční příjem (Kč):", min_value=0)

# Vstupní pole pro zadání odhadovaného ročního nárůstu příjmu
narust = st.number_input("Odhadovaný roční nárůst příjmu (%):", min_value=0)

# Výpočet celkového příjmu za 35 let s odhadovaným ročním nárůstem
prijmy_celkem = 12 * prijem * sum([(1 + narust / 100) ** i for i in range(35)])

# Výpočet odhadovaného důchodu jako 50% průměrného příjmu z posledních 5 let před důchodem
duchod = 0.5 * (prijmy_celkem / 60)

# Výstup vypočítaného důchodu
st.write("Odhadovaný měsíční důchod:", round(duchod), "Kč")

