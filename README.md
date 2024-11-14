<div align="center">
  <br>
  <img alt="Tech4Palestine" src="favicon.ico" width="300px">
  <h1>palestine API</h1>
  <strong>A Simple Fastapi for https://data.techforpalestine.org/docs/datasets/</strong>
</div>
<br>
<p align="center">
  <img src="https://img.shields.io/badge/Dependabot-active-brightgreen.svg" alt="Dependabot Badge">
  <img src="https://img.shields.io/github/languages/code-size/ummahrican/palestine-api" alt="GitHub code size in bytes">
</p>

palestine-api is a simple Fastapi integrated with [palestine-datasets](https://github.com/TechForPalestine/palestine-datasets/tree/main). The main purpose is to make a quick and simple API for requesting the latest data available from palestine-datasets.

## 📖 Prerequisites

In order to run the project we need `python>=3.12` and `uv` for package management.

Install uv following the [offical repo](https://github.com/astral-sh/uv?tab=readme-ov-file#getting-started)

## 🖥️ Local development

To install the application:

```shell
uv sync --frozen --no-cache
```

To start a local copy of the app on port `3000`:

```shell
uv run fastapi dev
```

### 🧪 Test
This project uses pytest for test discovery. Simply run:
```shell
pytest
```
test_FILENAME.py will be auto discovered and tests will run

### 📦 Docker builds

Simply build the dockerfile in your prefered architecture with (select arch with --platform= otherwise it defaults to your system):
```shell
docker build -t palestine-api-local .
```

Then run it!
```shell
docker run -d -p 80:80 palestine-api-local
```

### 🎨 Code linting

To check the code and styles quality, use the following command:

```shell
# Lint your code
uvx ruff check

# Format your code
uvx ruff format
```

### 🚀 Production deployment

<strong>PENDING</strong>

### 💾 Database

This project uses data from [palestine-datasets](https://github.com/TechForPalestine/palestine-datasets/tree/main), a curated list of reputable sources. Check out their repo and [site](https://data.techforpalestine.org/) for more in depth data questions as a database.

## 🤝 Contributing

<strong>PENDING</strong>

## 🍕 Community

Got Questions? Join the conversation in our [Discord](https://discord.gg/jkUqTYvd2s).  

## ⚖️ LICENSE

MIT © [palestine-api](LICENSE)
