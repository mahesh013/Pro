import requests

# — your hard-coded key & the correct endpoint —
GROQ_API_KEY = "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"
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

bot_name = "Yantra"

def get_response(user_msg: str) -> str:
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type":  "application/json"
    }
    payload = {
        # use your Llama3 model here:
        "model":      "Llama3-8b-8192",
        "messages": [
            {"role": "system", "content": f"You are {bot_name}, a helpful customer-support assistant Yantrik Technologies is a premier engineering and automation solution provider specializing in Welding, Assembly, and Handling Automation Systems for automotive components and Body in White (BIW) assemblies. Established in 2021, we have built a reputation for delivering innovative, reliable, and high-quality solutions tailored to meet the unique needs of our clients across various industries. Our dedicated team combines expertise with cutting-edge technology to deliver high-quality, reliable solutions tailored to our clients’ needs.Employee name of here is  1 : Pravin sir is plant head .2:Pankaj sir is company owner .3:chavahan sir is Partner of the company .4:mahesh kandekar ai intern ,5:Raju mundhe sir is manager of software development department .6:Manisha kandekar labview developer,7:pratima madam business developer 8:sumit sir and dhrv sir plc developer. give ans based on user question in short and meaningful way."},
            {"role": "user",   "content": user_msg}
        ],
        "temperature": 0.2,
        "top_p":       0.5,
        "max_tokens":  200
    }

    try:
        resp = requests.post(GROQ_API_URL, json=payload, headers=headers, timeout=10)

        # — DEBUG OUTPUT —
        print(f"[DEBUG] HTTP {resp.status_code} response from Groq:")
        print(resp.text)

        resp.raise_for_status()
        data = resp.json()

        # — DEBUG KEYS —
        print("[DEBUG] JSON keys:", data.keys())
        print("[DEBUG] choices payload:", data.get("choices"))

        # parse out the assistant’s reply
        return data["choices"][0]["message"]["content"].strip()

    except requests.HTTPError as http_err:
        print(f"[GROQ HTTP ERROR] {http_err}")
    except requests.RequestException as req_err:
        print(f"[GROQ REQUEST ERROR] {req_err}")
    except (ValueError, KeyError) as parse_err:
        print(f"[GROQ PARSE ERROR] {parse_err}")

    return "Sorry, I’m having trouble right now. Please try again later."
