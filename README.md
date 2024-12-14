AI-CLI-GOOGLE

AI-CLI-GOOGLE is a powerful and easy-to-use command-line tool built in Python that allows users to interact with Google's Generative AI model. With this tool, you can effortlessly generate content based on custom prompts directly from your terminal.

The tool provides a clean and minimalistic output, suppressing unwanted logs and warnings. It is designed to work on both Windows and Linux/macOS platforms and supports seamless integration with your existing workflow.


Features of AI-CLI-GOOGLE

AI-CLI-GOOGLE is a command-line tool that integrates seamlessly with Google's Generative AI, providing an intuitive way to generate content directly from the terminal. Below are the key features of this tool:
🔑 API Key Configuration

    Secure API Handling: The tool securely stores and retrieves your Google Generative AI API key from environment variables.
    Easy Setup: Simply set your API key using a single command (works across Windows and Linux/macOS).

📝 Prompt-Based Content Generation

    Text Generation: Generate content based on custom prompts that you pass through the command line or pipe.
    Flexible Input: You can provide a prompt directly using the -p flag or pipe data from another source.

🧹 Clean Output

    No Unwanted Logs: The tool suppresses unnecessary logs and warnings, ensuring a clean and readable output.
    Streamlined Terminal Experience: The focus is purely on the AI-generated content, free from technical noise.

⚡ Cross-Platform Support

    Works on Windows: Supports Windows OS, including setting environment variables for the API key.
    Works on Linux/macOS: Fully functional on Linux/macOS environments, with seamless installation and API key configuration.

💨 Fast and Efficient

    Quick Content Generation: The tool is designed to quickly generate responses to your prompts, making it perfect for creative or automated tasks.
    No Slowdowns: Optimized for fast execution and minimal resource usage.

🔒 Secure API Key Handling

    Environment Variables: Your Google Generative AI API key is securely stored and accessed through environment variables, ensuring no sensitive data is exposed in the codebase.
    Safe from Hardcoding: The API key is not hardcoded into the script, maintaining security.

📂 Save Responses to a File

    Output to File: You can save the generated content to a text file using the -o flag, making it easy to store and reuse responses.

🔧 Customizable

    Piping Data: Supports piping input from other commands or files, allowing for advanced integrations and automation.

🚀 Lightweight Tool

    No Additional Software: Only requires Python and a few dependencies, making it lightweight and easy to install.

🧑‍💻 Developer-Friendly

    Open Source: The tool is open-source, and contributions are welcome! Fork the repository, make improvements, and submit a pull request.
    No GUI Required: Perfect for developers who prefer using command-line tools for efficiency.


---

## 📦 Installation

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/AI-CLI-GOOGLE.git
cd AI-CLI-GOOGLE
```

### 2. Install Dependencies

Ensure you have `pip` installed, then install the required Python packages:

```bash
pip install -r requirements.txt
```

### 3. Set Up Your API Key

Before using the tool, make sure to set your **Google Generative AI** API key.

- **Windows**:
  Open the command prompt and set the API key as an environment variable:

  ```cmd
  set GENAI_API_KEY="your_api_key_here"
  ```

- **Linux/macOS**:
  Open your terminal and set the API key:

  ```bash
  export GENAI_API_KEY="your_api_key_here"
  ```

You can get the API key from [Google AI Studio](https://aistudio.google.com/apikey) by creating a project and obtaining your API key.

### 4. Run the Tool

Once everything is set up, you can start generating content by passing a prompt to the tool:

```bash
python ai-cli-google.py -p "Your prompt here"
```

For example:

```bash
python ai-cli-google.py -p "Tell me a joke!"
```

This will display the AI-generated response directly in your terminal.

---

Now you're ready to use **AI-CLI-GOOGLE**! Just follow the instructions to start generating content.



    
