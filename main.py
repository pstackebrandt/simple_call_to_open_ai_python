# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import openai

def call_open_ai():
    openai.api_key = 'Ihr-API-Schlüssel'

    _response = openai.Completion.create(
        engine="text-davinci-003",  # Prüfen Sie die aktuelle Engine-Version

        prompt="Übersetze den folgenden deutschen Text ins Russische: "
               "Herzlichen Glückwunsch zum Geburtstag liebe Mama!",
        max_tokens=60
    )
    return _response

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    response = call_open_ai()
    print(response.choices[0].text.strip())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
