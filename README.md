# AutoStream AI Agent

This project is a conversational AI agent built for a fictional SaaS product called AutoStream.

## Features

- Intent Detection (Greeting, Inquiry, High-Intent)
- RAG-based response system using local knowledge base
- Lead capture flow for high-intent users
- Maintains conversation state across multiple turns

## How to Run

1. Open terminal
2. Run:
   python app.py

## Architecture

I designed the system in a simple modular way.

The intent classifier detects user intent based on keywords.

The RAG pipeline fetches answers from a local JSON knowledge base.

State is managed using a class that stores user details during conversation.

When a user shows high intent, the agent collects user details and triggers a lead capture function.

## WhatsApp Integration (Approach)

To integrate with WhatsApp:

- Use WhatsApp Cloud API
- Create a webhook using Flask or FastAPI
- Receive user messages
- Send them to the agent
- Return responses back to WhatsApp

User sessions can be tracked using phone numbers.