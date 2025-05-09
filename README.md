The project leverages a natural language interface (NLI) that enables users to interact with both RDBMS (e.g., MySQL) and NoSQL (e.g., MongoDB) databases using natural language queries. The system interprets user inputs, predicts user intent and converts them into database queries using OpenAI API(GPT4). The system will execute those queries, and return the results to the users. 

Begin by uploading all Python files in the project (e.g., main.py, openaiapi.py, mysql_utils.py, etc.) to your Ubuntu environment.

Upload and import your CSV files (e.g., world_cup.csv, world_cup_1930_2022.csv) into MySQL, and your JSON files (e.g., IMDB_movie_details.json, IMDB_reviews.json) into MongoDB using mongoimport.

Create and activate a virtual environment in ubuntu: 'python3 -m venv venv', then 'source venv/bin/activate'

In the terminal, navigate to your project folder and execute the main script: "python3 main.py"

When prompted, enter your query in natural language, for example:"Which team won the World Cup in 2018?"

After typing your question, you’ll be asked to choose the database backend: 'mysql' or 'mongod'

The terminal will then display the executed query and its result.
