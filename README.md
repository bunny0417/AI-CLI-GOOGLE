[AI-CLI-GOOGLE

AI-CLI-GOOGLE is a powerful and easy-to-use command-line tool built in Python that allows users to interact with Google's Generative AI model. With this tool, you can effortlessly generate content based on custom prompts directly from your terminal.

The tool provides a clean and minimalistic output, suppressing unwanted logs and warnings. It is designed to work on both Windows and Linux/macOS platforms and supports seamless integration with your existing workflow.
](https://github.com/bunny0417/AI-CLI-GOOGLE)


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



    
