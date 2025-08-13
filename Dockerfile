FROM python:3.13-alpine

WORKDIR /monster-brawl-game
COPY *.py ./

ENTRYPOINT ["python", "main.py"]