@echo off
REM Go to project folder
cd /d "C:\Users\hajer\PycharmProjects\nopcommerceApp"

REM Activate virtual environment
call .venv\Scripts\activate

REM Run pytest (sanity OR regression)
pytest -s -v -m "sanity or regression" --html=./Reports/report.html TestCases/ --browser chrome

REM Uncomment below if you want different test selections
REM pytest -s -v -m "sanity and regression" --html=./Reports/report.html TestCases/ --browser chrome
REM pytest -s -v -m "regression" --html=./Reports/report.html TestCases/ --browser chrome

pause

