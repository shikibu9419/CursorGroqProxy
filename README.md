# Cursor Groq Proxy
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

A proxy server enabling access to [Groq](https://groq.com) API within [Cursor](https://cursor.sh/) IDE.

## Usage

0. Deploy this repo to your public server.
1. Get Groq API key from [Groq Cloud](https://console.groq.com).
2. Open Cursor and Open Cursor Settings (Ctrl+Shift+j).
3. Enter your API key and server URL.

## How to build

using Docker

```shell
docker build -t cursor-groq-proxy .
docker run -it --rm -p 8000:8000 cursor-groq-proxy:latest
```

using Pipenv

```shell
pipenv install
pipenv run dev
```

# Demo
![Demo](./etc/demo.gif)
