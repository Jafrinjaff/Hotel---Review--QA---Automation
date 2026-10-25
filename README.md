# Hotel Review QA Data Validation Automation
**Status: In Progress**

A personal Python project to automate a manual hotel review validation workflow. It uses synthetic practice data only. No company data or code is used.

## What works now
- Selenium extraction of hotel data from three synthetic HTML pages (websites/website1)
- Data retrieval from a practice MongoDB database using PyMongo
- Comparison of website values with MongoDB values
- Field-level PASS/FAIL results and an overall hotel status (single-hotel workflow)

## Planned
- Multi-hotel validation
- API checks using Requests
- Pytest test cases
- Logging and reporting

## Project Structure
- src/Database.py: MongoDB access
- src/website_extractor.py: Selenium extraction
- src/validation.py: comparison and PASS/FAIL logic
- src/main.py: runs the workflow
- websites/website1: synthetic HTML hotel pages

## Tech Stack
Python, Selenium WebDriver, MongoDB, PyMongo, Git

## How to Run
1. Install Python and MongoDB.
2. Run: pip install selenium pymongo
3. Start MongoDB and add the practice data (database: HotelQA_Automation, collection: ReviewDataBank).
4. Run: python src/main.py
