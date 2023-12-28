import pickle
import streamlit as st
from streamlit_option_menu import option_menu 



# loading the saved models


heart_model = pickle.load(open("randomforest.pkl",'rb'))
stroke_model = pickle.load(open("xgb_model.pkl",'rb'))
lung_model = pickle.load(open("ann_model.pickle",'rb'))


# sidebar navigation
with st.sidebar:
    
    selected = option_menu('Lifestyle Disease Prediction System', 
                           ['Heart Disease Prediction',
                            'Stroke Prediction',
                            'Lung Cancer Prediction'],
                           
                           default_index=0)
    

# Heart Disease Prediction Page   
if (selected == 'Heart Disease Prediction'): 
     # page title
     st.title('Heart Disease Predictor')
    
     col1, col2, col3 = st.columns(3)
     with col1:
         Cluster_options = ['0', '1']  
         Cluster = st.selectbox('ID ', Cluster_options)
        
     with col1:
         gender_options = ['0 Male', '1 Female']  
         gender = st.selectbox('Gender', gender_options)
        
     with col2:
         age_bin_options = ['0 For 20-30 ','1 For 35-40','2 For 40-45','3 For 45-50','4 For 50-55','5 For 55-60','6 For 60-95']  
         age_bin = st.selectbox('Age', age_bin_options)

     with col3:
         BMI_Class_options = ['1 For 18.5-24.9','2 For 25-29.9','3 For 30-34.9','4 For 35-39.9','5 For 40-49.9','6 For 50<']  
         BMI_Class = st.selectbox('BMI ', BMI_Class_options)

     with col1:
         MAP_Class_options = ['1 For 70-79.9','2 For 80-89.9','3 For 90-99.9','4 For 100-109.9','5 For 110-119.9','6 For 120<']  
         MAP_Class = st.selectbox('Mean Arterial Pressure ', MAP_Class_options)

     with col2:
         cholesterol_options = ['0 HDL', '1 LDL', '2 Normal'] 
         cholesterol = st.selectbox('Cholesterol ', cholesterol_options)

     with col3:
         gluc_options = ['0  Level1', '1  Level2', '2  Level3'] 
         gluc = st.selectbox('Glucose ', gluc_options)

     with col3:
         smoke_options = ['0  No', '1  Yes'] 
         smoke = st.selectbox('Smoking No=0, Yes=1', smoke_options)

     with col2:
         activity_options = ['0  No', '1  Yes'] 
         active = st.selectbox('Physical Activity ', activity_options)

    
    
     
     # code for Prediction
     heart_diagnosis = ''
    
     # creating a button for Prediction
    
     if st.button('Heart Disease Test Result'):
         if not all([Cluster,gender,	age_bin,	BMI_Class,	MAP_Class,	cholesterol,	gluc,	smoke,	active]):
             st.warning("Please fill in all the fields.")
         else:
             Cluster=int(Cluster)
             gender = ''.join(char for char in gender if char.isdigit())
             gender = int(gender) if gender else None
             for char in age_bin:
                if char.isdigit():
                    age_bin += char
                elif age_bin:
                    break
             age_bin = ''.join(char for char in age_bin if char.isdigit())
             age_bin = int(age_bin) if age_bin else None
             for char in BMI_Class:
                if char.isdigit():
                    BMI_Class += char
                elif BMI_Class:
                    break
             BMI_Class = ''.join(char for char in BMI_Class if char.isdigit())
             BMI_Class = int(BMI_Class) if BMI_Class else None
             for char in MAP_Class:
                if char.isdigit():
                    MAP_Class += char
                elif MAP_Class:
                    break
             MAP_Class = ''.join(char for char in MAP_Class if char.isdigit())
             MAP_Class = int(MAP_Class) if MAP_Class else None
             for char in cholesterol:
                if char.isdigit():
                    cholesterol += char
                elif cholesterol:
                    break
             cholesterol = ''.join(char for char in  cholesterol if char.isdigit())
             cholesterol = int(cholesterol) if  cholesterol else None
             for char in gluc:
                if char.isdigit():
                    gluc += char
                elif gluc:
                    break
             gluc = ''.join(char for char in gluc if char.isdigit())
             gluc = int(gluc) if  gluc else None
             smoke = ''.join(char for char in smoke if char.isdigit())
             smoke = int(smoke) if  smoke else None
             active = ''.join(char for char in active if char.isdigit())
             active = int(active) if active else None
             
            
             heart_prediction = heart_model.predict([[Cluster, gender,	age_bin,	BMI_Class,	MAP_Class,	cholesterol,	gluc,	smoke,	active]])                          
            
             if (heart_prediction[0] == 1):
               heart_diagnosis = 'The person might have a chance of sufferring from Heart Disease'
             else:
               heart_diagnosis = 'The person is not likely to suffer from Heart Disease'
        
     st.success(heart_diagnosis)  






