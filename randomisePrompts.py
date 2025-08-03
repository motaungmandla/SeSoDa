import jsonlines
import pandas as pd
import re
from sklearn.model_selection import train_test_split

# Define file paths
input_file = "news_dataset.jsonl"  # Path to your input JSONL dataset
output_train = "news_train.jsonl"
output_val = "news_val.jsonl"
output_test = "news_test.jsonl"

# Function to clean text
def clean_text(text):
    text = text.strip()  # Remove leading/trailing spaces
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
    text = re.sub(r'[^\x00-\x7F]+', '', text)  # Remove non-ASCII characters
    return text

# Load and clean dataset
data = []
with jsonlines.open(input_file) as reader:
    for obj in reader:
        if "prompt" in obj and "completion" in obj:
            # Clean prompt and completion
            obj["prompt"] = clean_text(obj["prompt"])
            obj["completion"] = clean_text(obj["completion"])
            # Check if completion is valid
            if len(obj["completion"]) > 0:
                data.append(obj)

# Convert to DataFrame for easier manipulation
df = pd.DataFrame(data)

# Split into train, validation, and test sets
train_data, temp_data = train_test_split(df, test_size=0.2, random_state=42)
val_data, test_data = train_test_split(temp_data, test_size=0.5, random_state=42)

# Save back to JSONL format
def save_to_jsonl(dataframe, output_file):
    with jsonlines.open(output_file, mode='w') as writer:
        for _, row in dataframe.iterrows():
            writer.write({"prompt": row["prompt"], "completion": row["completion"]})

save_to_jsonl(train_data, output_train)
save_to_jsonl(val_data, output_val)
save_to_jsonl(test_data, output_test)

print(f"Data split and saved:\n- Train: {len(train_data)} samples\n- Validation: {len(val_data)} samples\n- Test: {len(test_data)} samples")
