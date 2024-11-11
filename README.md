Legal AI Assistant is a domain-specific question-answering chatbot focused on legal issues. The assistant accepts user queries via text or voice input and provides concise, relevant answers related to legal matters. The application integrates several advanced technologies to deliver a seamless experience:

- **Language Model**: Utilizes the Groq API with the llama-3.1-8b-instant model for generating accurate responses to legal questions.
- **Speech-to-Text**: Employs OpenAI’s Whisper for converting voice inputs into text.
- **Text-to-Speech**: Uses gTTS (Google Text-to-Speech) to convert text responses back into speech, offering both US and UK English outputs.
- **Context Relevance**: Implements Zero-Shot Classification via Hugging Face Transformers to determine if a user’s query is relevant to the legal domain.
- **User Interface**: Provides an intuitive interface using Gradio, allowing users to interact with the assistant through both text and voice seamlessly.

Features:
- **Domain-Specific Knowledge**: Answers are tailored to legal issues, ensuring users receive expert information.
- **Multi-Modal Interaction**: Supports both text and audio inputs and outputs for versatile user engagement.
- **Context Filtering**: Questions outside the legal domain are politely declined, maintaining focus and accuracy.
- **Easy Deployment**: Instructions included for running the application locally or within a Docker container.


Getting Started:
**Clone the repository**:

	git clone https://github.com/yourusername/Legal-AI-Assistant.git

**Install Dependencies**:
- Ensure you have *Python 3.8 or higher*.
- Install required packages.

	pip install -r requirements.txt

**Setup API Key**:
Obtain a Groq Api key and set it as an environment variable:

	export GROQ_API_KEY='your_actual_groq_api_key'

**Run the Application**:

	python main.py

7. **Access the Interface**:
Open the provided local URL in your web browser to interact with the assistant.