##Stroke
if (selected == 'Stroke Prediction'):
    
    # page title
    st.title('Stroke Predictor')
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age ')
        
    with col2:
        avg_glucose_level = st.text_input('Glucose Level')
    
    with col3:
        bmi = st.text_input('BMI kg/cm^2')
    
    with col1:
        
        gender_options = ['1  Male', '0  Female']  
        gender_Male = st.selectbox('Gender ', gender_options)
    
    with col2:
        hypertension = ['0  No', '1  Yes']  
        hypertension_1 = st.selectbox('Do you Suffer from Hypertension ' , hypertension)
    
    with col3:
        heart_disease = ['0  No', '1  Yes']  
        heart_disease_1 = st.selectbox('Do you Have any Heart Disease ', heart_disease)
    
    with col1:
        ever_married = ['0  No', '1  Yes']  
        ever_married_Yes = st.selectbox('Are you Married ', ever_married)
    
    with col2:
        work_type_Never = ['0  Yes', '1  No']  
        work_type_Never_worked = st.selectbox('Have you Ever Worked ', work_type_Never)
        
    with col3:
        work_type = ['0  No', '1  Yes']  
        work_type_Private = st.selectbox('Do you work for a Organisation ' , work_type)
        
    with col1:
        work_type2 = ['0  No', '1  Yes']  
        work_type_Self_employed = st.selectbox(' Are You Self Employed   ' , work_type2)
        
    with col2:
        work_type1 = ['0   No', '1  Yes']  
        work_type_children = st.selectbox('Are you a Child ', work_type1)
        
    with col3:
        Residence_type = ['0 Rural', '1  Urban']  
        Residence_type_Urban = st.selectbox('Residence Type', Residence_type)
        
    with col1:
        smoking_status1 = ['0  No', '1  Yes']  
        smoking_status_formerly_smoked = st.selectbox('Formerly Smoked ', smoking_status1)
        
    with col2:
        smoking_status2 = ['0  No', '1  Yes']  
        smoking_status_never_smoked = st.selectbox('Have you Ever Smoked ', smoking_status2)
        
    with col3:
        smoking_status = ['0  No', '1  Yes']  
        smoking_status_smokes = st.selectbox('Are you Smoking in Present ', smoking_status)
        
    
    
        
    # code for prediction
    stroke_diagnosis=''
    
    # create a button for prediction
    
    if st.button('Stroke Test Result'):
        if not all([age,avg_glucose_level,bmi,gender_Male,hypertension_1,heart_disease_1,ever_married_Yes,work_type_Never_worked,work_type_Private,work_type_Self_employed ,work_type_children,Residence_type_Urban,smoking_status_formerly_smoked,smoking_status_never_smoked,smoking_status_smokes]):
            st.warning("Please fill in all the fields.")
        else:
            age=int(age)
            avg_glucose_level=float(avg_glucose_level)
            bmi=float(bmi)
            gender_Male = ''.join(char for char in gender_Male if char.isdigit())
            gender_Male = int(gender_Male) if  gender_Male else None
            hypertension_1 = ''.join(char for char in hypertension_1 if char.isdigit())
            hypertension_1 = int(hypertension_1) if  hypertension_1 else None
            
            heart_disease_1 = ''.join(char for char in heart_disease_1 if char.isdigit())
            heart_disease_1 = int(heart_disease_1) if  heart_disease_1 else None
            
            ever_married_Yes = ''.join(char for char in ever_married_Yes if char.isdigit())
            ever_married_Yes = int(ever_married_Yes) if  ever_married_Yes else None
            
            work_type_Never_worked = ''.join(char for char in work_type_Never_worked if char.isdigit())
            work_type_Never_worked = int(work_type_Never_worked) if  work_type_Never_worked else None
            
            work_type_Private = ''.join(char for char in work_type_Private if char.isdigit())
            work_type_Private = int(work_type_Private) if  work_type_Private else None
            
            work_type_Self_employed = ''.join(char for char in work_type_Self_employed if char.isdigit())
            work_type_Self_employed = int(work_type_Self_employed) if  work_type_Self_employed else None
            
            work_type_children = ''.join(char for char in work_type_children if char.isdigit())
            work_type_children = int(work_type_children) if  work_type_children else None
            
            Residence_type_Urban = ''.join(char for char in Residence_type_Urban if char.isdigit())
            Residence_type_Urban = int(Residence_type_Urban) if  Residence_type_Urban else None
            
            smoking_status_formerly_smoked = ''.join(char for char in smoking_status_formerly_smoked if char.isdigit())
            smoking_status_formerly_smoked = int(smoking_status_formerly_smoked) if  smoking_status_formerly_smoked else None
            
            smoking_status_never_smoked = ''.join(char for char in smoking_status_never_smoked if char.isdigit())
            smoking_status_never_smoked = int(smoking_status_never_smoked) if  smoking_status_never_smoked else None
            
            smoking_status_smokes = ''.join(char for char in smoking_status_smokes if char.isdigit())
            smoking_status_smokes = int(smoking_status_smokes) if  smoking_status_smokes else None
            
            
            stroke_pred = stroke_model.predict([[age,avg_glucose_level,bmi,gender_Male,hypertension_1,heart_disease_1,ever_married_Yes,work_type_Never_worked,work_type_Private,work_type_Self_employed ,work_type_children,Residence_type_Urban,smoking_status_formerly_smoked,smoking_status_never_smoked,smoking_status_smokes]])
            
            if (stroke_pred[0] == 1):
              stroke_diagnosis = 'The person might have a chance of sufferring from Stroke'
            else:
              stroke_diagnosis = 'The person is not likely to suffer from Stroke'
        
    st.success(stroke_diagnosis)  
    
    
    # Lung Cancer Prediction Page  
