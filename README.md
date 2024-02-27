# Cursor Groq Proxy

A proxy server enabling access to [Groq](https://groq.com) API within [Cursor](https://cursor.sh/) IDE.

## Usage

0. Deploy this repo to your public server.
1. Get Groq API key from [Groq Cloud](https://console.groq.com).
2. Open Cursor and Open Cursor Settings (Ctrl+Shift+j).
3. Enter your API key and server URL.

## Contribute

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
