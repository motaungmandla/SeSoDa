# Python script to convert text in a file to lowercase

# Function to convert text to lowercase and save to a new file
def convert_to_lowercase(input_file, output_file):
    try:
        # Open the input file in read mode
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()

        # Convert the text to lowercase
        lower_text = text.lower()

        # Open the output file in write mode and save the converted text
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(lower_text)

        print(f"Text has been successfully converted to lowercase and saved to {output_file}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please check the input file path, output file path, and file permissions.")

# Usage
input_file = 's1.txt'  # Change this to the path of your input text file
output_file = 'uniformtext.txt'  # Change this to your desired output file path

convert_to_lowercase(input_file, output_file)

convert_to_lowercase(input_file, output_file)
