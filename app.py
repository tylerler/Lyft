from flask import Flask, request

app = Flask(__name__)


@app.route('/test', methods=['POST'])
def parse():
    string_to_cut = request.json['string_to_cut']
    answer_string = cut_string(string_to_cut)
    return_json = {
        "return_string": answer_string,
    }
    return json.dumps(return_json)

def cut_string(string):
    i = 0
    cut_list = []
    for char in string:
        i += 1
        if i == 3:
            cut_list.append(char)
            i = 0
    return "".join(cut_list)

app.run(host='0.0.0.0', port=5000, debug=True)
