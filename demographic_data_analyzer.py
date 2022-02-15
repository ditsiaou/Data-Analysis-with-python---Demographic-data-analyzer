import pandas as pd
import sys
import numpy as np
def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv',delimiter=',')
    print(df.head(),df.columns)
    #sys.exit()
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()
    #print(race_count)
    #sys.exit()
    # What is the average age of men?
    men=df['age'].values[(( df['sex']=='Male'))] #θέλω #add
    #print(len(men)) #the len is ok checked
    #sys.exit()
    average_age_men = round(men.mean(),1)
    print(average_age_men)
    #sys.exit() 
    #until here we are ok
    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(100*len(df.values[(( df['education']=='Bachelors'))])/len(df.values),1)
    print((percentage_bachelors))
    #sys.exit()
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    #higher_education = df.values[np.logical_or(df['education'].values== 'Bachelors', df['education'].values=='Masters',df['education'].values=='Doctorate')]
    #higher_education=pd.DataFrame(df.values[np.logical_or(df['education'].values== 'Bachelors', df['education'].values=='Masters',df['education'].values=='Doctorate')],columns=df.columns)
    higher_education=pd.DataFrame(df.values[np.logical_or(df['education'].values== 'Bachelors', np.logical_or(df['education'].values=='Masters',df['education'].values=='Doctorate'))],columns=df.columns)
    print(higher_education['education'].value_counts())
    #sys.exit()
    #print(type(higher_education),type(df['education']))
    #sys.exit()ion) 
    #lower_education= df.values[(np.logical_and(df['education'].values!= 'Bachelors', df['education'].values!='Masters',df['education'].values!='Doctorate'))]
    lower_education=pd.DataFrame(df.values[np.logical_and(df['education'].values!= 'Bachelors',np.logical_and(df['education'].values!='Masters',df['education'].values!='Doctorate'))],columns=df.columns)
    len_lower_education=len(lower_education)
    print(lower_education['education'].value_counts())
    print(len(df),len(higher_education)+len(lower_education)) #obviously len(df) equals with the two other categories together
    #sys.exit()
    # percentage with salary >50K
    higher_education_richnopercentage= higher_education.values[higher_education['salary']=='>50K']
    #print(len(higher_education_richnopercentage))
    #sys.exit()
    higher_education_rich = round((100*len(higher_education_richnopercentage)/len(higher_education)),1)
    print(higher_education_rich)
    #sys.exit()
    lower_education_richnopercentage= lower_education.values[lower_education['salary']=='>50K']
    print(len(lower_education_richnopercentage))
    lower_education_rich = round(100*len(lower_education_richnopercentage)/len(lower_education),1)
    print(lower_education_rich)
    #sys.exit()
    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()
    #min_work_hours = pd.DataFrame(df.values[df['hours-per-week'].values]==df['hours-per-week'].min())
    df_min_work_hours=df[df["hours-per-week"] == min_work_hours] # αυτό δουλευει
    #df_min_work_hours=pd.DataFrame(np.where(df['hours-per-week']==min_work_hours),columns=df.columns)
    print(type(df_min_work_hours),df_min_work_hours)
    
    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df_min_work_hours
    rich=num_min_workers[num_min_workers["salary"] == '>50K']
    print(type(rich))
    rich_percentage = 100*len(rich)/(len(num_min_workers))
    print(rich_percentage)
    #sys.exit()
    # What country has the highest percentage of people that earn >50K?
    rich_people=pd.DataFrame(df.values[(( df['salary']=='>50K'))],columns=df.columns)
    print(type(rich_people),rich_people.head())
    race_rich_count = rich_people['native-country'].value_counts()

    print(race_rich_count,type(race_rich_count))
    #sys.exit()
    earning_country_percentage = 100*race_rich_count/(df['native-country'].value_counts()) #interesting that it works
    highest_earning_country=earning_country_percentage.idxmax()
    print(highest_earning_country)
    
    highest_earning_country_percentage = round(earning_country_percentage.max(),1)
    print(highest_earning_country_percentage)
    
    # Identify the most popular occupation for those who earn >50K in India.
    rich_Indians=pd.DataFrame(df.values[np.logical_and(df['native-country'].values== 'India', df['salary'].values=='>50K')],columns=df.columns)
    
    rich_Indians_occupations=rich_Indians['occupation'].value_counts()
    top_IN_occupation = rich_Indians_occupations.idxmax()
    print(top_IN_occupation)
    #sys.exit()
    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
