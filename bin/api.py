from flask import Flask, render_template, request, Response,redirect
import main
import requests
import spacy
import os
import json
app = Flask(__name__)


@app.route("/<path>", methods=['GET'])
def home(path):

    

    nlp = spacy.load('en_core_web_md')
    main.location = "../data/input/" +path
    result = main.main()

    
    result = result.to_dict()


    def set_default(obj):
        if isinstance(obj, set):
            return list(obj)
        raise TypeError

    return json.dumps(result,default=set_default,indent= 10)



if __name__ == '__main__':
     app.run(debug= True)
