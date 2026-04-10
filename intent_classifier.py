def classify_intent(text):
    text = text.lower()

    greetings = ["hi", "hello", "hey"]
    buying = ["buy", "start", "subscribe", "try"]
    inquiry = ["price", "plan", "cost", "feature"]

    if any(word in text for word in greetings):
        return "greeting"

    elif any(word in text for word in buying):
        return "high_intent"

    elif any(word in text for word in inquiry):
        return "inquiry"

    return "general"