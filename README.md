# Vitaz AI# Vitaz AI Assistant

Vitaz AI is a sophisticated conversational AI assistant that implements a two-stage 
processing system: thought generation and response creation. Built using the Groq 
API, it provides thoughtful and contextually aware responses.

## Features

- **Two-Stage Processing**: Separates thought analysis from response generation
- **Context Awareness**: Maintains conversation history for contextual responses
- **Detailed Thought Process**: Provides visibility into AI's reasoning
- **Error Handling**: Graceful handling of potential runtime issues

## Technical Details

### Requirements

- Python 3.10+
- Groq API access
- Required packages: `groq`

### Architecture

#### VitazAssistant Class

The main class implementing the AI assistant functionality:

- **Initialization**
  - Creates Groq client instance
  - Initializes conversation history

- **Methods**:
  1. `generate_thoughts(message: str) -> str | None`
     - Analyzes user input
     - Temperature: 0.7 (more focused analysis)
     - Max tokens: 2048
     
  2. `generate_response(message: str, thoughts: str | None) -> str | None`
     - Creates responses based on thoughts
     - Temperature: 1.3 (more creative responses)
     - Max tokens: 4096
     
  3. `process_message(message: str) -> dict[str, Any]`
     - Orchestrates the complete interaction flow
     - Maintains conversation history
     - Handles error cases

### Conversation History

- Maintains last 5 interactions
- Format: "user: [message], assistant: [response]"
- Used for context in future interactions

### Error Handling

The system provides graceful error handling:
- Catches and reports exceptions
- Returns formatted error messages
- Maintains system stability

## Usage

Run the assistant using:

```bash
python main.py
```

### Example Interaction:

```
: Hello, who are you?
Vitaz AI: [Thought analysis appears here]
------------
[Response appears here]
```

## Implementation Details

### Models

Uses the `llama3-70b-8192` model through Groq API for both:
- Thought generation
- Response creation

### Configuration

- **Thought Generation**:
  - Lower temperature (0.7) for more focused analysis
  - Systematic approach to understanding user input
  
- **Response Generation**:
  - Higher temperature (1.3) for more dynamic responses
  - Contextually aware using generated thoughts

### System Prompts

- **Thoughts Unit**:
  - Focuses on analysis and planning
  - Considers conversation history and current time
  
- **Response Unit**:
  - Creates natural, conversational responses
  - Uses thought analysis for informed responses

## Best Practices

1. Keep interactions clear and specific
2. Allow time for thought processing
3. Review thought analysis for understanding AI reasoning
4. Monitor for error messages

## Limitations

- Maximum context window of 5 previous interactions
- Dependent on Groq API availability
- Response times may vary based on model load

## Future Improvements

- Expandable context window
- Additional conversation memory mechanisms
- Enhanced error recovery strategies
- Model parameter fine-tuning options

## License

[Add your license information here] Assistant

Vitaz AI is a sophisticated conversational AI assistant that implements a two-stage 
processing system: thought generation and response creation. Built using the Groq 
API, it provides thoughtful and contextually aware responses.

## Features

- **Two-Stage Processing**: Separates thought analysis from response generation
- **Context Awareness**: Maintains conversation history for contextual responses
- **Detailed Thought Process**: Provides visibility into AI's reasoning
- **Error Handling**: Graceful handling of potential runtime issues

## Technical Details

### Requirements

- Python 3.10+
- Groq API access
- Required packages: `groq`

### Architecture

#### VitazAssistant Class

The main class implementing the AI assistant functionality:

- **Initialization**
  - Creates Groq client instance
  - Initializes conversation history

- **Methods**:
  1. `generate_thoughts(message: str) -> str | None`
     - Analyzes user input
     - Temperature: 0.7 (more focused analysis)
     - Max tokens: 2048
     
  2. `generate_response(message: str, thoughts: str | None) -> str | None`
     - Creates responses based on thoughts
     - Temperature: 1.3 (more creative responses)
     - Max tokens: 4096
     
  3. `process_message(message: str) -> dict[str, Any]`
     - Orchestrates the complete interaction flow
     - Maintains conversation history
     - Handles error cases

### Conversation History

- Maintains last 5 interactions
- Format: "user: [message], assistant: [response]"
- Used for context in future interactions

### Error Handling

The system provides graceful error handling:
- Catches and reports exceptions
- Returns formatted error messages
- Maintains system stability

## Usage

Run the assistant using:

```bash
python main.py 
or
uv run main.py
```

### Example Interaction:

```
: Hello, who are you?
Vitaz AI: [Thought analysis appears here]
------------
[Response appears here]
```

## Implementation Details

### Models

Uses the `llama3-70b-8192` model through Groq API for both:
- Thought generation
- Response creation

### Configuration

- **Thought Generation**:
  - Lower temperature (0.7) for more focused analysis
  - Systematic approach to understanding user input
  
- **Response Generation**:
  - Higher temperature (1.3) for more dynamic responses
  - Contextually aware using generated thoughts

### System Prompts

- **Thoughts Unit**:
  - Focuses on analysis and planning
  - Considers conversation history and current time
  
- **Response Unit**:
  - Creates natural, conversational responses
  - Uses thought analysis for informed responses

## Best Practices

1. Keep interactions clear and specific
2. Allow time for thought processing
3. Review thought analysis for understanding AI reasoning
4. Monitor for error messages

## Limitations

- Maximum context window of 5 previous interactions
- Dependent on Groq API availability
- Response times may vary based on model load

## Future Improvements

- Expandable context window
- Additional conversation memory mechanisms
- Enhanced error recovery strategies
- Model parameter fine-tuning options

## License

[Add your license information here]