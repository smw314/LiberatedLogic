# import openai
# from getpass import getpass
# from googleapiclient import discovery
# import json
# import http.client
# import urllib.request
# import urllib.parse
# import urllib.error
# import base64
# import ssl

# ssl._create_default_https_context = ssl._create_unverified_context

# subscription_key = "d6492f80fb9b48e091b6667f3deb8a55"
# endpoint = "perrincorp.cognitiveservices.azure.com"

# # Set up OpenAI API key
# openai.api_key = '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'

# API_KEY = 'AIzaSyDs1VNg4YmNqnsZI-WESdIKIAsFDe8okKY'

# client = discovery.build(
#   "commentanalyzer",
#   "v1alpha1",
#   developerKey=API_KEY,
#   discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
#   static_discovery=False,
# )
# def evaluate_message(message, subscription_key, endpoint):
#     headers = {
#         'Content-Type': 'text/plain',
#         'Ocp-Apim-Subscription-Key': subscription_key,
#     }

#     params = urllib.parse.urlencode({
#         'classify': 'True',
#     })

#     try:
#         conn = http.client.HTTPSConnection(endpoint)
#         conn.request("POST", "/contentmoderator/moderate/v1.0/ProcessText/Screen?%s" % params, message, headers)
#         response = conn.getresponse()
#         data = response.read().decode('utf-8')  # Decode from bytes to string
#         conn.close()

#         # Convert from JSON string to Python dictionary
#         data = json.loads(data)
        
#         # Check if 'Classification' is in the response
#         if 'Classification' in data:
#             # Extract category scores and profanity information
#             category1_score = data['Classification']['Category1']['Score']
#             category2_score = data['Classification']['Category2']['Score']
#             category3_score = data['Classification']['Category3']['Score']
#             review_recommended = data['Classification']['ReviewRecommended']
#             profanity_detected = data['Terms']

#             # Print category scores and review recommendation
#             print(f'Message: "{message}"')
#             print('Offensive Score:', round(category3_score, 3))
#             print('Sexually Explicit Score:', round(category1_score, 3))
#             print('Sexually Suggestive Score:', round(category2_score, 3))
#             print('Review Recommended:', review_recommended)
            
#             # Print each detected profanity term
#             if profanity_detected is not None:
#                 profanity_terms = ', '.join([term_info['Term'] for term_info in profanity_detected])
#                 print('Profanity Detected:', profanity_terms)
#             else:
#                 print('No profanity detected.')
#         else:
#             print('No classification information returned.')

#     except Exception as e:
#         print("Exception occurred: {0}".format(e))
# def evaluate_conversation(message1, message2, subscription_key, endpoint):
#     analyze_request1 = {
#       'comment': { 'text': message1 },
#       'requestedAttributes': {'TOXICITY': {}}
#     }
#     response1 = client.comments().analyze(body=analyze_request1).execute()

#     comment_value1 = response1['attributeScores']['TOXICITY']['spanScores'][0]['score']['value']

#     analyze_request2 = {
#       'comment': { 'text': message2 },
#       'requestedAttributes': {'TOXICITY': {}}
#     }
#     response2 = client.comments().analyze(body=analyze_request2).execute()

#     comment_value2 = response2['attributeScores']['TOXICITY']['spanScores'][0]['score']['value']

#     print("Comment1:", message1)
#     print("Toxicity Score:", round(comment_value1, 3))
#     evaluate_message(message1, subscription_key, endpoint)

#     print("\nComment2:", message2)
#     print("Toxicity Score:", round(comment_value2, 3))
#     evaluate_message(message2, subscription_key, endpoint)

#     # If any message is inappropriate, generate alternatives
#     if round(comment_value1, 3) > 0.5 or round(comment_value2, 3) > 0.5:
#         # Generate alternatives using OpenAI's GPT-3
#         response = openai.Completion.create(
#           engine="text-davinci-002",
#           prompt=f"One or both of the following messages seem unclear or harmful: \"{message1}\", \"{message2}\". Can you provide three alternative ways to express the same idea in a clearer and non-harmful manner?",
#           temperature=0.5,
#           max_tokens=200
#         )
#         # Print the alternatives
#         print("\nAlternative phrases:")
#         print(response.choices[0].text.strip())

# # Test the function with two messages
# evaluate_conversation("I hate you", "You're such an idiot", subscription_key, endpoint)

from transformers import pipeline
import re

# Load sentiment analysis pipeline
nlp = pipeline('sentiment-analysis', model='cardiffnlp/twitter-roberta-base-sentiment')

def analyze_conversation(conversation):
    # Split conversation into sentences
    sentences = re.split(r'(?<=[^A-Z].[.?]) +(?=[A-Z])', conversation)

    negative_sentences = []
    # Analyze sentiment of each sentence
    for sentence in sentences:
        result = nlp(sentence)
        sentiment = result[0]['label']
        # If sentiment is negative, add sentence to negative_sentences list
        if sentiment == 'NEGATIVE':
            negative_sentences.append(sentence)

    # If there are any negative sentences, print them
    if negative_sentences:
        print("Potentially harmful content detected:")
        for sentence in negative_sentences:
            print("-", sentence)
    else:
        print("No harmful content detected.")

# Test the function with a conversation
conversation = "I think you're a terrible person. I can't believe you would do something like that."
analyze_conversation(conversation)
