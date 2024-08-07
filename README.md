# Book-Buddy-NLP

`Book-Buddy-NLP` is a work-in-progress application that uses Natural Language Processing (NLP) to suggest books based on user queries. While currently under development, it will be a web application upon completion.

## Getting Started

To set up and run this project, follow the steps below:

### Prerequisites

Ensure you have Python 3 installed on your system. You can download it from [python.org](https://www.python.org/downloads).

### Installation

1. **Create a Virtual Environment**

    ```bash
    python3 -m venv venv
    ```

2. **Activate the Virtual Environment**

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

3. **Install the Requirements**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the FastAPI Application**

    ```bash
    python3 run.py
    ```

5. **Access the API Documentation**

    Open your web browser and go to [http://localhost:8000/docs](http://localhost:8000/docs).

6. **Testing the Application with Queries**

    Open your web browser and go to [http://localhost:8000/docs](http://localhost:8000/docs). Navigate to the /recommend-books endpoint and send one of the following queries via "input_string".

    ### Genre Queries
    - "Suggest some epic fantasy series besides 'The Lord of the Rings'."
    - "I'm in the mood for psychological thrillers, any ideas?"
    - "What are some good contemporary romance books?"
    - "Can you list top-rated science fiction novels of the last decade?"
    - "I'd love to dive into some ~. Recommendations?"

    ### Author Queries
    - "Tell me more about books written by Haruki Murakami."
    - "Which Margaret Atwood book should I start with?"
    - "I'm interested in exploring Raymond Chandler's work. Any suggestions?"
    - "List some children's books by Roald Dahl."
    - "What are the most acclaimed novels by Toni Morrison?"