if (selected == 'Lung Cancer Prediction'):    
    
    # page title
    st.title("Lung Cancer Predictor ")
    
    col1, col2, col3 = st.columns(3)  
    
    with col1:
        GENDER_OPTIONS = ['0  Female', '1  Male']  
        GENDER = st.selectbox('Gender ', GENDER_OPTIONS)
        
    with col2:
        AGE_options = ['0  If AGE<63', '1  If AGE>63']  
        AGE	 = st.selectbox('Age', AGE_options)
        
    with col3:
        SMOKING_options = ['1  No', '2  Yes']  
        SMOKING	 = st.selectbox('Smoking ', SMOKING_options)
        
    with col1:
        YELLOW_FINGERS_options = ['1  No', '2  Yes']  
        YELLOW_FINGERS = st.selectbox('Yellow Fingers ', YELLOW_FINGERS_options)
        
    with col2:
        ANXIETY_options = ['1  No', '2']  
        ANXIETY	 = st.selectbox('Anxiety ', ANXIETY_options)
        
    with col3:
        PEER_PRESSURE_options = ['1  No', '2  Yes']  
        PEER_PRESSURE = st.selectbox('Peer Pressure ', PEER_PRESSURE_options)
        
    with col1:
        CHRONIC_DISEASE_options = ['1  No', '2  Yes']  
        CHRONIC_DISEASE = st.selectbox('Chronic Disease ', CHRONIC_DISEASE_options)
           
    with col2:
        FATIGUE_options = ['1  No', '2  Yes']  
        FATIGUE = st.selectbox('Fatigue ', FATIGUE_options)
        
    with col3:
        ALLERGY_options = ['1  No', '2  Yes']  
        ALLERGY	 = st.selectbox('Allergy ', ALLERGY_options)
        
    with col1:
        WHEEZING_options = ['1  No', '2  Yes']  
        WHEEZING = st.selectbox('Wheezing  ', WHEEZING_options)
        
    with col2:
        ALCOHOL_CONSUMING_options = ['1  No', '2  Yes']  
        ALCOHOL_CONSUMING = st.selectbox('Alcohol Consuming ', ALCOHOL_CONSUMING_options)
        
    with col3:
        COUGHING_options = ['1  No', '2  Yes']  
        COUGHING = st.selectbox('Coughing ', COUGHING_options)
        
    with col1:
        SHORTNESS_OF_BREATH_options = ['1  No', '2  Yes']  
        SHORTNESS_OF_BREATH = st.selectbox('Shortness of Breath  ', SHORTNESS_OF_BREATH_options)
        
    with col2:
        SWALLOWING_DIFFICULTY_options = ['1  No', '2  Yes']  
        SWALLOWING_DIFFICULTY = st.selectbox('Swallowing Difficulty  ', SWALLOWING_DIFFICULTY_options)
        
    with col3:
        CHEST_PAIN_options = ['1  No', '2  Yes']  
        CHEST_PAIN	 = st.selectbox('Chest Pain ', CHEST_PAIN_options)
        
    


    # code for Prediction
    lung_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Lung Cancer Test Result"):
        if not all([GENDER,	AGE	,SMOKING	,YELLOW_FINGERS	,ANXIETY	,PEER_PRESSURE,	CHRONIC_DISEASE,	FATIGUE,	ALLERGY,	WHEEZING,	ALCOHOL_CONSUMING,	COUGHING,	SHORTNESS_OF_BREATH	,SWALLOWING_DIFFICULTY,	CHEST_PAIN	]):
            st.warning("Please fill in all the fields.")
        else:
            # Convert the selected values to integers
            GENDER = ''.join(char for char in GENDER if char.isdigit())
            GENDER = int(GENDER) if  GENDER else None
            
            for char in AGE:
                if char.isdigit():
                    AGE += char
                elif AGE:
                    break
            AGE = ''.join(char for char in AGE if char.isdigit())
            AGE = int(AGE) if AGE else None
            
            
            SMOKING = ''.join(char for char in SMOKING if char.isdigit())
            SMOKING = int(SMOKING) if  SMOKING else None
            
            YELLOW_FINGERS = ''.join(char for char in YELLOW_FINGERS if char.isdigit())
            YELLOW_FINGERS = int(YELLOW_FINGERS) if  YELLOW_FINGERS else None
            
            ANXIETY = ''.join(char for char in ANXIETY  if char.isdigit())
            ANXIETY = int(ANXIETY ) if  ANXIETY else None
            
            PEER_PRESSURE = ''.join(char for char in PEER_PRESSURE if char.isdigit())
            PEER_PRESSURE = int(PEER_PRESSURE) if PEER_PRESSURE else None
            
            CHRONIC_DISEASE = ''.join(char for char in CHRONIC_DISEASE if char.isdigit())
            CHRONIC_DISEASE = int(CHRONIC_DISEASE) if CHRONIC_DISEASE else None
            
            FATIGUE = ''.join(char for char in FATIGUE if char.isdigit())
            FATIGUE = int(FATIGUE) if  FATIGUE else None
            
            ALLERGY = ''.join(char for char in ALLERGY if char.isdigit())
            ALLERGY = int(ALLERGY) if  ALLERGY else None
            
            WHEEZING = ''.join(char for char in WHEEZING if char.isdigit())
            WHEEZING = int(WHEEZING) if WHEEZING else None
            
            ALCOHOL_CONSUMING = ''.join(char for char in ALCOHOL_CONSUMING if char.isdigit())
            ALCOHOL_CONSUMING = int(ALCOHOL_CONSUMING) if ALCOHOL_CONSUMING else None
            
            COUGHING = ''.join(char for char in COUGHING if char.isdigit())
            COUGHING = int(COUGHING) if  COUGHING else None
            
            SHORTNESS_OF_BREATH = ''.join(char for char in SHORTNESS_OF_BREATH if char.isdigit())
            SHORTNESS_OF_BREATH = int(SHORTNESS_OF_BREATH) if  SHORTNESS_OF_BREATH else None
            
            SWALLOWING_DIFFICULTY = ''.join(char for char in SWALLOWING_DIFFICULTY if char.isdigit())
            SWALLOWING_DIFFICULTY = int(SWALLOWING_DIFFICULTY) if  SWALLOWING_DIFFICULTY else None
            
            CHEST_PAIN = ''.join(char for char in CHEST_PAIN  if char.isdigit())
            CHEST_PAIN = int(CHEST_PAIN ) if  CHEST_PAIN  else None
           
            
        
            # Make the prediction
            lung_prediction = lung_model.predict([[GENDER,	AGE	,SMOKING	,YELLOW_FINGERS	,ANXIETY	,PEER_PRESSURE,	CHRONIC_DISEASE,	FATIGUE,	ALLERGY,	WHEEZING,	ALCOHOL_CONSUMING,	COUGHING,	SHORTNESS_OF_BREATH	,SWALLOWING_DIFFICULTY,	CHEST_PAIN]])                          
            
            if lung_prediction[0] == 1:
                lung_diagnosis = "The person have chances of Lung Cancer"
            else:
                lung_diagnosis = "The person does not have chances of Lung Cancer"
        
    st.success(lung_diagnosis)

  

    







    




