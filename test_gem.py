import requests
import json
import yaml

def load_config(yaml_file="test_gem.yml"):
    """Load the configuration from a YAML file and return the dictionary."""
    with open(yaml_file, "r") as file:
        config = yaml.safe_load(file)
    return config

def generate_content(prompt, api_key=None):
    """Send a request to the Gemini API with the given prompt."""

    if not api_key:
        raise ValueError("API key not found in YAML file.")

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    data = {"contents": [{"parts": [{"text": prompt}]}]}

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")

def main():


    try:
        config = load_config()

        prompt = """
        give me insurance industry news or trends or things that are happening for the last week
        """
        result = generate_content(prompt, config['GEMINI_API_KEY'])

        # Extract the text content
        text_content = result["candidates"][0]["content"]["parts"][0]["text"]

        print(text_content)

    except Exception as e:
        print(e)
  
# Example usage
if __name__ == "__main__":

    main()
    
  