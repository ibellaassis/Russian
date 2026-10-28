


def translator(language):
    translations = {
        'spanish': {
            'hello': 'hola',
            'goodbye': 'adiós',
            'thank you': 'gracias'
        },
        'french': {
            'hello': 'bonjour',
            'goodbye': 'au revoir',
            'thank you': 'merci'
        },
        'italian': {
            'hello': 'ciao',
            'goodbye': 'arrivederci',
            'thank you': 'grazie'
        },
        'german': {
            'hello': 'hallo',
            'goodbye': 'auf Wiedersehen',
            'thank you': 'danke'
        },
        'arabic': {
            'hello': 'مرحبًا',
            'goodbye': 'مع السلامة',
            'thank you': 'شكرًا'
        },
        'portuguese': {
            'hello': 'olá',
            'goodbye': 'tchau',
            'thank you': 'obrigado/obrigada'
        },
        'japanese': {
            'hello': 'こんにちは',
            'goodbye': 'さようなら',
            'thank you': 'ありがとう'
        },
        'chinese': {
            'hello': '你好',
            'goodbye': '再见',
            'thank you': '谢谢'
        },
        'russian': {
            'hello': 'привет',
            'goodbye': 'до свидания',
            'thank you': 'спасибо'
        },
        'korean': {
            'hello': '안녕하세요',
            'goodbye': '안녕히 가세요',
            'thank you': '감사합니다'
        },
        'dutch': {
            'hello': 'hallo',
            'goodbye': 'tot ziens',
            'thank you': 'dank je'
        },
        'turkish': {
            'hello': 'merhaba',
            'goodbye': 'hoşça kal',
            'thank you': 'teşekkür ederim'
        },
        'greek': {
            'hello': 'γεια σου',
            'goodbye': 'αντίο',
            'thank you': 'ευχαριστώ'
        },
        'hindi': {
            'hello': 'नमस्ते',
            'goodbye': 'अलविदा',
            'thank you': 'धन्यवाद'
        },
        'swahili': {
            'hello': 'jambo',
            'goodbye': 'kwaheri',
            'thank you': 'asante'
        }
    }
    
    def translate_word(word):
        if word in translations[language]:
            return translations[language][word]
        return "Word not found."

    return translate_word

translate_to_russian = translator('russian')
print(translate_to_russian('hello'))