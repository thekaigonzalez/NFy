import argparse
import json

parser = argparse.ArgumentParser("news_writer")

parser.add_argument("FILE", help="File to parse into the JSON news. This is required.")

args = parser.parse_args()

def parse_newsj(newscode):
    """ Ugh... Why do I keep writing parsers?! """

    state = 0
    buffer = ""

    author="Nobody"
    title = "None"
    parag = ""

    for n in newscode:
        if n == '(' and state == 0:
            state = 5
            buffer = ""
        
        elif n == ')' and state == 6:
            state = 399
            author = buffer.strip()
            buffer = ""
        elif n == '/' and state == 5:
            state = 6
            title = buffer.strip()
            buffer = ""
        elif n == '\n' and state == 0:
            state = 399
        else:
            buffer += n
    parag = buffer

    return {
        'author': author,
        "body": parag.strip(),
        'title': title
    }

file = open(args.FILE, "r")
dic = parse_newsj(file.read())
file.close()

js = json.dumps(dic)
file2 = open(args.FILE[:args.FILE.find(".")] + ".json", "w")
file2.write(str(js))
file2.close()

file2 = open(args.FILE[:args.FILE.find(".")] + ".html", "w")
file2.write("<h1> " + dic['title'] + "</h1>\n\n<p>" + dic['body'] + "</p>")
file2.close()