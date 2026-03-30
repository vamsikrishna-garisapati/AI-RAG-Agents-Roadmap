# SETUP.md

## Comprehensive Setup and Installation Guide

### Prerequisites
Before you start, ensure you have the following installed on your system:
- Python 3.8 or higher
- pip (Python package manager)
- Git (for version control)

### Step-by-Step Installation Instructions

1. **Clone the Repository**  
   Open your terminal and run the following command:  
   ```bash  
   git clone https://github.com/vamsikrishna-garisapati/AI-RAG-Agents-Roadmap.git  
   ```  

2. **Navigate to the Project Directory**  
   ```bash  
   cd AI-RAG-Agents-Roadmap  
   ```  

3. **Set Up Virtual Environment**  
   It's recommended to use a virtual environment to manage dependencies:  
   ```bash  
   python -m venv venv  
   ```  
   Activate the virtual environment:  
   - On Windows:  
     ```bash  
     venv\Scripts\activate  
     ```  
   - On macOS/Linux:  
     ```bash  
     source venv/bin/activate  
     ```  

4. **Install Dependencies**  
   Install the required packages using pip:  
   ```bash  
   pip install -r requirements.txt  
   ```  

5. **API Key Configuration**  
   Obtain your API key from the respective service you are going to use and add it to your environment variables:
   - On Windows:  
     ```bash  
     setx API_KEY "your_api_key_here"  
     ```  
   - On macOS/Linux:  
     ```bash  
     export API_KEY="your_api_key_here"  
     ```  

### Project Execution Examples
To run the project, execute:  
```bash  
python main.py  
```

### Troubleshooting
- If you face issues while installing dependencies, ensure your Python version is compatible and try upgrading pip:  
```bash  
pip install --upgrade pip  
```

- If the program raises API errors, double-check your API key configuration and permissions.

### Next Steps
Once you have set up the project and ensured everything is working:
- Explore the different features of the project.
- Contribute to the project by fixing issues or adding new features.
- Check the [Contributing Guidelines](CONTRIBUTING.md) for more information.
