# HardwareRecs Analyzer

## Overview
The HardwareRecs Analyzer is a Python-based application designed to parse, analyze, and visualize data from the HardwareRecs Q&A site. This tool is capable of preprocessing textual data, performing statistical analysis on linguistic features, and presenting the results through visualizations.

## Getting Started

### Prerequisites
- Python 3.9
- External libraries: `numpy`, `scipy`, `pandas`, `matplotlib`
- Ensure all file operations are set to use `utf-8` encoding to avoid character encoding issues.

### Installation
- Clone the repository to your local machine: git clone https://github.com/pragy29/HardwareRecs
- Navigate to the cloned directory: cd HardwareRecs-Analyzer

### Setup
No additional setup is required beyond having Python and the necessary libraries installed. Make sure all scripts are marked as executable where applicable.

### Running the Application
To run the application, execute the main script from the command line: python main.py

## Features
- **Data Preprocessing**: Cleans HTML content and special characters from dataset entries.
- **Data Analysis**: Implements a class for parsing XML data and extracting key linguistic features.
- **Data Visualization**:
  - Vocabulary size distribution across posts.
  - Trends in the number of posts over different quarters.

## File Structure
- `data/`: Directory containing the dataset and any generated output files.
- `src/`: Contains all Python scripts.
  - `parser.py`: Parses XML data and extracts information.
  - `data_visualization.py`: Generates visual graphs from analyzed data.
  - `preprocess_data.py`: Preprocesses data to clean and prepare text for analysis.

## Usage
1. **Data Preprocessing**: Run the `preprocess_data.py` to clean the data.
2. **Parsing and Analysis**: Use `parser.py` to analyze the cleaned data.
3. **Visualization**: Execute `data_visualization.py` to generate visual representations of the analysis.

## License
This project is licensed under the Monash Univeristy Faculty of IT.

## Authors
- https://github.com/pragy29

## Acknowledgments
- Monash University, Faculty of IT, for the assignment guidelines and dataset.
- All contributors who helped in testing and refining the project.
