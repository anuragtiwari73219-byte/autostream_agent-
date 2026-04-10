import json

def load_data():
    with open("data/knowledge_base.json") as f:
        return json.load(f)

def answer_query(query):
    data = load_data()
    query = query.lower()

    if "pro" in query:
        return f"Our Pro plan is priced at {data['pricing']['pro']['price']} and offers {data['pricing']['pro']['details']}."

    elif "basic" in query:
        return f"The Basic plan costs {data['pricing']['basic']['price']} and includes {data['pricing']['basic']['details']}."

    elif "refund" in query:
        return data["policies"]["refund"]

    return "Could you please be more specific?"