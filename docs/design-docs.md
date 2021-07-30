# Chad v1.0 Design

## Glossary

## Problem

I need a simple chat based 'assistant' that can manage parts of my life that I have trouble managing on my own.

Things that I need managed:

* My Calendar
* Get the weather

## Description of the Solution

Create a Discord client bot that I can send messages to that can process these commands for me. I would like to message the bot in plain english; so I will use a NLP library to parse the commands from raw text.

I should consider creating an API for adding new commands for me.

## Solution - Technical

Python is going to be the language of choice for this project due to the large user base of NLP tooling and discord-py library.

The NLP command parsing and processing may need to be refactored out later so a hard line in the code should be drawn between discord-py and the NLP commands. For now I'm going to try to keep everything running in a single container for simplicity and easy of maintaining.

## Metrics
