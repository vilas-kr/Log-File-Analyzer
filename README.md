
# Log File Analyzer

The Log File Analyzer is a Python-based tool that parses server or application log files, extracts key information, and provides insights such as:
1. HTTP error code counts.
2. Error frequencies
3. IP address summary

## Features
1. Parse log files line by line
2. Count occurrences of each IP address
3. Count occurrences of HTTP status codes
4. Export a text summary to log_summary.txt
5. Works with standard server log formats

## Tech Stack
```
-- Language : Python
-- Tools: VSCode, Git
-- Libraries: Faker
```

## Project Structure
```
Log-File-Analyzer/
│
|-- src/
|   |-- generate_log_file.py
│   |-- analyzer.py         
│
|-- log_summary.txt
|-- server_log.txt    
|-- README.md
|-- .gitignore
|-- requirements.txt  
```

## Installation
```
Clone the repository -> git clone https://github.com/vilas-kr/Log-File-Analyzer.git

Move to project folder 
    -> cd Log-File-Analyzer

Install dependencies 
    -> pip install -r requirements.txt

Run the application 
    -> First generate log file 
        -> python generate_log_file.py
    -> Then, run analyzer
        -> python analyzer.py
```

## Author
```
Vilas K R
GitHub username: vilas-kr
```
