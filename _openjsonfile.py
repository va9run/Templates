def jsonfile(filelocation,name):
    file = open(filelocation+"/"+name, "r", encode='utf-8')
    dataunfold = json.load(file)
    finaldata = pd.json_normalize(dataunfold['data'])
    return finaldata