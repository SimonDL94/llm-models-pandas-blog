import re
import json
import os
import pandas as pd


def read_json_response(filename):
  with open(filename, "r") as json_file:
    data_dict = json.load(json_file)
  return data_dict


def extract_python_code_from_prompt(text_response):
  pattern = r'```python(.*?)```'
  matches = re.findall(pattern, text_response, re.DOTALL)
  return matches


def get_response_python_codes(directory='_response_data'):
  files = os.listdir(directory)
  output = dict()
  for f in files:
    question_name = f.split('.')[0]
    response_output = read_json_response(directory + '/' + f)['output']
    output[question_name] = extract_python_code_from_prompt(response_output)
  return output


def exec_response_python_codes():
  python_codes = get_response_python_codes()
  results = {
    'question': []
    ,'code': []
    ,'result': []
    ,'error': []
  }
  for q in python_codes:
    code = python_codes[q][0]
    results['code'].append(code)
    results['question'].append(q)
    try:
      exec(code)
      results['result'].append('SUCCESS')
      results['error'].append('NA')
      print('SUCCESS - executing code for question: ' + q)
    except Exception as exc:
      print('FAILED - executing code for question: ' + q)
      results['result'].append('FAILED')
      results['error'].append(str(exc))
      print('EXCEPTION - ' + str(exc))
  output = pd.DataFrame(results)
  return output


if __name__ == '__main__':
  df = exec_response_python_codes()
  print(df)
  print('DONE')


