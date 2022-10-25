import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from pyscrs import createModel

def predict(team1, team2, usrvenue, usrtoss, decide):
    # np.random.seed(47)
    # df_ipl = pd.read_csv("IPL_Win_Pred.csv")
    

    # X = df_ipl.drop("WinningTeam", axis=1)
    # y = df_ipl["WinningTeam"]

    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # model = GradientBoostingClassifier()
    # model.fit(X_train, y_train)

    # model.score(X_test, y_test)

    # pickle.dump(model, open("mymodel.pkl", "wb"))
    try:
        model = pickle.load(open("data/mymodel.pkl", "rb"))
        model.predict([[3, 2, 1, 3, 1]])
    except Exception:
        createModel.trainModel()
        model = pickle.load(open("data/mymodel.pkl", "rb"))
    

    team = {}
    team_cat = ['Gujarat Titans', 'Rajasthan Royals', 'Lucknow Super Giants', 'Punjab Kings', 'Mumbai Indians', 'Royal Challengers Bangalore', 'Kolkata Knight Riders', 'Sunrisers Hyderabad', 'Delhi Capitals', 'Chennai Super Kings', 'Kings XI Punjab', 'Delhi Daredevils', 'Rising Pune Supergiant', 'Gujarat Lions', 'Rising Pune Supergiants', 'Pune Warriors', 'Deccan Chargers', 'Kochi Tuskers Kerala']
    for i in range(0, len(team_cat)):
        team[team_cat[i]] = i+1

    toss = {
    "Batting": 1,
    "Fielding": 2
    }

    venue = {}
    venue_cat = ['Narendra Modi Stadium, Ahmedabad', 'Eden Gardens, Kolkata', 'Wankhede Stadium, Mumbai', 'Brabourne Stadium, Mumbai', 'Dr DY Patil Sports Academy, Mumbai', 'Maharashtra Cricket Association Stadium, Pune', 'Dubai International Cricket Stadium', 'Sharjah Cricket Stadium', 'Zayed Cricket Stadium, Abu Dhabi', 'Arun Jaitley Stadium, Delhi', 'MA Chidambaram Stadium, Chepauk, Chennai', 'Sheikh Zayed Stadium', 'Rajiv Gandhi International Stadium', 'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium', 'MA Chidambaram Stadium', 'Punjab Cricket Association IS Bindra Stadium', 'Wankhede Stadium', 'M.Chinnaswamy Stadium', 'Arun Jaitley Stadium', 'Eden Gardens', 'Sawai Mansingh Stadium', 'Maharashtra Cricket Association Stadium', 'Holkar Cricket Stadium', 'Rajiv Gandhi International Stadium, Uppal', 'M Chinnaswamy Stadium', 'Feroz Shah Kotla', 'Green Park', 'Punjab Cricket Association IS Bindra Stadium, Mohali', 'Saurashtra Cricket Association Stadium', 'Shaheed Veer Narayan Singh International Stadium', 'JSCA International Stadium Complex', 'Brabourne Stadium', 'Punjab Cricket Association Stadium, Mohali', 'MA Chidambaram Stadium, Chepauk', 'Sardar Patel Stadium, Motera', 'Barabati Stadium', 'Subrata Roy Sahara Stadium', 'Himachal Pradesh Cricket Association Stadium', 'Dr DY Patil Sports Academy', 'Nehru Stadium', 'Vidarbha Cricket Association Stadium, Jamtha', 'New Wanderers Stadium', 'SuperSport Park', 'Kingsmead', 'OUTsurance Oval', "St George's Park", 'De Beers Diamond Oval', 'Buffalo Park', 'Newlands']
    for i in range(0, len(venue_cat)):
        venue[venue_cat[i]] = i+1
    print("---------------------------------------------------")
    print(team[team1], team[team2], venue[usrvenue], team[usrtoss], toss[decide])
    wins = model.predict([[team[team1], team[team2], venue[usrvenue], team[usrtoss], toss[decide]]])
    # wins = model.predict([[team["Mumbai Indians"], team["Chennai Super Kings"], venue["Brabourne Stadium"], team["Mumbai Indians"], toss["Fielding"]]])

    winner = ""
    for i in team:
        if team[i] == wins[0]:
            winner = i
            break
    print(winner)
    return winner