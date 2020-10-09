from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

languages = [{'name': 'java'}, {'name': 'python'}, {'name': 'ruby'}]

@app.route('/', methods=['GET'])
def test():
    return jsonify({'message': 'It works'})

@app.route('/lang', methods=['GET'])
def return_all_languages():
    return jsonify({'languages': languages})

@app.route('/lang/<string:name>', methods=['GET'])
def return_lang_with_name(name: str):
    langs = [language for language in languages if language['name'] == name]
    return jsonify({'language': langs[0]})

@app.route('/lang', methods=['POST'])
def add_lang():
    language = request.get_json()
    languages.append(language)
    return jsonify({'languages': languages})


@app.route('/lang/<string:name>', methods=['PUT'])
def update_lang(name: str):
    langs = [language for language in languages if language['name'] == name]
    print(langs)
    langs[0]['name'] = request.get_json()['name']
    return jsonify({'language': langs[0]})

@app.route('/lang/<string:name>', methods=['DELETE'])
def delete_lang(name: str):
    langs = [language for language in languages if language['name'] == name]
    languages.remove(langs[0])
    return jsonify({'languages': languages})

if __name__ == '__main__':
    app.run(debug=True, port=8080)