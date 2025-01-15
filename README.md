# Research Papers CLI

A powerful command-line tool for researchers and academics to fetch, process, and analyze research papers directly from PubMed.


## Table of Contents

- [About the Project](#about-the-project)
- [Key Features](#key-features)
- [Technologies and Tools Used](#technologies-and-tools-used)
- [Installation](#installation)
- [Usage](#usage)
- [Command Options](#command-options)
- [Contributing](#contributing)

## About the Project

The **Research Papers CLI** is designed to streamline the process of fetching and analyzing research papers. With just a few commands, you can:

- Query PubMed for research papers using keywords.
- Export results to CSV files for easy analysis.
- Automate repetitive data-gathering tasks.
  
This tool is ideal for students, researchers, and professionals who rely on scholarly articles for their work.


## Key Features

- **Fast Querying**: Fetch research papers using a single command.
- **Customizable Output**: Export results to a CSV file for further analysis.
- **Debug Mode**: Enable detailed logging to troubleshoot and monitor API calls.
- **Lightweight**: Minimal dependencies ensure quick setup and fast execution.


## Technologies and Tools Used

- **Python 3.8+**: Core programming language.
- **Requests**: For making HTTP requests to the PubMed API.
- **Argparse**: Command-line argument parsing.
- **CSV**: For structured output storage.
- **Poetry**: Dependency management and packaging.
- **Logging**: Integrated logging for monitoring tool execution.


## Installation

Follow these steps to set up the **Research Papers CLI**:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/KartikPanditaaa/research-papers-cli.git
   cd research-papers-cli
   ```
2. **Set Up Python Environment**: Ensure Python 3.8+ is installed on your system.

3. **Install Dependencies**: Use Poetry to install all required dependencies:

   ```bash
   poetry install
   ```
4. **Verify Installation**: Run the help command to ensure the tool is set up correctly:

   ```bash
   poetry run python cli.py --help
   ```

## Usage

Use the CLI tool to fetch research papers and process them:

**Basic Usage**
   ```bash
   poetry run get-papers-list "your query string" -f output.csv
   ```
Example:
To search for papers on CRISPR technology and save the results to crispr_results.csv:

   ```bash
   poetry run get-papers-list "CRISPR technology" -f crispr_results.csv
   ```

**Debug Mode**:
Enable debug logs to monitor API requests and responses:

   ```bash
   poetry run get-papers-list "CRISPR technology" -f crispr_results.csv -d
   ```

**Command Options**:

- **-f, --file**: Specify the name of the output CSV file (default: output.csv).
- **-d, --debug**: Enable debug mode for detailed logging.
- **-h, --help**: Display help information about the commands.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.
