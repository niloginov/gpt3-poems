#!/usr/bin/env python3
import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')

# OpenAI engine to use, probably best to keep davinci
openai_engine = 'davinci'


# Provide a template poem to translate from with contextual info
def provide_openai_template():
    return_string = ''
    return return_string


# Run the completion and provide output
def main():
    # Make sure we can actually get the model to work
    if openai.Engine.retrieve(openai_engine)['ready'] is not True:
        print("Couldn't get OpenAI engine!")
        os.exit(1)

    prompt_string = provide_openai_template()

    # We generate the completion here, and 
    openai.Completion.create(
        engine=openai_engine,
        prompt=prompt_string,
        max_tokens=64
    )


if __name__ == '__main__':
    main()
