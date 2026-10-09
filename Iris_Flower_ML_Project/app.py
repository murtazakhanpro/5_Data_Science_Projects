import streamlit as st
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

st.set_page_config(page_title="Iris Flower Classifier", page_icon="🌸", layout="centered")


@st.cache_resource
def load_model():
	iris = load_iris()
	model = RandomForestClassifier(random_state=42)
	model.fit(iris.data, iris.target)
	return iris, model

iris, model = load_model()

st.title("Iris Flower Classifier")
st.write("Enter the flower measurements to predict its species.")

left, center, right = st.columns([1, 2, 1])
with center:
	sepal_length = st.number_input("Sepal length (cm)", min_value=0.0, value=5.1, step=0.1)
	sepal_width = st.number_input("Sepal width (cm)", min_value=0.0, value=3.5, step=0.1)
	petal_length = st.number_input("Petal length (cm)", min_value=0.0, value=1.4, step=0.1)
	petal_width = st.number_input("Petal width (cm)", min_value=0.0, value=0.2, step=0.1)

	if st.button("Predict species", type="primary", use_container_width=True):
		measurements = [[sepal_length, sepal_width, petal_length, petal_width]]
		prediction = model.predict(measurements)[0]
		st.success(f"Predicted species: **{iris.target_names[prediction].title()}**")