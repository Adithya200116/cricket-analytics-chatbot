import pandas as pd
from flask import Flask, render_template, request, jsonify
import joblib  # For loading the trained model

# Load your CSV files into pandas DataFrames
df = pd.read_csv("data/batting.csv")
bowling_df = pd.read_csv("data/bowling.csv")
match_schedule_df = pd.read_csv("data/match_schedule_results.csv")  # Added match_schedule.csv
playerdetails_df = pd.read_csv("data/player-details.csv")

# Load the pre-trained ML model (example with a scikit-learn model)
ml_model = joblib.load("models/trained_model.pkl")

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.get_json()['question']
    answer = get_answer_from_csv(user_input)
    return jsonify({'answer': answer})

def get_answer_from_csv(query):
    query = query.lower()

 # Check if the question is about runs
    if "runs" in query:
        for batsman in df['Batsman_Name'].unique():
            if batsman.lower() in query:
                result = df[df['Batsman_Name'].str.lower() == batsman.lower()]
                total_runs = result['Runs'].sum()
                return f"{batsman} scored {total_runs} runs."
        for match in df['Match_no'].unique():
            if f"match {match}" in query:
                match_data = df[df['Match_no'] == match]
                total_runs_in_match = match_data['Runs'].sum()
                return f"Total runs in Match {match}: {total_runs_in_match}"

    # Check if the question is about the strike rate
    if "strike rate" in query:
        for batsman in df['Batsman_Name'].unique():
            if batsman.lower() in query:
                result = df[df['Batsman_Name'].str.lower() == batsman.lower()]
                strike_rate = result['Strike_Rate'].iloc[0]
                return f"{batsman}'s strike rate: {strike_rate}"

    # Check if the question is about batting position
    if "batting position" in query:
        for batsman in df['Batsman_Name'].unique():
            if batsman.lower() in query:
                result = df[df['Batsman_Name'].str.lower() == batsman.lower()]
                batting_position = result['Batting_Position'].iloc[0]
                return f"{batsman}'s batting position: {batting_position}"

    # Check if the question is about 4s or 6s
    if "fours" in query or "4s" in query:
        for batsman in df['Batsman_Name'].unique():
            if batsman.lower() in query:
                result = df[df['Batsman_Name'].str.lower() == batsman.lower()]
                total_fours = result['4s'].sum()
                return f"{batsman} hit {total_fours} fours."
    if "sixes" in query or "6s" in query:
        for batsman in df['Batsman_Name'].unique():
            if batsman.lower() in query:
                result = df[df['Batsman_Name'].str.lower() == batsman.lower()]
                total_sixes = result['6s'].sum()
                return f"{batsman} hit {total_sixes} sixes."

    # Check if the question is about dismissal 
    if "dismissed" in query or "out" in query:
        for batsman in df['Batsman_Name'].unique():
            if batsman.lower() in query:
                result = df[df['Batsman_Name'].str.lower() == batsman.lower()]
                dismissal_type = result['Dismissal'].iloc[0]
                return f"{batsman}'s dismissal: {dismissal_type}"

    # Check if the question is about balls faced
    if "balls faced" in query:
        for batsman in df['Batsman_Name'].unique():
            if batsman.lower() in query:
                result = df[df['Batsman_Name'].str.lower() == batsman.lower()]
                total_balls = result['Balls'].sum()
                return f"{batsman} faced {total_balls} balls."

    # Check if the question is about match details (batsmen in match)
    if "batsmen in match" in query or "batted" in query:
        for match in df['Match_no'].unique():
            if f"match {match}" in query:
                match_data = df[df['Match_no'] == match]
                batsmen_in_match = match_data['Batsman_Name'].unique()
                return f"Batsmen in Match {match}: {', '.join(batsmen_in_match)}"
            
    # Check if the question is about team innings-specific questions
    if "team innings" in query:
        for team_innings in df['Team_Innings'].unique():
            if team_innings.lower() in query:
                team_data = df[df['Team_Innings'].str.lower() == team_innings.lower()]
                total_runs = team_data['Runs'].sum()
                return f"{team_innings} scored a total of {total_runs} runs."

            
    # Total runs conceded by a bowler
    if "runs conceded" in query or "runs given" in query:
        for bowler in bowling_df['Bowler_Name'].unique():
            if bowler.lower() in query:
                result = bowling_df[bowling_df['Bowler_Name'].str.lower() == bowler.lower()]
                total_runs = result['Runs'].sum()
                return f"{bowler} conceded {total_runs} runs."

    # Total wickets taken by a bowler
    if "wickets" in query:
        for bowler in bowling_df['Bowler_Name'].unique():
            if bowler.lower() in query:
                result = bowling_df[bowling_df['Bowler_Name'].str.lower() == bowler.lower()]
                total_wickets = result['Wickets'].sum()
                return f"{bowler} took {total_wickets} wickets."

    # Economy rate of a bowler
    if "economy" in query:
        for bowler in bowling_df['Bowler_Name'].unique():
            if bowler.lower() in query:
                result = bowling_df[bowling_df['Bowler_Name'].str.lower() == bowler.lower()]
                economy = result['Economy'].mean()
                return f"{bowler}'s economy rate is {economy:.2f}."

    # Overs bowled by a bowler
    if "overs" in query:
        for bowler in bowling_df['Bowler_Name'].unique():
            if bowler.lower() in query:
                result = bowling_df[bowling_df['Bowler_Name'].str.lower() == bowler.lower()]
                total_overs = result['Overs'].sum()
                return f"{bowler} bowled {total_overs} overs."

    # Maidens bowled by a bowler
    if "maidens" in query:
        for bowler in bowling_df['Bowler_Name'].unique():
            if bowler.lower() in query:
                result = bowling_df[bowling_df['Bowler_Name'].str.lower() == bowler.lower()]
                total_maidens = result['Maidens'].sum()
                return f"{bowler} bowled {total_maidens} maiden overs."

    # Best performance of a bowler in a specific match
    if "best performance" in query or "best figures" in query:
        for bowler in bowling_df['Bowler_Name'].unique():
            if bowler.lower() in query:
                result = bowling_df[bowling_df['Bowler_Name'].str.lower() == bowler.lower()]
                best_match = result.loc[result['Wickets'].idxmax()]
                return (f"{bowler}'s best performance: {best_match['Wickets']} wickets for "
                        f"{best_match['Runs']} runs in Match {best_match['Match_no']}.")
    
    # Match details queries
    if "match details" in query.lower():
        for match in df['Match_no'].unique():
            if f"match {match}" in query.lower():
                match_data = df[df['Match_no'] == match]
                return f"Details of Match {match}: {match_data['Match_Between'].iloc[0]}"

            
    # Match details queries
    if "who won in" in query and "match" in query.lower():
        for match in match_schedule_df['Match_no'].unique():
            if f"match {match}" in query:
                match_data = match_schedule_df[match_schedule_df['Match_no'] == match]
                winner = match_data['Winner'].iloc[0]
                return f"The winner of Match {match} is {winner}."

    if "when and where" in query and "match" in query.lower():
        for match in match_schedule_df['Match_no'].unique():
            if f"match {match}" in query:
                match_data = match_schedule_df[match_schedule_df['Match_no'] == match]
                date = match_data['Date'].iloc[0]
                venue = match_data['Venue'].iloc[0]
                return f"Match {match} was played on {date} at {venue}."

    if "which teams played" in query and "match" in query.lower():
        for match in match_schedule_df['Match_no'].unique():
            if f"match {match}" in query:
                match_data = match_schedule_df[match_schedule_df['Match_no'] == match]
                print(match_data.columns)  # This will print the column names to the console
                team1 = match_data['T1'].iloc[0]
                team2 = match_data['T2'].iloc[0]
                return f"The teams in Match {match} were {team1} and {team2}."
            

    if "player details" in query or "details of":
        for player in playerdetails_df['player_name'].unique():
            if player.lower() in query:
                player_data = playerdetails_df[playerdetails_df['player_name'].str.lower() == player.lower()]
                player_details = player_data.iloc[0]
                return (
                    f"Player Name: {player_details['player_name']}<br/>\n"
                    f"Team: {player_details['team_name']}<br/>\n"
                    f"Image: <a class='photo-link' href='{player_details['image_of_player']}' target='_blank'>{player_details['image_of_player']}</a><br/>\n"
                    f"Batting Style: {player_details['battingStyle']}<br/>\n"
                    f"Bowling Style: {player_details['bowlingStyle']}<br/>\n"
                    f"Playing Role: {player_details['playingRole']}<br/>\n"
                    f"Description: {player_details['description']}"
                )
            

    if "world cup in 2023" in  query.lower() or "world cup" in query.lower():
        return "The winner of the 2023 World Cup was Australia."
    
    # Check if the question matches any predefined patterns and answer accordingly (CSV logic)
    # You can copy your existing CSV logic here

    # Fallback to ML model if no answer found from CSV logic
    return get_answer_from_ml(query)

def get_answer_from_ml(query):
    # Use the trained ML model to predict the answer for the given query
    # Let's assume your model returns a category like "runs", "wickets", etc.
    model_prediction = ml_model.predict([query])  # Assuming your model takes a list of text inputs
    category = model_prediction[0]

    # Now, based on the predicted category, you can return a response
    if category == "runs":
        return "I'm still learning about runs data!"
    elif category == "wickets":
        return "I'm still learning about wickets data!"
    elif category == "match details":
        return "I'm still learning about match details!"
    else:
        return "I'm still learning about cricket!"  # Default response

if __name__ == "__main__":
    app.run(debug=True)
