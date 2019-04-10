import sys
import re


def main():
    f = open("sola.ai-out", "r")
    output = open("users", "w")
    pattern = "^https://sola.ai/([^/]+)$"
    for x in f:
        y = re.findall(pattern, x)
        if y: 
            output.write("profile:{}".format(y[0]))
    f.close()
    output.close()


if __name__ == '__main__':
    main()
