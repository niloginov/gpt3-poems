#!/usr/bin/env python3
import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')

# OpenAI engine to use, probably best to keep davinci, but curie might also work
openai_engine = 'davinci'


# Provide a template poem to translate from to provide some context for GPT-3
def get_template_string():
    ret = ''
    english_data = []
    chinese_data = []

    with open('training_data_english.txt', 'r') as file:
        english_data = file.read().split('\n')

    with open('training_data_chinese.txt', 'r') as file:
        chinese_data = file.read().split('\n')

    if len(chinese_data) != len(english_data):
        raise ValueError('Training data length mismatch!')
        os.exit(1)

    for i in range(len(english_data)):
        ret += 'Chinese: ' + chinese_data[i] + '\n\n'
        ret += 'English: ' + english_data[i] + '\n'

    return ret


# Get an input string from file to translate
def get_input_string():
    ret = 'Chinese: '

    with open('test_data_chinese.txt', 'r') as file:
        ret += file.read().strip('\n')

    ret += '\nEnglish: '

    return ret


# Run the completion and provide output
def main():
    # Make sure we can actually get the model to work
    if openai.Engine.retrieve(openai_engine)['ready'] is not True:
        raise Exception('Couldn\'t get OpenAI engine!'')
        os.exit(1)

    # Get in training data
    prompt_string = get_template_string() + get_input_string()

    # Generate the completion with GPT-3
    resp = openai.Completion.create(
        engine=openai_engine,
        prompt=prompt_string,
        max_tokens=64
    )

    # Print it out!
    print(resp)


if __name__ == '__main__':
    main()
