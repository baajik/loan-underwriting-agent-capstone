# Loan Underwriting Agent - Intelligent Document Analysis

A sophisticated AI-powered loan underwriting assistant with document processing capabilities, built with Gradio and LangChain.

## Features

### Core Functionality
- **Query Understanding**: Classifies and responds to different types of loan-related questions (factual, analytical, comparison, definition)
- **Basic Tools**: Includes calculator functionality for loan calculations and financial operations
- **Memory**: Maintains conversation context across interactions
- **Document Upload**: Upload and process loan documents to provide context for underwriting decisions

### Document Processing
- **Supported Formats**: TXT, PDF, DOCX
- **Content Extraction**: Automatically extracts text content from uploaded loan documents
- **Context Integration**: Document content is seamlessly integrated into the conversation context

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Application

```bash
# Run in part1 mode (Query Understanding)
python main.py part1

# Run in part2 mode (Basic Tools)
python main.py part2

# Run in part3 mode (Memory)
python main.py part3

# Run on a specific port
python main.py part1 --port 8080

# Run on a specific host
python main.py part1 --host 127.0.0.1
```

### Using Document Upload

1. Start the application in your preferred mode
2. Upload one or more loan documents using the file upload interface
3. Ask questions about the uploaded documents
4. The AI will use the document content as context for answering your questions

### Example Usage

1. **Upload loan application documents** (PDF/DOCX)
2. **Ask questions** like:
   - "What is the debt-to-income ratio for this loan application?"
   - "Compare the applicant's income vs expenses"
   - "Calculate the monthly mortgage payment"
   - "What are the key risk factors in this application?"

## Modes

### Part 1: Query Understanding
- Classifies loan-related questions into categories (factual, analytical, comparison, definition)
- Formats responses based on question type
- Professional presentation of underwriting information

### Part 2: Basic Tools
- All Part 1 features
- Calculator functionality for loan calculations
- Enhanced response formatting for financial data

### Part 3: Memory
- All Part 2 features
- Conversation memory and context retention
- Follow-up question handling for complex underwriting scenarios

## Dependencies

- `gradio`: Web interface framework
- `python-dotenv`: Environment variable management
- `PyPDF2`: PDF text extraction
- `python-docx`: DOCX text extraction
- `langchain`: AI/LLM integration

## Environment Variables

Create a `.env` file with your API keys:
```
OPENAI_API_KEY=your_openai_api_key_here
```

## File Structure

```
loan_underwriting/
├── app.py              # Main application with document upload
├── main.py             # Entry point
├── requirements.txt    # Dependencies
├── core/
│   └── chat_interface.py  # Abstract chat interface
├── week1/
│   ├── factory.py      # Chat implementation factory
│   ├── part1.py        # Query understanding
│   ├── part2.py        # Basic tools
│   └── part3.py        # Memory
└── tools/
    └── calculator.py   # Calculator tool
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is part of the LangChain course assignment. 