import argparse
import sys
import os
import google.generativeai as genai
import logging

# Suppress logging warnings by setting environment variables
os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"

# Optionally suppress logs from the generative AI package by setting logging to CRITICAL
logging.basicConfig(level=logging.CRITICAL)

def get_api_key():
    """Retrieve the API key from environment variables."""
    api_key = os.getenv("GENAI_API_KEY")
    if not api_key:
        print("Error: API key not found. Please set the API key using the appropriate command for your OS.")
        if sys.platform == "win32":
            print("For Windows, use: set GENAI_API_KEY=your_key")
        else:
            print("For Linux/macOS, use: export GENAI_API_KEY=your_key")
        sys.exit(1)
    return api_key

def get_input_data(args):
    """Retrieve input data from stdin or command line arguments."""
    if not sys.stdin.isatty():
        # Read from stdin if piped
        return sys.stdin.read().strip()
    elif args.prompt:
        # Use the prompt provided as an argument
        return args.prompt
    else:
        print("Error: No prompt provided. Use -p or pipe input.")
        sys.exit(1)

def generate_content(api_key, input_data):
    """Generate content using Google Generative AI."""
    try:
        # Configure the API key
        genai.configure(api_key=api_key)
        
        # Initialize the model
        model = genai.GenerativeModel("gemini-1.5-flash")
        
        # Generate content
        response = model.generate_content(input_data)
        return response.text
    except Exception as e:
        print(f"Error generating content: {e}")
        sys.exit(1)

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Generate content using Google Generative AI.")
    parser.add_argument("-p", "--prompt", help="Prompt to pass to the generative AI model.")
    parser.add_argument("-o", "--output", help="File to save the generated content.")
    args = parser.parse_args()

    # Get the API key from environment variable
    api_key = get_api_key()

    # Get input data
    input_data = get_input_data(args)

    # Generate content
    generated_content = generate_content(api_key, input_data)

    # Print the response in green color
    print("\033[32m" + generated_content + "\033[0m")

    # Optionally save to output file
    if args.output:
        try:
            with open(args.output, 'w') as f:
                f.write(generated_content)
            print(f"Content saved to {args.output}")
        except Exception as e:
            print(f"Error saving content to file: {e}")
            sys.exit(1)

if __name__ == "__main__":
    main()
