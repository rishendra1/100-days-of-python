import streamlit as st
import matplotlib.pyplot as plt

st.title("Plotting points in a graph")

x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 12, 5]
p = ['A','B','C','D','E']
st.write("Given Points")
for i in range(len(x)):
    st.write(f"{p[i]}) ({x[i]},{y[i]})")

fig, ax = plt.subplots()
ax.plot(x, y)
st.pyplot(fig)
