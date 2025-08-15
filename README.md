# IA Agents Playground

This project demonstrates an interactive AI agent using LangChain, Azure OpenAI.

## Features
- Weather information tool
- Wikipedia search tool (Spanish)
- Azure OpenAI GPT-4o integration
- Interactive console for user questions

## Requirements
- Python 3.8+
- See `requirements.txt` for dependencies

## Usage
1. Clone the repository.
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set your Azure OpenAI environment variables in a `.env` file:
   - `AZURE_OPENAI_ENDPOINT`
   - `AZURE_OPENAI_API_KEY`
   - `AZURE_OPENAI_API_VERSION`
   - `AZURE_OPENAI_MODEL`
4. Run the agent:
   ```sh
   python agent.py
   ```
5. Type your questions in Spanish. Type `salir` or `exit` to quit.

## License
MIT
