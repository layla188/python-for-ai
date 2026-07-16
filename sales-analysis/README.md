# Paris Weather AI Analyzer

This beginner AI engineering project retrieves Paris weather data from the Open-Meteo API and analyzes a generated weather summary using a Hugging Face sentiment-analysis pipeline.

## Features

- Calls an external REST API
- Processes a JSON response
- Creates a Pandas DataFrame
- Calculates average temperatures
- Generates a weather summary
- Uses a Hugging Face sentiment-analysis pipeline
- Tests the model on 10 sentences
- Creates and saves a weather chart
- Saves API data as a CSV file

## Technologies

- Python
- Jupyter Notebook
- Requests
- Pandas
- Matplotlib
- Hugging Face Transformers
- PyTorch
- Git and GitHub

## Project Structure

```text
python-for-ai/
├── README.md
├── requirements.txt
├── weather_ai_analysis.ipynb
├── get_data.py
├── data/
│   └── paris_weather.csv
├── outputs/
│   └── paris_weather_chart.png
└── practice/
```

## Installation

Clone the repository:

```bash
git clone https://github.com/sama-elmoataz/python-for-ai.git
cd python-for-ai
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Running the Project

1. Open the repository in VS Code.
2. Open `weather_ai_analysis.ipynb`.
3. Select the `.venv` Python kernel.
4. Select **Restart Kernel and Run All Cells**.
5. Wait for the Hugging Face model to download on the first run.

## Project Workflow

```text
Weather API → JSON → DataFrame → Weather summary
→ Hugging Face pipeline → Sentiment result
```

## Author

Layla Yasser