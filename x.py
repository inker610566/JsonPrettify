import json

output = u""


indent_string = u"    "

def re(json, indent):
    global output
    if type(json).__name__ == "list":
        output += u"[\n"
        for x in json:
            re(x, indent+1)
            output += u",\n"
        output = output[:-2]
        output += u"\n%s]" % (indent_string*indent,)
    elif type(json).__name__ == "dict":
        output += u"\n%s{" % (indent_string*indent,)
        for k, v in json.iteritems():
            output += u"\n%s\"%s\":" %(indent_string*(indent+1),k,)
            re(v, indent+2)
            output += u","
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
            output += u"\"" + json + u"\""
        except UnicodeDecodeError:
            pass
            #print json.encode("utf-8")
    elif type(json).__name__ == "str":
        output += u"\"%s\"" % (json.encode("utf-8"),)
    else:
        output += str(json).encode("utf-8")

re(json.load(open("01org/2015-05-05.json", "r")), 0)

print output.encode("utf-8")
