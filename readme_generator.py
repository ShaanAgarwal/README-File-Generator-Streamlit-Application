def ask(query):
    import openai
    import json
    import re

    # Load API key from secrets.json
    with open("./secrets.json", "r") as f:
        json_file = json.load(f)

    openai.api_key = json_file['api_key']

    # Make the API call to OpenAI's chat completion endpoint
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": query}],
        temperature=0.5,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    response = response.choices[0].message.content
    return response