# Playwright UI Automation Framework

This project is an end-to-end (E2E) UI automation framework built using Playwright with Python, designed to validate a complete purchase flow in a web application.

The framework follows the Page Object Model (POM) design pattern to ensure scalability, maintainability, and clear separation of concerns.

## Tech Stack
- Python
- Pytest
- Playwright
- Allure Reports

## Features
- Page Object Model (POM)
- Fixtures for setup
- Config management
- Screenshot on failure
- Allure reporting

## Run Tests
pytest --alluredir=allure-results

## View Report
allure serve allure-results
