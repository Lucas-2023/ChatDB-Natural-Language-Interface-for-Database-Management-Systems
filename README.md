Introduction: The project leverages a natural language interface (NLI) that enables users to interact with both RDBMS (e.g., MySQL) and NoSQL (e.g., MongoDB) databases using natural language queries. The system interprets user inputs, predicts user intent and converts them into database queries using OpenAI API(GPT4). The system will execute those queries, and return the results to the users. 

Before running the program, make sure your Ubuntu environment has the necessary tools and configurations. You should have Python 3 and pip installed, along with the python3-venv module to create and manage virtual environments. In addition, install MySQL Server and MongoDB, both of which should be up and running. You’ll also need the MongoDB import tools (mongo-tools) to load JSON data into MongoDB.

Once the environment is prepared, create a virtual environment with python3 -m venv venv and activate it using source venv/bin/activate. Inside the environment, install the required Python packages using pip install openai pymongo mysql-connector-python pandas. Finally, ensure you have a valid OpenAI API key for GPT-4 access. This key can either be hardcoded in your config.py file or set as an environment variable using export OPENAI_API_KEY="your-key".

Begin by uploading all Python files in the project (e.g., main.py, openaiapi.py, mysql_utils.py, etc.) to your Ubuntu environment.

Upload and import your CSV files (e.g., world_cup.csv, world_cup_1930_2022.csv) into MySQL, and your JSON files (e.g., IMDB_movie_details.json, IMDB_reviews.json) into MongoDB using mongoimport.

Create and activate a virtual environment in ubuntu: 'python3 -m venv venv', then 'source venv/bin/activate'

In the terminal, navigate to your project folder and execute the main script: "python3 main.py"

When prompted, enter your query in natural language, for example:"Which team won the World Cup in 2018?"

After typing your question, you’ll be asked to choose the database backend: 'mysql' or 'mongod'

The terminal will then display the executed query and its result.
