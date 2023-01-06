import pandas as pd
'''pandas'''
import numpy as np
'''numpy'''
#from sklearn import train_test_split
'''traintestsplit'''
def null_count(df):
    ''' docstring'''
    df = pd.DataFrame(df)
    num = int(df.isnull().sum())
    return num

def train_test_split_func(df,target,frac):
    '''docstring'''
    X = df.drop(target,axis=1) 
    y = df[target]
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=frac)
    return X_train,X_test,y_train,y_test

def randomize(df,seed):
    '''docstring'''
    df.sample(frac=1,random_state=seed)
    return df

def random_df(col=1,row=1,range=100):
    '''docstring'''
    df = pd.DataFrame(np.random.randint(0,range,size=(row,col)))
    return df


'''def addr_split(series): #doesn't work yet
    import re
    city = []
    state = []
    zip = []    
    for i in range(len(series)):
        city.append(re.findall(string = series[i],pattern=r'(?!.*\S)'))
        zip.append(re.findall(string = series[i],pattern='(\d+)(?!.*\w)'))'''
     

def abbr_2_state(series):
    '''docstring'''
    stateslist = {'Alabama':'AL','Kentucky':'KY', 'Ohio':'OH','Alaska':	'AK',
                  'Louisiana':'LA','Oklahoma':'OK','Arizona':'AZ','Maine':'ME',
                  'Oregon':'OR','Arkansas':'AR','Maryland':'MD','Pennsylvania':'PA',
                  'American Samoa':'AS','Massachusetts':'MA','Puerto Rico':'PR',
                  'California':'CA','Michigan':'MI','Rhode Island':'RI',
                  'Colorado':'CO','Minnesota':'MN','South Carolina':'SC',
                  'Connecticut':'CT','Mississippi':	'MS','South Dakota':'SD',
                  'Delaware':'DE','Missouri':'MO','Tennessee':'TN',
                  'District of Columbia':'DC','Montana':'MT','Texas':'TX',
                  'Florida':'FL','Nebraska':'NE','Trust Territories':'TT',
                  'Georgia':'GA','Nevada':'NV',	'Utah':	'UT',
                  'Guam':'GU','New Hampshire':'NH','Vermont':'VT',
                  'Hawaii':'HI','New Jersey':'NJ','Virginia':'VA',
                  'Idaho':'ID',	'New Mexico':'NM','Virgin Islands':'VI',
                  'Illinois':'IL','New York':'NY','Washington':'WA',
                  'Indiana':'IN','North Carolina':'NC','West Virginia':'WV',
                  'Iowa':'IA','North Dakota':'ND','Wisconsin':'WI',
                  'Kansas':	'KS','Northern Mariana Islands':'CM','Wyoming':'WY'}
    newlist = []
    for i,j in enumerate(series):
        try:
            if series[i] in stateslist.keys():
                newlist.append(list(stateslist.values())[list(stateslist.keys()).index(series[i])])
            else:
                newlist.append(list(stateslist.keys())[list(stateslist.values()).index(series[i])])  
        except ValueError:
            print('Make sure states or abbreviations are spelled correctly')
    return newlist
def random_bowling_score():
    '''needs to return a random bowling score between 0 and 300'''
    return np.random.randint(0,301)