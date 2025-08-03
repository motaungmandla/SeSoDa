import json

def convert_multiline_to_jsonl(input_path, output_path):
    buffer = ""
    brace_count = 0
    inside_object = False
    total_objects = 0
    errors = 0

    with open(input_path, 'r', encoding='utf-8-sig') as infile, \
         open(output_path, 'w', encoding='utf-8') as outfile:
        
        for line_num, line in enumerate(infile, 1):
            stripped = line.strip()
            if not stripped:
                continue  # skip blank lines

            # Count braces
            open_count = stripped.count('{')
            close_count = stripped.count('}')
            brace_count += open_count - close_count

            # Start accumulating when we hit the first opening brace
            if not inside_object and open_count > 0:
                inside_object = True
                buffer = stripped
            elif inside_object:
                buffer += " " + stripped

            # When object is complete (brace balanced)
            if inside_object and brace_count == 0:
                try:
                    json_obj = json.loads(buffer)
                    outfile.write(json.dumps(json_obj, ensure_ascii=False) + "\n")
                    total_objects += 1
                except json.JSONDecodeError as e:
                    print(f"❌ JSON error on line {line_num}: {e}")
                    errors += 1
                buffer = ""
                inside_object = False

    print(f"✅ Done! Converted {total_objects} objects to JSONL.")
    if errors > 0:
        print(f"⚠️ Skipped {errors} invalid objects.")

# Example usage
convert_multiline_to_jsonl("Sesotho/Ses-Eng.jsonl", "Sesotho/Ses-Eng-final.jsonl")
