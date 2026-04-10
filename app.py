from agent.intent_classifier import classify_intent
from agent.rag_pipeline import answer_query
from agent.lead_tool import mock_lead_capture
from agent.state_manager import UserState

state = UserState()

print("AutoStream Assistant: Hi! How can I help you today?")

while True:
    user_input = input("You: ")

    intent = classify_intent(user_input)
    state.intent = intent

    if intent == "greeting":
        print("Agent: Hello! Ask me about pricing or features.")

    elif intent == "inquiry":
        print("Agent:", answer_query(user_input))

    elif intent == "high_intent":
        print("Agent: Great! Let's get your details.")

        if not state.name:
            state.name = input("Agent: Your name: ")

        if not state.email:
            state.email = input("Agent: Your email: ")

        if not state.platform:
            state.platform = input("Agent: Your platform: ")

        if state.name and state.email and state.platform:
            mock_lead_capture(state.name, state.email, state.platform)
            print("Agent: Thank you! We'll contact you soon.")
            break

    else:
        print("Agent: Can you rephrase?")