from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler
app=Flask(__name__,template_folder='template')
model=pickle.load(open('CreditCard_model.pkl', 'rb'))
@app.route('/',methods=['get'])
def Home():
    return render_template('index.html')

standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
     
    if request.method == 'POST':
        npa = int(request.form['NPASTATUS'])
        ruoul=float(request.form['RUOUL'])
        Age=int(request.form['age'])
        Gender=request.form['gender']
        gender_type=0
        if(Gender=='Male'):
                gender_type=0
        else:
                gender_type=1
                
        region_type=0
        Region=request.form['region']
        if(Region=='Central'):
                region_type=4
        elif(Region=='North'):
                region_type=1
        elif(Region=='West'):
                region_type=2
        elif(Region=='South'):
                region_type=0
        else:
                region_type=3
        house_type=0
        House=request.form['rentedhouse']
        if(House=='ownhouse'):
                house_type=0
        else:
                house_type=1
                
        occupation_type=0
        Occupation=request.form['occupation']
        if(Occupation=='selfemployed'):
            occupation_type=0
        elif(Occupation=='Officer'):
            occupation_type=1
        else:
            occupation_type=2
        educaton_type=0    
        Education=request.form['education']
        if(Education=='matric'):
                educaton_type=0
        elif(Education=='graduate'):
                educaton_type=1
        elif(Education=='phd'):
                educaton_type=2
        elif(Education=='professional'):
                educaton_type=3
        else:
                educaton_type=4
                
        monthly_income = float(request.form['monthlyincome'])
        notdunw = int(request.form['NOTDUNW'])
        Debtratio = float(request.form['debtratio'])
        nooclal = int(request.form['NOOCLAL'])
        nrelol = int(request.form['NRELOL'])
        nod = int(request.form['NOD'])
        data =pd.DataFrame(data=[[npa,ruoul,Age,gender_type,region_type,monthly_income,house_type,occupation_type,educaton_type,notdunw,Debtratio,nooclal,nrelol,nod]],columns=['NPA Status','RevolvingUtilizationOfUnsecuredLines','age','Gender','Region','MonthlyIncome','Rented_OwnHouse','Occupation','Education','NumberOfTime30-59DaysPastDueNotWorse','DebtRatio','NumberOfOpenCreditLinesAndLoans','NumberRealEstateLoansOrLines','NumberOfDependents'])
        prediction=model.predict(data)
        output=(prediction[0])
        #return render_template('index.html',prediction_text='Employee Salary should be $ {}'.format(output))
        if(output==1):
           return render_template('index.html',prediction_text="Costumer is good for Credit Card")
        else:
           return render_template('index.html',prediction_text="Sorry Costumer is bad for Credit Card")
    else:
       return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

