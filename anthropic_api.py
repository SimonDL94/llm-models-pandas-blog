import anthropic
import yaml
import json
import pandas_questions

MODEL = "claude-3-opus-20240229"


def get_secrets_api_key():
    with open('secrets.yaml') as file:
      output = yaml.safe_load(file)['ANTHROTOPIC_API_KEY']
    return output


def get_response(message, model=MODEL):

    client = anthropic.Anthropic(
      api_key=get_secrets_api_key(),
    )
    response = client.messages.create(
      model=model,
      max_tokens=1000,
      temperature=0,
      system=message,
      messages=[
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": message
            }
          ]
        }
      ]
    )
    return response.content[0].text


def save_response_json(prompt, output, filename):
  output_dict = dict()
  output_dict['prompt'] = prompt
  output_dict['output'] = output
  json_object = json.dumps(output_dict, indent=4)
  with open('_response_data/' + filename, "w") as outfile:
    outfile.write(json_object)


def get_responses_from_pandas_questions():
  for q in pandas_questions.QUESTIONS_DICT:
    print('getting response for question: ' + str(q))
    prompt = 'can you give me fully working python code to do the following with the Python pandas library:'
    prompt += prompt + ' ' + pandas_questions.QUESTIONS_DICT[q]
    response = get_response(
      message=prompt
    )
    save_response_json(
      prompt=prompt
      , output=response
      , filename=q + '.json'
    )


if __name__ == '__main__':
  get_responses_from_pandas_questions()
  print('DONE')




