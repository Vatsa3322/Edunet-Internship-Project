import streamlit as st
import pickle
from streamlit_option_menu import option_menu

# Change Name & Logo
st.set_page_config(page_title="Disease Prediction", page_icon="⚕️")

# Hiding Streamlit add-ons
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Adding Background Image
background_image_url = "https://imageio.forbes.com/specials-images/imageserve/67c87cf77106670c853909b2/White-cyborg-robotic-hand-pointing-his-finger-to-human-hand-with-stretched-finger--/960x0.jpg?format=jpg&width=1440"  # Replace with your image URL

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
background-image: url({background_image_url});
background-size: cover;
background-position: center;
background-repeat: no-repeat;
background-attachment: fixed;
}}

[data-testid="stAppViewContainer"]::before {{
content: "";
position: absolute;
top: 0;
left: 0;
width: 100%;
height: 100%;
background-color: rgba(0, 0, 0, 0.7);
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Load the saved models
models = {
    'diabetes': pickle.load(open('Models\diabetes.sav', 'rb')),
    'heart_disease': pickle.load(open('Models\heart_disease_model.sav', 'rb')),
    'parkinsons': pickle.load(open('Models\parkinson.sav', 'rb')),
    'lung_cancer': pickle.load(open('Models\lungs_disease_model.sav', 'rb')),
    'Alzheimer': pickle.load(open('Models\Alzheimer_prediction.sav', 'rb')),
    'kidney': pickle.load(open('Models\kidneydisease.sav', 'rb')),
}

# Create a dropdown menu for disease prediction
selected = st.selectbox(
    'Select a Disease to Predict',
    ['Diabetes Prediction',
     'Heart Disease Prediction',
     'Parkinsons Prediction',
     'Lung Cancer Prediction',
     'Alzheimer Prediction',
     'Kidney Disease Prediction']
)

def display_input(label, tooltip, key, type="text"):
    if type == "text":
        return st.text_input(label, key=key, help=tooltip)
    elif type == "number":
        return st.number_input(label, key=key, help=tooltip, step=1)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes')
    st.write("Enter the following details to predict diabetes:")

    #Pregnancies = display_input('Number of Pregnancies', 'Enter number of times pregnant', 'Pregnancies', 'number')
    Glucose = display_input('Glucose Level', 'Enter glucose level', 'Glucose', 'number')
    BloodPressure = display_input('Blood Pressure value', 'Enter blood pressure value', 'BloodPressure', 'number')
    SkinThickness = display_input('Skin Thickness value', 'Enter skin thickness value', 'SkinThickness', 'number')
    Insulin = display_input('Insulin Level', 'Enter insulin level', 'Insulin', 'number')
    BMI = display_input('BMI value', 'Enter Body Mass Index value', 'BMI', 'number')
    DiabetesPedigreeFunction = display_input('Diabetes Pedigree Function value', 'Enter diabetes pedigree function value', 'DiabetesPedigreeFunction', 'number')
    Age = display_input('Age of the Person', 'Enter age of the person', 'Age', 'number')

    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        diab_prediction = models['diabetes'].predict([[Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'
        st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease')
    st.write("Enter the following details to predict heart disease:")

    age = display_input('Age', 'Enter age of the person', 'age', 'number')
    sex = display_input('Sex (1 = male; 0 = female)', 'Enter sex of the person', 'sex', 'number')
    cp = display_input('Chest Pain types (0, 1, 2, 3)', 'Enter chest pain type', 'cp', 'number')
    trestbps = display_input('Resting Blood Pressure', 'Enter resting blood pressure', 'trestbps', 'number')
    chol = display_input('Serum Cholesterol in mg/dl', 'Enter serum cholesterol', 'chol', 'number')
    fbs = display_input('Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)', 'Enter fasting blood sugar', 'fbs', 'number')
    restecg = display_input('Resting Electrocardiographic results (0, 1, 2)', 'Enter resting ECG results', 'restecg', 'number')
    thalach = display_input('Maximum Heart Rate achieved', 'Enter maximum heart rate', 'thalach', 'number')
    exang = display_input('Exercise Induced Angina (1 = yes; 0 = no)', 'Enter exercise induced angina', 'exang', 'number')
    oldpeak = display_input('ST depression induced by exercise', 'Enter ST depression value', 'oldpeak', 'number')
    slope = display_input('Slope of the peak exercise ST segment (0, 1, 2)', 'Enter slope value', 'slope', 'number')
    ca = display_input('Major vessels colored by fluoroscopy (0-3)', 'Enter number of major vessels', 'ca', 'number')
    thal = display_input('Thal (0 = normal; 1 = fixed defect; 2 = reversible defect)', 'Enter thal value', 'thal', 'number')

    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        heart_prediction = models['heart_disease'].predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        heart_diagnosis = 'The person has heart disease' if heart_prediction[0] == 1 else 'The person does not have heart disease'
        st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease")
    st.write("Enter the following details to predict Parkinson's disease:")

    fo = display_input('MDVP:Fo(Hz)', 'Enter MDVP:Fo(Hz) value', 'fo', 'number')
    fhi = display_input('MDVP:Fhi(Hz)', 'Enter MDVP:Fhi(Hz) value', 'fhi', 'number')
    flo = display_input('MDVP:Flo(Hz)', 'Enter MDVP:Flo(Hz) value', 'flo', 'number')
    Jitter_percent = display_input('MDVP:Jitter(%)', 'Enter MDVP:Jitter(%) value', 'Jitter_percent', 'number')
    Jitter_Abs = display_input('MDVP:Jitter(Abs)', 'Enter MDVP:Jitter(Abs) value', 'Jitter_Abs', 'number')
    RAP = display_input('MDVP:RAP', 'Enter MDVP:RAP value', 'RAP', 'number')
    PPQ = display_input('MDVP:PPQ', 'Enter MDVP:PPQ value', 'PPQ', 'number')
    DDP = display_input('Jitter:DDP', 'Enter Jitter:DDP value', 'DDP', 'number')
    Shimmer = display_input('MDVP:Shimmer', 'Enter MDVP:Shimmer value', 'Shimmer', 'number')
    Shimmer_dB = display_input('MDVP:Shimmer(dB)', 'Enter MDVP:Shimmer(dB) value', 'Shimmer_dB', 'number')
    APQ3 = display_input('Shimmer:APQ3', 'Enter Shimmer:APQ3 value', 'APQ3', 'number')
    APQ5 = display_input('Shimmer:APQ5', 'Enter Shimmer:APQ5 value', 'APQ5', 'number')
    APQ = display_input('MDVP:APQ', 'Enter MDVP:APQ value', 'APQ', 'number')
    DDA = display_input('Shimmer:DDA', 'Enter Shimmer:DDA value', 'DDA', 'number')
    NHR = display_input('NHR', 'Enter NHR value', 'NHR', 'number')
    HNR = display_input('HNR', 'Enter HNR value', 'HNR', 'number')
    RPDE = display_input('RPDE', 'Enter RPDE value', 'RPDE', 'number')
    DFA = display_input('DFA', 'Enter DFA value', 'DFA', 'number')
    spread1 = display_input('Spread1', 'Enter spread1 value', 'spread1', 'number')
    spread2 = display_input('Spread2', 'Enter spread2 value', 'spread2', 'number')
    D2 = display_input('D2', 'Enter D2 value', 'D2', 'number')
    PPE = display_input('PPE', 'Enter PPE value', 'PPE', 'number')

    parkinsons_diagnosis = ''
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = models['parkinsons'].predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
        parkinsons_diagnosis = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"
        st.success(parkinsons_diagnosis)

# Lung Cancer Prediction Page
if selected == "Lung Cancer Prediction":
    st.title("Lung Cancer")
    st.write("Enter the following details to predict lung cancer:")

    GENDER = display_input('Gender (1 = Male; 0 = Female)', 'Enter gender of the person', 'GENDER', 'number')
    AGE = display_input('Age', 'Enter age of the person', 'AGE', 'number')
    SMOKING = display_input('Smoking (1 = Yes; 0 = No)', 'Enter if the person smokes', 'SMOKING', 'number')
    YELLOW_FINGERS = display_input('Yellow Fingers (1 = Yes; 0 = No)', 'Enter if the person has yellow fingers', 'YELLOW_FINGERS', 'number')
    ANXIETY = display_input('Anxiety (1 = Yes; 0 = No)', 'Enter if the person has anxiety', 'ANXIETY', 'number')
    PEER_PRESSURE = display_input('Peer Pressure (1 = Yes; 0 = No)', 'Enter if the person is under peer pressure', 'PEER_PRESSURE', 'number')
    CHRONIC_DISEASE = display_input('Chronic Disease (1 = Yes; 0 = No)', 'Enter if the person has a chronic disease', 'CHRONIC_DISEASE', 'number')
    FATIGUE = display_input('Fatigue (1 = Yes; 0 = No)', 'Enter if the person experiences fatigue', 'FATIGUE', 'number')
    ALLERGY = display_input('Allergy (1 = Yes; 0 = No)', 'Enter if the person has allergies', 'ALLERGY', 'number')
    WHEEZING = display_input('Wheezing (1 = Yes; 0 = No)', 'Enter if the person experiences wheezing', 'WHEEZING', 'number')
    ALCOHOL_CONSUMING = display_input('Alcohol Consuming (1 = Yes; 0 = No)', 'Enter if the person consumes alcohol', 'ALCOHOL_CONSUMING', 'number')
    COUGHING = display_input('Coughing (1 = Yes; 0 = No)', 'Enter if the person experiences coughing', 'COUGHING', 'number')
    SHORTNESS_OF_BREATH = display_input('Shortness Of Breath (1 = Yes; 0 = No)', 'Enter if the person experiences shortness of breath', 'SHORTNESS_OF_BREATH', 'number')
    SWALLOWING_DIFFICULTY = display_input('Swallowing Difficulty (1 = Yes; 0 = No)', 'Enter if the person has difficulty swallowing', 'SWALLOWING_DIFFICULTY', 'number')
    CHEST_PAIN = display_input('Chest Pain (1 = Yes; 0 = No)', 'Enter if the person experiences chest pain', 'CHEST_PAIN', 'number')

    lungs_diagnosis = ''
    if st.button("Lung Cancer Test Result"):
        lungs_prediction = models['lung_cancer'].predict([[GENDER, AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, CHRONIC_DISEASE, FATIGUE, ALLERGY, WHEEZING, ALCOHOL_CONSUMING, COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN]])
        lungs_diagnosis = "The person has lung cancer disease" if lungs_prediction[0] == 1 else "The person does not have lung cancer disease"
        st.success(lungs_diagnosis)


# Alzheimer Disease Prediction Page
if selected == "Alzheimer Prediction":
    st.title("Alzheimer Disease")
    st.write("Enter the following details to predict Alzheimer disease:")

    Age = display_input('Age', 'Enter age of the person', 'Age', 'number')
    Smoking = display_input('Smoking (1 = Yes; 0 = No)', 'Enter if the person smokes', 'smoking', 'number')
    AlcoholConsumption = display_input('Alcohol Consumption (1 = Yes; 0 = No)', 'Enter if the person consumes alcohol', 'alcohol', 'number')
    FamilyHistoryAlzheimers = display_input('Family History of Alzheimer (1 = Yes; 0 = No)', 'Enter if the person has family history of Alzheimer', 'family_history', 'number')
    HeadInjury = display_input('Head Injury (1 = Yes; 0 = No)', 'Enter if the person has head injury', 'head_injury', 'number')
    Confusion = display_input('Confusion (1 = Yes; 0 = No)', 'Enter if the person is confused', 'confusion', 'number')


    Alzheimer_diagnosis = ''
    if st.button("Alzheimer Test Result"):
        Alzheimer_prediction = models['Alzheimer'].predict([[Age,Smoking,AlcoholConsumption,FamilyHistoryAlzheimers,HeadInjury,Confusion]])
        Alzheimer_diagnosis = "The person has Alzheimer disease" if Alzheimer_prediction[0] == 1 else "The person does not have Alzheimer disease"
        st.success(Alzheimer_diagnosis)

# Kidney Disease Prediction Page
if selected == "Kidney Disease Prediction":
    st.title("Kidney Disease")
    st.write("Enter the following details to predict kidney disease:")

    age = display_input('Age', 'Enter age of the person', 'age', 'number')
    bp = display_input('Blood Pressure', 'Enter blood pressure', 'bp', 'number')
    sg = display_input('Sugar level', 'Enter sugar level', 'sg', 'number')
    al = display_input('Albuminuria', 'Enter Albuminuria (1 = Yes; 0 = No)', 'al', 'number')
    bu = display_input('Blood Urea', 'Enter blood urea', 'bu', 'number')
    sc = display_input('Serum Creatinine', 'Enter serum creatinine level ', 'sc', 'number')
    sod = display_input('Sodium', 'Enter sodium level', 'sod', 'number')
    pot = display_input('Potassium', 'Enter potassium level', 'pot', 'number')
    hemo = display_input('Hemoglobin', 'Enter hemoglobin level', 'hemo', 'number')
    pcv = display_input('Packed Cell Volume', 'Enter packed cell volume', 'pcv', 'number')
    wc = display_input('White Blood Cell Count', 'Enter white blood cell count', 'wc', 'number')
    rc = display_input('Red Blood Cell Count', 'Enter red blood cell count', 'rc', 'number')
    htn = display_input('Hypertension (1 = Yes; 0 = No)', 'Enter if the person has hypertension', 'htn', 'number')
    dm = display_input('Diabetes Mellitus (1 = Yes; 0 = No)', 'Enter if the person has diabetes mellitus', 'dm', 'number')
    appet = display_input('Appetite (1 = Good; 0 = Poor)', 'Enter appetite', 'appet', 'number')
    pe = display_input('Pedal Edema (1 = Yes; 0 = No)', 'Enter if the person has pedal edema', 'pe', 'number')
    ane = display_input('Anemia (1 = Yes; 0 = No)', 'Enter if the person has anemia', 'ane', 'number')

    thyroid_diagnosis = ''
    if st.button("Kidney Test Result"):
        kidneydisease_prediction = models['Kidney'].predict([[age,bp,sg,al,bu,sc,sod,pot,hemo,pcv,wc,rc,htn,dm,appet,pe,ane]])
        kidneydisease_diagnosis = "The person has Kidney disease" if kidneydisease_prediction[0] == 1 else "The person does not have Kidney disease"
        st.success(kidneydisease_diagnosis)





