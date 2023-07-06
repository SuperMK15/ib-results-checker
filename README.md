# IB Results Checker Script

## Overview
This project provides an automation script written in Python that allows users to log into the International Baccalaureate Organization (IBO) candidate portal and navigate to the results page automatically. The script utilizes the Selenium library to interact with the web browser.
- Go to [Prerequisites](#prerequisites)
- Go to [Installation](#installation)
- Go to [Configuration](#configuration)
- Go to [Usage](#usage)

## Prerequisites
Before using this project, make sure you have the following:
- Python 3 installed on your machine.
- Chrome web browser installed.

## Installation
1. Get the project either by downloading it and unzipping it to your preferred location, or cloning this GitHub repository and navigating to the project directory with the bash commands below:
```
git clone https://github.com/SuperMK15/ib-results-checker.git/
cd ib-results-checker
```
2. Open a terminal if you haven't already in the project directory, and install the required Python dependencies by running:
```
pip install -r requirements.txt
```

## Configuration
To use the script, you need to configure your login information in the `config.txt` file. Follow the steps below:
1. Open the provided `config_template.txt` file.
2. Make a copy of it and name it `config.txt`. Make sure to save it in the same directory.
3. Replace `your_personal_code_here` with your IBO personal code and 'your_pin_here' with your PIN.
4. Adjust the `time_between_reloads` value if desired. This value represents the time (in seconds) to wait before reloading the page and trying again.
5. Ensure you save all your changes to the file.

## Usage
To run the script, execute the following command in the terminal or simply run it using your IDE of choice:
```
python main.py
```
To stop the script, you can use `Ctrl+C` in the terminal.

## Troubleshooting
- If the script fails to run or encounters any issues, ensure that you have correctly installed the required dependencies by running `pip install -r requirements.txt`.
- Verify that the login information in the config.txt file is correct.
- If you still encounter issues, ensure your Chrome browser and the provided Chromedriver version are compatible. If not, replace it with your own from `https://chromedriver.chromium.org/downloads`.
