import sys

from sympy.physics.units import action
from transformers import pipeline

if len(sys.argv) < 2:
 print("No input received")
 sys.exit(1)

user_input = sys.argv[1] # Get input from command line
user_tools = sys.argv[2]

tools_list = ["docker","kubernetes"]

# Initialize the zero-shot classification pipeline
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Define candidate intents for each tool
if user_tools in tools_list:
 candidate_intents_map = {
  "docker": [
   "create docker container",
   "stop docker container",
   "list docker containers",
   "remove docker container",
   "build docker image",
   "pull docker image",
   "push docker image",
   "inspect docker container"
  ],
  "kubernetes": [
   "create a pod",
   "delete a pod",
   "scale deployment",
   "get pod logs"
  ]
 }
else:
    print("tools does not exist...")
# Fetch the list of intents for the selected tool
candidate_intents = candidate_intents_map.get(user_tools.lower())

if not candidate_intents:
 print("Tool not supported.")

# Run the classification
result = classifier(
  user_input,
  candidate_intents,
  hypothesis_template="The user wants to {}."
 )
print(result['labels'][0])





 # Print the most likely intent
 # print(result['labels'][0])
 # print("Confidence Scores:", dict(zip(result['labels'], result['scores'])))






 # print(user_input)
     # Process it (example: uppercase it)

 #print(user_input.upper())
