import sys
from transformers import pipeline

if len(sys.argv) < 2:
 print("No input received")
 sys.exit(1)

user_input = sys.argv[1] # Get input from command line


# Load the zero-shot classification pipeline with a powerful model
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Define your possible intents
candidate_intents = [
 "create docker container",
 "stop docker container",
 "list docker containers",
 "remove docker container",
 "build docker image",
 "pull docker image",
 "push docker image",
 "inspect docker container"
]

# Run zero-shot classification
result = classifier(
 user_input,
 candidate_intents,
 hypothesis_template="The user wants to {}."
)

# Print the most likely intent
print(result['labels'][0])
# print("Confidence Scores:", dict(zip(result['labels'], result['scores'])))






# print(user_input)
    # Process it (example: uppercase it)

#print(user_input.upper())
