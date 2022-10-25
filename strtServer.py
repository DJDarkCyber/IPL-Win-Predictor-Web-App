from flask import Flask, redirect, url_for, render_template, request
from pyscrs import predictWins, getGraphDetails
from flask import Flask, request, render_template

app = Flask('__name__')

app.secret_key = "437437437437"

@app.route("/")
def indexPage():
    return render_template("index.html")

@app.route("/predictWinnings", methods=["POST", "GET"])
def predictWinner():
    if request.method == "GET":
        team = ['Gujarat Titans', 'Rajasthan Royals', 'Lucknow Super Giants', 'Punjab Kings', 'Mumbai Indians', 'Royal Challengers Bangalore', 'Kolkata Knight Riders', 'Sunrisers Hyderabad', 'Delhi Capitals', 'Chennai Super Kings', 'Kings XI Punjab', 'Delhi Daredevils', 'Rising Pune Supergiant', 'Gujarat Lions', 'Rising Pune Supergiants', 'Pune Warriors', 'Deccan Chargers', 'Kochi Tuskers Kerala']
        venue = ['Narendra Modi Stadium, Ahmedabad', 'Eden Gardens, Kolkata', 'Wankhede Stadium, Mumbai', 'Brabourne Stadium, Mumbai', 'Dr DY Patil Sports Academy, Mumbai', 'Maharashtra Cricket Association Stadium, Pune', 'Dubai International Cricket Stadium', 'Sharjah Cricket Stadium', 'Zayed Cricket Stadium, Abu Dhabi', 'Arun Jaitley Stadium, Delhi', 'MA Chidambaram Stadium, Chepauk, Chennai', 'Sheikh Zayed Stadium', 'Rajiv Gandhi International Stadium', 'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium', 'MA Chidambaram Stadium', 'Punjab Cricket Association IS Bindra Stadium', 'Wankhede Stadium', 'M.Chinnaswamy Stadium', 'Arun Jaitley Stadium', 'Eden Gardens', 'Sawai Mansingh Stadium', 'Maharashtra Cricket Association Stadium', 'Holkar Cricket Stadium', 'Rajiv Gandhi International Stadium, Uppal', 'M Chinnaswamy Stadium', 'Feroz Shah Kotla', 'Green Park', 'Punjab Cricket Association IS Bindra Stadium, Mohali', 'Saurashtra Cricket Association Stadium', 'Shaheed Veer Narayan Singh International Stadium', 'JSCA International Stadium Complex', 'Brabourne Stadium', 'Punjab Cricket Association Stadium, Mohali', 'MA Chidambaram Stadium, Chepauk', 'Sardar Patel Stadium, Motera', 'Barabati Stadium', 'Subrata Roy Sahara Stadium', 'Himachal Pradesh Cricket Association Stadium', 'Dr DY Patil Sports Academy', 'Nehru Stadium', 'Vidarbha Cricket Association Stadium, Jamtha', 'New Wanderers Stadium', 'SuperSport Park', 'Kingsmead', 'OUTsurance Oval', "St George's Park", 'De Beers Diamond Oval', 'Buffalo Park', 'Newlands']
        return render_template("predictWins.html", teams=team, desc=["Batting", "Fielding"], venues=venue)
    
    elif request.method == "POST":
        team1 = request.form["TEAM1"]
        team2 = request.form["TEAM2"]
        venue = request.form["VENUE"]
        toss = request.form["TOSS"]
        desc = request.form["DESC"]

        print("----")
        print(team1, team2)

        winner = predictWins.predict(team1, team2, venue, toss, desc)

        team1Wins, team2Wins = getGraphDetails.noOfTeamWins(team1, team2)
        venue_team1, venue_team2, venue_team1_wins, venue_team2_wins = getGraphDetails.getWinsAtVenue(team1, team2)
        print(team1Wins, team2Wins)

        team1_venue_win, team2_venue_win = getGraphDetails.getOpponentWinsVenu(team1, team2)

        return render_template("predictedWinner.html", win=winner, team1Wins=team1Wins, team2Wins=team2Wins, team1=team1, team2=team2, 
                                                venue_team1=venue_team1, venue_team2=venue_team2, venue_team1_wins=venue_team1_wins, venue_team2_wins=venue_team2_wins,
                                                team1_venue_win=team1_venue_win, team2_venue_win=team2_venue_win)

if __name__ == '__main__':
    app.run(debug=True)