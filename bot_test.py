import openai

openai.api_key = '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'

prompt = "How can we fight inflation?"

response  = openai.Completion.create(
    model= 'davinci:ft-liberated-logic-2023-06-30-20-54-43',
    prompt= prompt,
    max_tokens = 250
)

print("\nPrompt:")
print(prompt)
print("\nGenerated text:")
print(response.choices[0].text.strip())