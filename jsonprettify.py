output = u""

indent_string = u"    "

def JsonPrettify(json_obj):
    global output
    output = u""
    def re(json, indent):
        global output
        if type(json).__name__ == "list":
            output += indent_string*indent + u"[\n"
            for x in json:
                re(x, indent+1)
                output += u",\n"
            output = output[:-2]
            output += indent_string*indent + u"["
        elif type(json).__name__ == "dict":
            output += indent_string*indent + u"{\n"
            for k, v in json.iteritems():
                output += u"%s\"%s\":\n" %(indent_string*(indent+1),k,)
                re(v, indent+2)
                output += u",\n"

            if json: output = output[:-2]
            output += u"\n%s}" % (indent_string*indent,)

        elif type(json).__name__ == "unicode":
            try:
                '''
                print "Output"
                print type(output).__name__
                print "Real"
                print type(json).__name__
                print json.encode("utf-8")
                '''
                output += indent_string*indent + u"\"" + json + u"\""
            except UnicodeDecodeError:
                pass
                #print json.encode("utf-8")
        elif type(json).__name__ == "str":
            output += indent_string*indent + u"\"%s\"" % (json.encode("utf-8"),)
        else:
            output += indent_string*indent + str(json).encode("utf-8")

    re(json_obj, 0)

    return output

if __name__ == "__main__":
    import json
    print JsonPrettify(json.load(open("../hsc-visualize/a.json", "r")))
    #print json.dumps({"body": [1,2,3]})
    

