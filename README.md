

- Create data models - example with sqlalchemy in "app\models.py"
- Create an endpoint that returns business and symptom data
  - Endpoint should take two optional parameters - business_id & diagnostic
  - Endpoint should return Business ID, Business Name, Symptom Code, Symptom Name, and Symptom Diagnostic values based on filter
- Generate migration script and run migration to create database tables - alembic files provided
  - To create a migration file: "alembic revision --autogenerate -m some_comment"
  - To update database with migration file: "alembic upgrade head"
- Design a database mock up based on the provided data - "app\data\business_symptom_data.csv"
- Create an endpoint for importing a CSV file into the database
  - The only requirement is the endpoint requires a CSV file. If needed, other parameters can be used.
- Create a virtual environment and install the requirements - "requirements\requirements.txt"

