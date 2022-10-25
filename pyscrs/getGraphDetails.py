import pandas as pd

def noOfTeamWins(team1, team2):
    print("********")
    print(team1 + " | "+ team2)
    df_req = pd.read_csv("data/IPL-Req-Data.csv")
    team1_wins = []
    for i in range(0, len(df_req["Team1"])):
        if df_req["Team1"][i] == team1 or df_req["Team2"][i] == team1:
            if df_req["Team1"][i] == team2 or df_req["Team2"][i] == team2:
                team1_wins.append(df_req["WinningTeam"][i])
    
    team1_wins = pd.Series(team1_wins)
    team1_wins.value_counts()

    team1_wined = 0
    team2_wined = 0

    try:
        team1_wined = team1_wins.value_counts()[team1]
    except Exception:
        team1_wined = 0
    
    try:
        team2_wined =  team1_wins.value_counts()[team2]
    except Exception:
        team2_wined =0

    return team1_wined, team2_wined


def getWinsAtVenue(team1_, team2_):
    df_req = pd.read_csv("data/IPL-Req-Data.csv")
    team1 = 0
    team1_wined = 0
    team2 = 0
    team2_wined = 0
    for i in range(0, len(df_req)):
        if df_req["Team1"][i] == team1_ or df_req["Team2"][i] == team1_:
            if df_req["Venue"][i] == "Eden Gardens":
                team1 = team1 + 1
                if df_req["WinningTeam"][i] == team1_:
                    team1_wined = team1_wined + 1
    
    for i in range(0, len(df_req)):
        if df_req["Team1"][i] == team2_ or df_req["Team2"][i] == team2_:
            if df_req["Venue"][i] == "Eden Gardens":
                team2 = team2 + 1
                if df_req["WinningTeam"][i] == team2_:
                    team2_wined = team2_wined + 1

    return team1, team2, team1_wined, team2_wined

def getOpponentWinsVenu(team1_, team2_):
    df_req = pd.read_csv("data/IPL-Req-Data.csv")
    team1_venue_win = 0
    team2_venue_win = 0
    for i in range(0, len(df_req["Team1"])):
        if df_req["Team1"][i] == team1_ or df_req["Team2"][i] == team1_:
            if df_req["Team1"][i] == team2_ or df_req["Team2"][i] == team2_:
                if df_req["Venue"][i] == "Eden Gardens":
                    if df_req["WinningTeam"][i]== team1_:
                        team1_venue_win = team1_venue_win + 1
                    elif df_req["WinningTeam"][i] == team2_:
                        team2_venue_win = team2_venue_win + 1
    

    # for i in range(0, len(df_req["Team1"])):
    #     if df_req["Team1"][i] == "Kolkata Knight Riders" or df_req["Team2"][i] == "Kolkata Knight Riders":
    #         if df_req["Team1"][i] == "Mumbai Indians" or df_req["Team2"][i] == "Mumbai Indians":
    #             if df_req["Venue"][i] == "Eden Gardens":
    #                 if df_req["WinningTeam"][i]== "Mumbai Indians":
    #                     team2_venue_win = team2_venue_win + 1

    return team1_venue_win, team2_venue_win