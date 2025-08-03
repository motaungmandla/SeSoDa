from jsonschema import validate
from jsonschema.exceptions import ValidationError

def validate_jsonl_with_schema(file_path, schema=None):
    """
    Validate JSONL against an optional JSON Schema.
    Example schema: {"type": "object", "properties": {"prompt": {"type": "string"}}
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            
            try:
                data = json.loads(line)
                if schema:
                    validate(instance=data, schema=schema)
            except json.JSONDecodeError as e:
                yield (False, i, f"JSON Syntax Error: {str(e)}")
            except ValidationError as e:
                yield (False, i, f"Schema Error: {str(e)}")
            else:
                yield (True, i, None)

# Usage:
schema = {
    "type": "object",
    "required": ["prompt", "completion"],
    "properties": {
        "prompt": {"type": "string"},
        "completion": {"type": "string"}
    }
}

for result in validate_jsonl_with_schema('data.jsonl', schema):
    valid, line, msg = result
    if not valid:
        print(f"Line {line} failed: {msg}")