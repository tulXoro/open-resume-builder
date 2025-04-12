# Open Resume Builder

## Description

This is a simple resume builder that uses AI to generate a resume based on the user's input, and a job description.

***DISCLAIMER: This is not meant to be used seriously. It is not a replacement for building your own resume. Use at your own risk.***

## How it works

### Architecture

The app is built using a microservices architecture, with the following components:

- **Frontend**: Uses [Sveltekit](https://svelte.dev/docs/kit/introduction) to create a simple web app that allows the user to input their information and job description. It uses [Tailwind CSS](https://tailwindcss.com/) for styling.
- **Backend**: Uses [Python](https://www.python.org/) and [FastAPI](https://fastapi.tiangolo.com/) to create a simple API that takes the user's input and job description.
- **LLM**: Uses [Ollama](https://ollama.com/) to run the LLMs locally. The LLM is used to generate the resume based on the user's input and job description.

All components are containerized using [Docker](https://www.docker.com/) for easy deployment.

### Other Noteable Technologies

- To be added later...

## Usage

Use this however you see fit.

## Dependencies

### For Docker Installation (recommended)

- [Docker](https://www.docker.com/) (optional, but recommended)

### For Manual Installation

- [Node.js](https://nodejs.org/en) v21.1.0 or later
- [Python](https://www.python.org/) (probably 3.10 or later)
- [Ollama](https://ollama.com/)

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
