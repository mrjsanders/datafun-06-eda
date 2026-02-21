# datafun-06-eda
## Author: Jacob Sanders
## Created February 2026
Analyzing data from a *.csv (update name later)
Making sense of middle school math data in relation to next year's math class placement.
## -------------------------------

## Workflow process
Created .gitignore file
Created requirements.txt 
Created pyproject.toml
Include .venv folder and contents
Installed packaged listed in the requirements.txt file
Updated pip from 25.3 to 26.0.1
## -------------------------------

## Data File
Pulled from my middle school gradebook
Swapped student name for animal starting with the same letter  
Data Includes:  
    1. Chapter Test Scores  
    2. Practice State Test predictors. The perentage indicates the students chances of passing the state test.  
    3. Attendance data as a POI.  
   
## -------------------------------

Source: math_class_data.csv  (8th Grade Student Classroom data)  

Records: 18  

Columns:                     Data Type:  

Student_ID                   int64  
Student_Name_First             str  
Student_Name_Last_Initial      str  
Chapter_1_Test               int64  
Chapter_2_Test               int64  
Chapter_3_Test               int64  
Chapter_4_Test               int64  
Chapter_5_Test               int64  
Chapter_6_Test               int64  
Chapter_7_Test               int64  
Fall_MAP_score               int64  
Winter_MAP_score             int64  
Attendance_Percent_YTD       int64  
dtype: object  

## --- Action Log

1. I built the repo from scratch before I saw the message on our 
   assignment announcement. (Big mistake on my part!)
2. Created a jupyter notebook.
3. Created markup and code blocks to explain and create boxplots
4. Tried using ipwdigets to create buttons.
   1. Made it work on VS Code, but he github preview doesn't support
   2. Ran out of time to work with Voila to resolve the display issue
5. I'm happy with my project, but sad that it only displays correctly 
   in VS Code.
## ---------------------------------

