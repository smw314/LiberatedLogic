from googleapiclient import discovery
import json

API_KEY = ''

client = discovery.build(
  "commentanalyzer",
  "v1alpha1",
  developerKey=API_KEY,
  discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
  static_discovery=False,
)

comment = ""

analyze_request = {
  'comment': { 'text': comment },
  'requestedAttributes': {'TOXICITY': {}}
}

response = client.comments().analyze(body=analyze_request).execute()

comment_value = response['attributeScores']['TOXICITY']['spanScores'][0]['score']['value']

print("Comment:", comment)
print("Toxicity Value:", comment_value)

# response = client.comments().analyze(body=analyze_request).execute()
# print(json.dumps(response, indent=2))
