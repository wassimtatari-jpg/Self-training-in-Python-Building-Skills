import openai

api_key="Your api key"

openai.api_key=api_key

response=openai.completions.create(
    engine='YOUR_OPENAI_API_KEY',
    prompt="Tell me somthing intersting about stars",
    max_tokens="500"
)
print(response['choice'][0].text.strip())