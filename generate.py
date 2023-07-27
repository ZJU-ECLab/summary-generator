from hugchat import hugchat
import subprocess
import json
import os


def generate_summary(abstract, chatbot):
    summary = chatbot.chat('\
            Please write a summary of an article based on its abstract. \
            The summary should be very concise, short and easy to understand. \
            Try to make the summary as short as possible. Make sure that the summary is less than four sentences, and about 150-360 words.\
            A possible format is: The research forcuses on [research problem]. [research method]. The results shows that [results and conclusions]. \
            Please reply only with the summary. \
            Here is the abstract, please summarize it with the requirements above: \
            '
                 + abstract)
    return summary

def translate_to_zh(text, method):
    translated = method(text)
    return translated

def translate_DeepLX(text):
    translated = subprocess.run(['curl', '-s', '-d', '{"text":"{' + text +'}", "source_lang":"EN", "target_lang":"ZH"}', '-X', 'POST', '0.0.0.0:1188/translate'], stdout = subprocess.PIPE).stdout
    return translated.decode('utf-8')


if __name__ == '__main__':
    try:
        cookie = os.listdir('usercookies')[0]
    except:
        print('Please run `login.py` first to login!')
        exit()
    chatbot = hugchat.ChatBot(cookie_path = f'usercookies/{cookie}')

    abstract = input('Paste the abstract here:')

    summary = generate_summary(abstract, chatbot)

    if summary == None:
        print('Failed to generate using hugging chat!')
        exit()

    print('\nSummary generated by hugging chat:')
    print(summary)
    print('\n')

    try:
        translated = translate_to_zh(summary, translate_DeepLX)
        translated = json.loads(str(translated))['data']

        print('Translation by DeepL:')
        print(translated)
    except:
        print('Failed to translate!')
