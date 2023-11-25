import http.client, urllib.request, urllib.parse, urllib.error, base64, json
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def evaluate_message(message, subscription_key, endpoint):
    headers = {
        'Content-Type': 'text/plain',
        'Ocp-Apim-Subscription-Key': subscription_key,
    }

    params = urllib.parse.urlencode({
        'classify': 'True',
    })

    try:
        conn = http.client.HTTPSConnection(endpoint)
        conn.request("POST", "/contentmoderator/moderate/v1.0/ProcessText/Screen?%s" % params, message, headers)
        response = conn.getresponse()
        data = response.read().decode('utf-8')  # Decode from bytes to string
        conn.close()

        # Convert from JSON string to Python dictionary
        data = json.loads(data)
        
        # Extract category scores and profanity information
        category1_score = data['Classification']['Category1']['Score']
        category2_score = data['Classification']['Category2']['Score']
        category3_score = data['Classification']['Category3']['Score']
        review_recommended = data['Classification']['ReviewRecommended']
        profanity_detected = data['Terms']

        # Print category scores and review recommendation
        print('Sexually Explicit Score:', category1_score)
        print('Sexually Suggestive Score:', category2_score)
        print('Offensive Score:', category3_score)
        print('Review Recommended:', review_recommended)
        
        # Print each detected profanity term
        if profanity_detected is not None:
            profanity_terms = ', '.join([term_info['Term'] for term_info in profanity_detected])
            print('Profanity Detected:', profanity_terms)
        else:
            print('No profanity detected.')

    except Exception as e:
        print("Exception occurred: {0}".format(e))


message = "Can you hop on a call with me soon? I need some help"
subscription_key = "d6492f80fb9b48e091b6667f3deb8a55"
endpoint = "perrincorp.cognitiveservices.azure.com"
result = evaluate_message(message, subscription_key, endpoint)
print(result)
