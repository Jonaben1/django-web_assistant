import openai
from .secret_key import API_KEY

openai.api_key = API_KEY

def chatgpt(request):
    prompt = request.POST.get('prompt')
    response = openai.Completion.create(
        engine='text-davinci-003',
        temperature=1,
        prompt=prompt,
        max_tokens=1000,
    )
    res = response.choices[0].text
    chats = {'prompt':prompt,
            'response':  res
            }
    return chats
