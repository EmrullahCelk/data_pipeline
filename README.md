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
To run the project, clone <a href="https://github.com/EmrullahCelk/data_pipeline.git">the project</a> files to your computer and install the necessary dependencies. Please remember to create the .env file and save the required variables. Then, run the **data_pipeline_main.py** file.

# Installing the project on Ubuntu using Putty and WinSCP, and scheduling automatic execution with Crontab
In this section, you will learn how to use tools like WinSCP and PuTTY to run a project on Ubuntu operating system. WinSCP is used to copy files from a Windows operating system to an Ubuntu server, while PuTTY provides a terminal connection and can be used to run the project on Ubuntu.

Before you begin, you will need your IP address and password to connect to the Ubuntu server. By providing your IP address and password, you can follow the steps below.

  ### 1. Connecting to the Ubuntu Server
  <li>Open WinSCP and enter your IP address and username to connect to the Ubuntu server.<br>
  <li>Enter your password to log in or add the .ppk file, then click the "Login" or "Connect" button.<br>
  <li>Once successfully connected, you can see your local files on the left panel and the files on the Ubuntu server on the right panel.<br>
  
  ### 2. Establishing a Terminal Connection with PuTTY
  <li>Open PuTTY and enter your IP address to connect to the Ubuntu server.<br>
  <li>Enter your username and password to log in.<br>
  <li>Click the "Open" button to establish the connection.<br>
  <li>Once successfully connected, you can access the Ubuntu server in the PuTTY terminal window and execute your commands.<br>

  <li>Additionally, you can directly connect to PuTTY by clicking on the PuTTY connection icon located in the top left corner of WinSCP.<br>

  ### 3. Updating the Project and Uploading Necessary Files
  <li>After successfully connecting to the Ubuntu server through the PuTTY terminal window, navigate to the directory where your project is located. For example, use the command `cd /path/to/project` to navigate to the directory where your project is located.<br>
  <li>Clone <a href="https://github.com/EmrullahCelk/data_pipeline.git">this project</a><br>
    <li>To update system packages for the project, execute the following commands in the PuTTY terminal:</li>
  <ul>
    <code>sudo apt-get update</code>: Updates the package manager's (APT) repository databases.</li>
    
    <code>sudo apt-get install python3</code>: Installs the latest version of Python 3 on the system. This command provides the Python execution environment required for the project to run.</li>
  </ul> 
  <li>Create and activate a virtual environment.</li>
<ul>
  <code>python3 -m venv venv</code>: Create a virtual environment.</li>
  <code>source venv/bin/activate</code>: Activate the virtual environment.</li>
</ul> 
  <li>Copy the project files to the server using WinSCP. Please make sure you copy the <strong>requirements.txt</strong> and <strong>.env</strong> files to the root directory of the project.<br>
  <ul>
    <code>sudo apt install postgresql-server-dev-all</code>: Installs the PostgreSQL development files.</li>
  </ul>
  <li>To install the necessary Python packages, use the requirements.txt file.:</li>
  <ul>
    <code>pip install -r requirements.txt</code>: It ensures that the packages listed in the <strong>requirements.txt</strong> file, which specify the project's dependencies, are installed sequentially.</li>
  </ul>

  ### 4. Scheduling Automatic Execution with Cron
  <li>Edit the crontab file using the command <code>crontab -e</code>.<br>
<li>Add a command to the crontab file that will execute your project:</li>
<ul>
  <code>0 0 * * * /path/to/python /path/to/project/data_pipeline_main.py</code>:This command is used by a scheduled task manager called cron. The expression <strong>0 0 * * *</strong> specifies midnight (00:00) every day. <strong>/path/to/python</strong> specifies the full path to the Python interpreter. <strong>/path/to/project/data_pipeline_main.py</strong> specifies the full path to the Python script. So, this command will run the specified Python script every midnight.</li></ul>
  <li>Additionally, you can seek assistance from the <a href="https://crontab.guru/">crontab.guru</a> website to check the correctness of your other cron expressions. This site provides information on how to structure cron expressions and allows you to validate the accuracy of your expressions.</li>
  
</ul>



    



  
## License
This project is licensed under the MIT License. See the LICENSE file for details.
