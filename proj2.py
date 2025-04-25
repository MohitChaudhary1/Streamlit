import streamlit as st

st.title("Coffee Maker App")

if st.button("Make Coffee"):
    st.success("Your Coffee is being brewed")

add_masala = st.checkbox("Add Coffee Beans")

if add_masala:
    st.write("Cofee beans added")

tea_type = st.radio("Pick your chai base: ", ["Milk", "Water", "Almond Milk"])
st.write(f"Selected base {tea_type}")
flavour = st.selectbox("Choose flavour: ", ["Adrak", "Kesar", "Tulsi"])
st.write(f"Selected Flavour {flavour}")

sugar = st.slider("Sigar level (spoon)", 0, 5, 4)
st.write(f"Selected sugar level {sugar}")

cups = st.number_input("How many cups", min_value=1, max_value=10, step=1)
st.write(f"Selected sugar level {cups}")

name = st.text_input("Enter your name")
if name:
    st.write(f"Welcome, {name} ! Your Coffee is on the way")

dob = st.date_input("Select your date of birth")
st.write(f"Your date of birth {dob}")