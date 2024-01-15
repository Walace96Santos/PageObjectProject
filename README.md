# PageObjectProject

## Overview

This project is a test automation framework using the Page Object Model for Selenium testing.

## Project Structure

```plaintext
PageObjectProject
|-- tests
|   |-- features
|   |-- mappings
|   |-- pages
|   |-- steps
|-- .pre-commit-config.yaml
|-- .pylintrc
|-- flake8
|-- requirements.txt
|-- README.md
```

# Getting Started

## Prerequisites

Python 3.10

Virtualenv

## Installation

1. Clone the repository:

```plaintext
git clone https://github.com/Walace96Santos/PageObjectProject.git
cd PageObjectProject
```

2. Create and activate a virtual environment:

```plaintext
python3.10 -m venv venv
source venv/bin/activate
```

3. Install project dependencies:

```plaintext
pip install -r requirements.txt
```


# Running Tests

Execute the following command to run the tests:

```plaintext
pytest tests/steps/test_THE_TEST_HERE.py
```
