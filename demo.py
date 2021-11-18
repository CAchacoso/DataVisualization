import pandas as pd
import streamlit as st
import plotly_express as pl

st.set_option('deprecation_showfileUploaderEncoding', False)
st.title("Data Visualization")
st.sidebar.subheader("Visualization Settings")

uploaded_file = st.sidebar.file_uploader(label="Upload File", type=['csv', 'xlsx'])

global df
if uploaded_file is not None:
	print(uploaded_file)
	try:
		df = pd.read_csv(uploaded_file)
	except Exception as e:
		print(e)
		df = pd.read_excel(uploaded_file)

global numeric_columns
try:
	st.write(df)
except Exception as e:
	print(e)
	st.write("Please upload file to application.")

select_chart = st.sidebar.selectbox(
	label="Select the chart type",
	options=['Scatterplots', 'Lineplots', 'Histogram', 'Boxplot']
	)

numeric_columns = list(df.select_dtypes(['float', 'int']).columns)

if select_chart == 'Scatterplots':
	st.sidebar.subheader("Scatterplot Settings")
	try:
		x_values = st.sidebar.selectbox('X-axis', options=numeric_columns)
		y_values = st.sidebar.selectbox('Y-axis', options=numeric_columns)
		plot = pl.scatter(data_frame=df, x=x_values, y=y_values)
		st.plotly_chart(plot)
	except Exception as e:
		print(e)
