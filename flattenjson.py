import json

# Read the file and compact multi-line JSON
with open("Sesotho/Ses-Eng.jsonl", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Write back with all JSON objects on single lines
with open("Sesotho/Ses-Eng_fixed.jsonl", "w", encoding="utf-8") as f:
    for line in lines:
        line = line.strip()
        if line:  # Skip empty lines
            try:
                # Parse and re-serialize to ensure single-line format
                obj = json.loads(line)
                f.write(json.dumps(obj, ensure_ascii=False) + "\n")
            except json.JSONDecodeError:
                # Handle multi-line JSON objects (like your verb entry)
                if line.startswith("{") and not line.endswith("}"):
                    # Combine until we find closing }
                    combined = line
                    for next_line in lines[lines.index(line)+1:]:
                        combined += next_line.strip()
                        if next_line.strip().endswith("}"):
                            break
                    obj = json.loads(combined)
                    f.write(json.dumps(obj, ensure_ascii=False) + "\n")