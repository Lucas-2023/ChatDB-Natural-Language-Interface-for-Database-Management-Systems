import openai
from config import OPENAI_API_KEY, GPT_MODEL

openai.api_key = OPENAI_API_KEY

def convert_to_sql(nl_query):
    prompt = f"""You are a helpful assistant that converts natural language into SQL queries.
Use standard SQL syntax compatible with MySQL.
Do not include explanations or natural language, only output the SQL code.

You have access to two tables:

1. matches — contains detailed match-level information for all FIFA World Cup games, including t
eams, scores, referees, dates, cards, goals, and substitutions.

The fields in this table are:

match_id

home_team, away_team

home_score, away_score

home_xg, away_xg

home_penalty, away_penalty

home_manager, away_manager

home_captain, away_captain

Attendance, Venue, Officials, Round, Date, Score, Referee, Notes, Host, Year

home_goal, away_goal

home_goal_long, away_goal_long

home_own_goal, away_own_goal

home_penalty_goal, away_penalty_goal

home_penalty_miss_long, away_penalty_miss_long

home_penalty_shootout_goal_long, away_penalty_shootout_goal_long

home_penalty_shootout_miss_long, away_penalty_shootout_miss_long

home_red_card, away_red_card

home_yellow_red_card, away_yellow_red_card

home_yellow_card_long, away_yellow_card_long

home_substitute_in_long, away_substitute_in_long

2. world_cup — contains year-level summary data for each World Cup tournament, including the host country, winner, runner-up, total teams, attendance, and top scorers.

The fields in this table are:

Year

Host

Teams

Champion

Runner_Up

TopScorer

Attendance

AttendanceAvg

Matches

Natural Language: {nl_query}
SQL:"""

    response = openai.ChatCompletion.create(
        model=GPT_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1
    )
    return response['choices'][0]['message']['content'].strip()

def convert_to_mongo(nl_query):
    prompt = f"""You are a MongoDB expert that converts natural language to MongoDB queries using PyMongo syntax.
Use either find() or aggregate() with stages like $match, $group, $project, and $lookup.
Only return the Python code for db.collection.find(...) or db.collection.aggregate([...]).
Do not include explanations.

Natural Language: {nl_query}
MongoDB Query:"""

    response = openai.ChatCompletion.create(
        model=GPT_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1
    )
    return response['choices'][0]['message']['content'].strip()