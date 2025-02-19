# Project Title

## Introduction

This project is designed to fetch HTML content from Yahoo Finance, parse it using BeautifulSoup, and extract text, links, and images. The extracted text is saved to a file for further analysis.

## Features

- **HTML Content Fetching**: Utilizes `urllib.request` to fetch HTML content from a specified URL.
- **Content Parsing**: Uses BeautifulSoup to parse HTML content and extract text, links, and images.
- **Data Storage**: Saves the extracted text to a file named `page_text.txt`.

## Structure

├── .gitignore ├── README.md  ├── main.py

- **.gitignore**: Specifies files and directories to be ignored by Git.
- **README.md**: Contains documentation for the project.
- **main.py**: The main script that performs HTML fetching and parsing.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd <project-directory>
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the `main.py` script to fetch and parse HTML content: 
    
    python main.py