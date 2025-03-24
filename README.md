# Open Resume Builder

## Description

This is a simple resume builder that uses AI to generate a resume based on the user's input, and a job description.

## How it works

Not sure yet. It's a work in progress.

## Usage

Use this however you see fit.

## Dependencies

- [Node.js](https://nodejs.org/en) v21.1.0 or later
- [Python](https://www.python.org/) (probably 3.10 or later)
- [Docker](https://www.docker.com/) (optional, but recommended)

## Installation

### Docker (recommended)

1. Clone the repository and change directory into it.
2. Build the Docker image with `docker compose build`.
3. Start the app using `docker compose up`.

    *Note: You may want to pull models with `docker compose exec ollama ollama pull <model>`, where `<model>` is the name of the model you want to pull.*

    Example: `docker compose exec ollama ollama pull llama2`

    Feel free to add more models by editing the `main.py` file in `backend/main.py`.

### Manual

1. Clone the repository and change directory into it.
2. Further instructions will be added at a later time....

## Contributing

You can contribute by submitting a pull request or opening an issue.
