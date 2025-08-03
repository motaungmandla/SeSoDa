import re

def clean_text(text):
    """
    Cleans the given text by removing unwanted characters, standardizing text, and converting to lowercase.
    
    Args:
        text (str): The input text to be cleaned.
        
    Returns:
        str: The cleaned text.
    """
    # Remove HTML entities (e.g., &rsquo;)
    text = re.sub(r'&[a-zA-Z0-9#]+;', '', text)
    
    # Remove extra spaces, newlines, and tabs
    text = re.sub(r'\s+', ' ', text)
    
    # Remove punctuation that isn't part of normal text (e.g., quotes, parentheses, etc.)
    text = re.sub(r'[^\w\s]', '', text)
    
    # Convert to lowercase
    text = text.lower()

    return text


def clean_dataset_file(input_file_path, output_file_path):
    """
    Cleans a dataset file by removing numeric indices, tabs at the beginning of each line,
    and applying text cleaning (punctuation, HTML entities, etc.).
    
    Args:
        input_file_path (str): Path to the input text file.
        output_file_path (str): Path to save the cleaned output file.
    """
    try:
        with open(input_file_path, 'r', encoding='utf-8') as infile, \
             open(output_file_path, 'w', encoding='utf-8') as outfile:
            for line in infile:
                # Remove numbers and tabs at the beginning of a line
                cleaned_line = re.sub(r'^\d+\t', '', line).strip()
                # Clean the text further (punctuation, HTML entities, etc.)
                cleaned_line = clean_text(cleaned_line)
                outfile.write(cleaned_line + '\n')
        print(f"Cleaning complete! Cleaned file saved to: {output_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
	
# Example usage
input_file = "s1.txt"
output_file = "checkmeOut.txt"
#clean_dataset_file(input_file, output_file)
clean_text(input_file)
