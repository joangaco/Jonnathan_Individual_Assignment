import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns

# NOTE: Please remember to check if scikit-learn is installed, and install it if not to use sklearn.model_selection and sklearn.ensemble 

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

df=pd.read_csv('Admission.csv')

def main():

    menu=['Welcome page', 'Exploratory Data Analysis', 'Key Takeaways']
    choice=st.sidebar.selectbox("Menu", menu)

    if choice=='Welcome page':
    	
    	title_text = 'Individual assingment - Python for Data Analysis 2'
    	custom_color = 'color: #002060;'
    	centered_style = 'text-align: center;'
    	font_size = 'font-size: 30px;'
    	title_style = f"{custom_color} {centered_style} {font_size}"
    	st.markdown(f"<h1 style='{title_style}'>{title_text}</h1>", unsafe_allow_html=True)
    	
    	st.image('https://images.pexels.com/photos/577585/pexels-photo-577585.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2')

    	col1, col2 = st.columns(2)
    	
    	with col1:st.image('https://images.pexels.com/photos/574071/pexels-photo-574071.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2')

    	with col2:st.image("https://images.pexels.com/photos/2004161/pexels-photo-2004161.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2")
		    	    	
    	st.markdown('---')

    	title_text = 'Admission Dataset'
    	custom_color = 'color: #002060;'
    	centered_style = 'text-align: center;'
    	font_size = 'font-size: 30px;'
    	title_style = f"{custom_color} {centered_style} {font_size}"
    	st.markdown(f"<h1 style='{title_style}'>{title_text}</h1>", unsafe_allow_html=True)
    	
    	text = 'The college admissions process is one of the most important moments for people as they go from their high school education to choosing a topic that they are truly passionate about to focus on.'
    	custom_color = 'color: #5B9BD5;'
    	font_size = 'font-size: 24px;'
    	text_alignment = 'text-align: justify; text-justify: inter-word;'

    	text_style = f"{custom_color} {font_size} {text_alignment}"
    	st.markdown(f"<p style='{text_style}'>{text}</p>", unsafe_allow_html=True)

    	text = 'In this way, all participants in the admission process seek to obtain the best results to try to achieve a place in the study program and university of their dreams.'
    	custom_color = 'color: #5B9BD5;'
    	font_size = 'font-size: 24px;'
    	text_alignment = 'text-align: justify; text-justify: inter-word;'

    	text_style = f"{custom_color} {font_size} {text_alignment}"
    	st.markdown(f"<p style='{text_style}'>{text}</p>", unsafe_allow_html=True)

    	text = 'Thus, by analyzing the Admissions dataset, it can be observed with a sample of 400 participants how their results in tests such as TOEFL or GRE are relevant when determining their chances of being admitted.'
    	custom_color = 'color: #5B9BD5;'
    	font_size = 'font-size: 24px;'
    	text_alignment = 'text-align: justify; text-justify: inter-word;'

    	text_style = f"{custom_color} {font_size} {text_alignment}"
    	st.markdown(f"<p style='{text_style}'>{text}</p>", unsafe_allow_html=True)

    	text = 'As a result, this app has 3 sections that can be selected on the left side. The first is this Welcome Page, where a brief introduction of the information identified in the database is made. The second is the Exploratory Data Analysis, which shows the analyzes carried out in an easy and interactive way. And the third is the Key Takeaways section that shows insights from the data.'
    	custom_color = 'color: #5B9BD5;'
    	font_size = 'font-size: 24px;'
    	text_alignment = 'text-align: justify; text-justify: inter-word;'

    	text_style = f"{custom_color} {font_size} {text_alignment}"
    	st.markdown(f"<p style='{text_style}'>{text}</p>", unsafe_allow_html=True)

    	st.image('https://images.pexels.com/photos/3807755/pexels-photo-3807755.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2')

    elif choice=='Exploratory Data Analysis':
    	
    	title_text = 'Admission Dataset Analysis'
    	custom_color = 'color: #002060;'
    	centered_style = 'text-align: center;'
    	font_size = 'font-size: 36px;'
    	title_style = f"{custom_color} {centered_style} {font_size}"
    	st.markdown(f"<h1 style='{title_style}'>{title_text}</h1>", unsafe_allow_html=True)

    	title_text = 'Original Dataset Preview'
    	custom_color = 'color: #002060;'
    	centered_style = 'text-align: center;'
    	font_size = 'font-size: 30px;'
    	title_style = f"{custom_color} {centered_style} {font_size}"
    	st.markdown(f"<h1 style='{title_style}'>{title_text}</h1>", unsafe_allow_html=True)

    	text = 'The original database is made up of 9 columns with 400 rows, as can be seen below:'
    	custom_color = 'color: #5B9BD5;'
    	font_size = 'font-size: 24px;'
    	text_alignment = 'text-align: justify; text-justify: inter-word;'

    	text_style = f"{custom_color} {font_size} {text_alignment}"
    	st.markdown(f"<p style='{text_style}'>{text}</p>", unsafe_allow_html=True)

    	data=pd.read_csv('Admission.csv')
    	st.dataframe(data)

    	df=pd.read_csv('Admission.csv')
    	TOEFL_dist=data['TOEFL Score'].value_counts()
    	GRE_dist=df['GRE Score'].value_counts()
    	University_dist=df['University Rating'].value_counts()
    	SOP_dist=df['SOP'].value_counts()
    	CGPA_dist=df['CGPA'].value_counts()
    	Research_dist=df['Research'].value_counts()
    	Adm_dist=df['Admission Chance'].value_counts()
    	
    	st.markdown('---')

    	title_text = 'TOEFL & GRE results'
    	custom_color = 'color: #002060;'
    	centered_style = 'text-align: center;'
    	font_size = 'font-size: 30px;'
    	title_style = f"{custom_color} {centered_style} {font_size}"
    	st.markdown(f"<h1 style='{title_style}'>{title_text}</h1>", unsafe_allow_html=True)

    	text = 'In the TOEFL and GRE results it can be seen all the scores obtained by applicants in each test for the admission process.'
    	custom_color = 'color: #5B9BD5;'
    	font_size = 'font-size: 24px;'
    	text_alignment = 'text-align: justify; text-justify: inter-word;'

    	text_style = f"{custom_color} {font_size} {text_alignment}"
    	st.markdown(f"<p style='{text_style}'>{text}</p>", unsafe_allow_html=True)

    	col1, col2 = st.columns(2)
    	with col1:
    		fig,ax=plt.subplots()
    		title_text = 'TOEFL Results'
    		custom_color = 'color: #002060;'
    		centered_style = 'text-align: center;'
    		font_size = 'font-size: 30px;'
    		title_style = f"{custom_color} {centered_style} {font_size}"
    		st.markdown(f"<h1 style='{title_style}'>{title_text}</h1>", unsafe_allow_html=True)
    		ax.bar(TOEFL_dist.index,TOEFL_dist)
    		st.pyplot(fig)

    		text = 'It can be identified that the score ranges from 0 to 120, all of the applicants have a score higher than 90 points. Furthermore, it can be seen that the mode is 110 points.'
    		custom_color = 'color: #5B9BD5;'
    		font_size = 'font-size: 24px;'
    		text_alignment = 'text-align: justify; text-justify: inter-word;'
    		text_style = f"{custom_color} {font_size} {text_alignment}"
    		st.markdown(f"<p style='{text_style}'>{text}</p>", unsafe_allow_html=True)

    	with col2:
    		fig,ax=plt.subplots()
    		title_text = 'GRE Results'
    		custom_color = 'color: #002060;'
    		centered_style = 'text-align: center;'
    		font_size = 'font-size: 30px;'
    		title_style = f"{custom_color} {centered_style} {font_size}"
    		st.markdown(f"<h1 style='{title_style}'>{title_text}</h1>", unsafe_allow_html=True)
    		ax.bar(GRE_dist.index,GRE_dist)
    		st.pyplot(fig)

    		text = 'While in the case of GRE the scores range from 0 to 340, where all candidates are above 290 points. Furthermore, it can be seen that the mode is at 312 and 324 points.'
    		custom_color = 'color: #5B9BD5;'
    		font_size = 'font-size: 24px;'
    		text_alignment = 'text-align: justify; text-justify: inter-word;'
    		text_style = f"{custom_color} {font_size} {text_alignment}"
    		st.markdown(f"<p style='{text_style}'>{text}</p>", unsafe_allow_html=True)
    	
    	st.markdown('---')

    	title_text = 'SOP & CGPA results'
    	custom_color = 'color: #002060;'
    	centered_style = 'text-align: center;'
    	font_size = 'font-size: 30px;'
    	title_style = f"{custom_color} {centered_style} {font_size}"
    	st.markdown(f"<h1 style='{title_style}'>{title_text}</h1>", unsafe_allow_html=True)

    	text = 'In the SOP and CGPA results it can be seen the consolidated results obtained by applicants for the admission process.'
    	custom_color = 'color: #5B9BD5;'
    	font_size = 'font-size: 24px;'
    	text_alignment = 'text-align: justify; text-justify: inter-word;'

    	text_style = f"{custom_color} {font_size} {text_alignment}"
    	st.markdown(f"<p style='{text_style}'>{text}</p>", unsafe_allow_html=True)

    	title_text = 'SOP Results'
    	custom_color = 'color: #002060;'
    	centered_style = 'text-align: center;'
    	font_size = 'font-size: 30px;'
    	title_style = f"{custom_color} {centered_style} {font_size}"
    	st.markdown(f"<h1 style='{title_style}'>{title_text}</h1>", unsafe_allow_html=True)
    	fig = px.scatter(x=SOP_dist.index, y=SOP_dist, labels={'x': 'SOP Score', 'y': 'Frequency'})
    	st.plotly_chart(fig)
    	
    	text = 'The score ranges from 1 to 5, more than 70% of the applicants have a score higher than 3 out of 5. Furthermore, it can be seen that the mode is 3.5 and 4 points.'
    	custom_color = 'color: #5B9BD5;'
    	font_size = 'font-size: 24px;'
    	text_alignment = 'text-align: justify; text-justify: inter-word;'
    	text_style = f"{custom_color} {font_size} {text_alignment}"
    	st.markdown(f"<p style='{text_style}'>{text}</p>", unsafe_allow_html=True)
    	
    	title_text = 'CGPA Results'
    	custom_color = 'color: #002060;'
    	centered_style = 'text-align: center;'
    	font_size = 'font-size: 30px;'
    	title_style = f"{custom_color} {centered_style} {font_size}"
    	st.markdown(f"<h1 style='{title_style}'>{title_text}</h1>", unsafe_allow_html=True)
    	fig = px.scatter(x=CGPA_dist.index, y=CGPA_dist, labels={'x': 'CGPA Score', 'y': 'Frequency'})
    	st.plotly_chart(fig)

    	text = 'While in the case of CGPA the scores range from 6.8 to 9.9, where all candidates have a wide variety of scores. Furthermore, it can be seen that the mode is a score of 8.'
    	custom_color = 'color: #5B9BD5;'
    	font_size = 'font-size: 24px;'
    	text_alignment = 'text-align: justify; text-justify: inter-word;'
    	text_style = f"{custom_color} {font_size} {text_alignment}"
    	st.markdown(f"<p style='{text_style}'>{text}</p>", unsafe_allow_html=True)
    	
    	st.markdown('---')

    	title_text = 'TOEFL & GRE results impact on Admission Chance'
    	custom_color = 'color: #002060;'
    	centered_style = 'text-align: center;'
    	font_size = 'font-size: 30px;'
    	title_style = f"{custom_color} {centered_style} {font_size}"
    	st.markdown(f"<h1 style='{title_style}'>{title_text}</h1>", unsafe_allow_html=True)

    	text = 'After analyzing the variables separately, it is important to identify their impact on Admission Chance, as detailed below:'
    	custom_color = 'color: #5B9BD5;'
    	font_size = 'font-size: 24px;'
    	text_alignment = 'text-align: justify; text-justify: inter-word;'

    	text_style = f"{custom_color} {font_size} {text_alignment}"
    	st.markdown(f"<p style='{text_style}'>{text}</p>", unsafe_allow_html=True)

    
    	col1, col2 = st.columns(2)
    	with col1:
    		data = pd.read_csv('Admission.csv')
    		x_axis = 'TOEFL Score'
    		y_axis = 'Admission Chance'
    		average_data = data.groupby(x_axis)[y_axis].mean().reset_index()
    		title_text = 'TOEFL Results'
    		custom_color = 'color: #002060;'
    		centered_style = 'text-align: center;'
    		font_size = 'font-size: 30px;'
    		title_style = f"{custom_color} {centered_style} {font_size}"
    		st.markdown(f"<h1 style='{title_style}'>{title_text}</h1>", unsafe_allow_html=True)
    		fig = px.line(average_data, x=x_axis, y=y_axis, title=f'Average {y_axis}')
    		st.plotly_chart(fig, use_container_width=True)
    	
    	with col2:
    		data = pd.read_csv('Admission.csv')
    		x_axis = 'GRE Score'
    		y_axis = 'Admission Chance'
    		average_data = data.groupby(x_axis)[y_axis].mean().reset_index()
    		title_text = 'GRE Results'
    		custom_color = 'color: #002060;'
    		centered_style = 'text-align: center;'
    		font_size = 'font-size: 30px;'
    		title_style = f"{custom_color} {centered_style} {font_size}"
    		st.markdown(f"<h1 style='{title_style}'>{title_text}</h1>", unsafe_allow_html=True)
    		fig = px.line(average_data, x=x_axis, y=y_axis, title=f'Average {y_axis}')
    		st.plotly_chart(fig, use_container_width=True)

    	text = 'As can be seen in both graphs, the higher the TOEFL or GRE score, the greater the Admission Chance. Similarly, it happens the same with SOP and CGPA results, as displayed below:'
    	custom_color = 'color: #5B9BD5;'
    	font_size = 'font-size: 24px;'
    	text_alignment = 'text-align: justify; text-justify: inter-word;'

    	text_style = f"{custom_color} {font_size} {text_alignment}"
    	st.markdown(f"<p style='{text_style}'>{text}</p>", unsafe_allow_html=True)

    	col1, col2 = st.columns(2)
    	with col1:
    		data = pd.read_csv('Admission.csv')
    		x_axis = 'SOP'
    		y_axis = 'Admission Chance'
    		average_data = data.groupby(x_axis)[y_axis].mean().reset_index()
    		title_text = 'SOP Results'
    		custom_color = 'color: #002060;'
    		centered_style = 'text-align: center;'
    		font_size = 'font-size: 30px;'
    		title_style = f"{custom_color} {centered_style} {font_size}"
    		st.markdown(f"<h1 style='{title_style}'>{title_text}</h1>", unsafe_allow_html=True)
    		fig = px.line(average_data, x=x_axis, y=y_axis, title=f'Average {y_axis}')
    		st.plotly_chart(fig, use_container_width=True)
    	
    	with col2:
    		data = pd.read_csv('Admission.csv')
    		x_axis = 'CGPA'
    		y_axis = 'Admission Chance'
    		average_data = data.groupby(x_axis)[y_axis].mean().reset_index()
    		title_text = 'CGPA Results'
    		custom_color = 'color: #002060;'
    		centered_style = 'text-align: center;'
    		font_size = 'font-size: 30px;'
    		title_style = f"{custom_color} {centered_style} {font_size}"
    		st.markdown(f"<h1 style='{title_style}'>{title_text}</h1>", unsafe_allow_html=True)
    		fig = px.line(average_data, x=x_axis, y=y_axis, title=f'Average {y_axis}')
    		st.plotly_chart(fig, use_container_width=True)
 	
    elif choice=='Key Takeaways':

    	title_text = 'General Insights'
    	custom_color = 'color: #002060;'
    	centered_style = 'text-align: center;'
    	font_size = 'font-size: 30px;'
    	title_style = f"{custom_color} {centered_style} {font_size}"
    	st.markdown(f"<h1 style='{title_style}'>{title_text}</h1>", unsafe_allow_html=True)    	

    	text = 'After the analyzes carried out, it can be determined that the better results you have in exams such as TOEFL and GRE, the better the chances of Admission Chance you can have. As well as the same happens with the SOP and CGPA scores.'
    	custom_color = 'color: #5B9BD5;'
    	font_size = 'font-size: 24px;'
    	text_alignment = 'text-align: justify; text-justify: inter-word;'

    	text_style = f"{custom_color} {font_size} {text_alignment}"
    	st.markdown(f"<p style='{text_style}'>{text}</p>", unsafe_allow_html=True)

    	text = 'As a result, to conclude the analysis, below there is an interactive graph that allows to identify how each of the variables that are available in the dataset could impacts the Admission Chance:'
    	custom_color = 'color: #5B9BD5;'
    	font_size = 'font-size: 24px;'
    	text_alignment = 'text-align: justify; text-justify: inter-word;'

    	text_style = f"{custom_color} {font_size} {text_alignment}"
    	st.markdown(f"<p style='{text_style}'>{text}</p>", unsafe_allow_html=True)

    	data = pd.read_csv('Admission.csv')
    	data = data.iloc[:, 1:]
    	title_text = 'All Dataset variables impact on Admission Chance'
    	custom_color = 'color: #002060;'
    	centered_style = 'text-align: center;'
    	font_size = 'font-size: 30px;'
    	title_style = f"{custom_color} {centered_style} {font_size}"
    	st.markdown(f"<h1 style='{title_style}'>{title_text}</h1>", unsafe_allow_html=True)    	
    	x_axis = st.selectbox("Select X-axis Variable", data.columns)
    	fig = px.bar(data, x=x_axis, y='Admission Chance', title=f'Bar Chart')
    	st.plotly_chart(fig, use_container_width=True)
    	st.markdown('---')

    	data = pd.read_csv('Admission.csv')
    	X = data[['GRE Score', 'TOEFL Score', 'University Rating', 'SOP', 'LOR ', 'CGPA', 'Research']]
    	y = data['Admission Chance']
    	model = RandomForestRegressor()
    	model.fit(X, y)
    	
    	title_text = 'Admission Chance Prediction'
    	custom_color = 'color: #002060;'
    	centered_style = 'text-align: center;'
    	font_size = 'font-size: 30px;'
    	title_style = f"{custom_color} {centered_style} {font_size}"
    	st.markdown(f"<h1 style='{title_style}'>{title_text}</h1>", unsafe_allow_html=True)

    	text = 'Finally, to try to predict the Admission Chance considering all the variables in the dataset, below there is an interactive model has been developed that allows to input different values for each variable to try to identify how the Admission Chance would behave:'
    	custom_color = 'color: #5B9BD5;'
    	font_size = 'font-size: 24px;'
    	text_alignment = 'text-align: justify; text-justify: inter-word;'

    	text_style = f"{custom_color} {font_size} {text_alignment}"
    	st.markdown(f"<p style='{text_style}'>{text}</p>", unsafe_allow_html=True)


    	gre_score = st.slider("GRE Score", min_value=290, max_value=340, value=310)
    	toefl_score = st.slider("TOEFL Score", min_value=90, max_value=120, value=105)
    	university_rating = st.selectbox("University Rating", [1, 2, 3, 4, 5])
    	sop = st.slider("Statement of Purpose (SOP)", min_value=1.0, max_value=5.0, value=3.0)
    	lor = st.slider("Letter of Recommendation (LOR)", min_value=1.0, max_value=5.0, value=3.0)
    	cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0, value=8.0)
    	research = st.selectbox("Research Experience", ["No", "Yes"])
    	user_input = pd.DataFrame({'GRE Score': [gre_score],'TOEFL Score': [toefl_score],'University Rating': [university_rating],'SOP': [sop],'LOR ': [lor],'CGPA': [cgpa],'Research': [1 if research == "Yes" else 0]})
    	prediction = model.predict(user_input)
    	st.write(f"Predicted Admission Chance: {prediction[0]:.2f}")

main()
