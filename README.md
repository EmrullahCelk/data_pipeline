# Data Pipeline for Weather Information
This project aims to fetch weather information of a city from an API, convert it into a DataFrame, write it to a database, and send a notification upon completion.

## Usage
To initiate the project, run the data_pipeline.py file. This will fetch weather information from the API, save it to the database, and send a notification upon completion.

## File Structure
**data_pipeline.py**: The main executable file.<br><br>
**weather_information.py**: Module to fetch and process weather information from the API.<br><br>
**create_dataframe.py**: Module to convert weather information into a DataFrame.<br><br>
**df_to_postgresql.py**: Module to write the DataFrame to a PostgreSQL database.<br><br>
**send_mail.py**: Module to send notification emails.<br><br>
**.env**: File containing environment variables.<br><br>
**requirements.txt**: This file lists the external dependencies of the project along with their versions.

## How to Run
To run the project, Clone <a href="https://github.com/EmrullahCelk/data_pipeline.git">the project</a>  files to your computer and run the **data_pipeline_main.py** file by installing the necessary dependencies. 

## License
This project is licensed under the MIT License. See the LICENSE file for details.
