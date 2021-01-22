import os

with open("./out/output.txt", "w") as f:
    for filename in os.listdir("./"):
        if filename.endswith(".txt"):
            f.write("<pre>")
            with open(filename, "r") as g:
                f.writelines(g.readlines())
            f.write("</pre>")
