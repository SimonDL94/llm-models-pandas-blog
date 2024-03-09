# llm-models-pandas-blog
- code related to testing ANTHROTOPIC Claude LLM model by asking pandas questions
- necessary packages: pandas, numpy and scikit-learn
- Claude model version used: "claude-3-opus-20240229"

- scripts:
    - anthropic_api.py 
      - py script to make a call to the anthrotopic API and saving the json responses under hidden '_response_data' folder
    - main.py
      - py script to extract python code from the saved jsons responses - after calling
    - pandas_questions.py
      - py script that contains the pandas / python questions asked to claude
    - secrets.yaml (to store your personal API key)
      - ANTHROTOPIC_API_KEY:
    - requirements.txt
    - _response_data
      - input prompts / string questions - and answers returned from Claude API language model
