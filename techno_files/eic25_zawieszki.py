import subprocess
import os


def read_list(fname="lista.csv"):
    for row in open(fname):
        yield row


def write_preamble(fname):
    preamble = r"""%25 EIC technology, (C) LM 2018
\documentclass{article}
    \usepackage{graphicx}
    \usepackage[space]{grffile}
    \usepackage{anyfontsize}
    \usepackage{fontspec}
    \usepackage{color}
    \setromanfont[
            BoldFont=NexaB.otf,
            ]{NexaL.otf}
    \usepackage{multicol}
    \usepackage[english]{babel}%
    \usepackage[a6paper,left=1cm,right=1cm,top=1cm,bottom=1cm]{geometry}
    \usepackage{lipsum}% http://ctan.org/pkg/lipsum

    \begin{document}
    \pagestyle{empty}

    % top
    \centering{\includegraphics[width=0.9\textwidth,keepaspectratio]{top}}\\
    \vspace*{0.3cm}
    """

    with open(fname, "w") as f:
        f.write(preamble)


def write_player(p, f, photo):
    country = p[0].lower()
    name = p[1].lower()
    surname = p[2].lower()
    dan = p[3].lower()
    role = p[4].lower()
    spec = p[8].lower()

    Name = name.capitalize()
    Surname = surname.capitalize()

    if photo == None:
        photo = "nophoto"

    if dan == "-1":
        dan = "{\color{white}1}"
    elif dan.lower() == "mudan":
        dan = "mudan"
    elif "renshi" in dan:
        dan = "renshi " + dan[0] + " dan"
    elif "kyoshi" in dan:
        dan = "kyoshi " + dan[0] + " dan"
    elif "hanshi" in dan:
        dan = "hanshi " + dan[0] + " dan"
    else:
        dan += " dan"

    name_size = "huge"
    if len(Name) > 8:
        name_size = "Large"

    surname_size = "huge"
    if len(Surname) > 8:
        surname_size = "Large"


    string = "%"
    string += r""" pic name role
    \begin{minipage}[c]{0.3\textwidth}
    \centering{\includegraphics[height=3cm]{foto/%s}}
    \end{minipage}
    \begin{minipage}[c]{0.15\textwidth}
    \phantom{eic}
    \end{minipage}
    \begin{minipage}[c]{0.5\textwidth}
    \begin{flushright}
    {\%s \textbf{%s}}\\
    {\%s \textbf{%s}}\\
    \vspace*{0.3cm}
    {\Large %s}\\{\Large %s}
    \end{flushright}
    \end{minipage}\\
    \vspace*{0.3cm}
    """ % (photo, name_size, Name.split(" ")[0], 
            surname_size, Surname, dan, spec)

    with open(f, "a") as f:
        f.write(string)

def write_country(p, f, C):
    country = p[0].lower()
    string = "%"
    string += r""" country
    \begin{minipage}[c]{0.3\textwidth}
    \centering{\includegraphics[height=1.5cm]{flags/%s}}
    \end{minipage}
    \begin{minipage}[c]{0.15\textwidth}
    \phantom{eic}
    \end{minipage}
    \begin{minipage}[c]{0.5\textwidth}
    \begin{center}
    {\fontsize{30}{40}\selectfont %s}
    \end{center}
    \end{minipage}
    """ % (country, C)

    with open(f, "a") as f:
        f.write(string)


def write_role(p, f):
    role = p[4].lower()

    size = "huge"
    if len(role) > len("manager + competitor"):
        size = "Large"

    string = "%"
    string += r""" role
    \vspace*{0.25cm}
    \begin{center}
    {\%s %s}
    \end{center}
    \vspace*{0.25cm}
    """ % (size, role)

    with open(f, "a") as f:
        f.write(string)


def write_footer(f):
    foot = "%"
    foot += r""" foot
    \centering{\includegraphics[width=\textwidth,keepaspectratio]{footer}}

\end{document}
    """

    with open(f, "a") as f:
        f.write(foot)


def is_in_foto_dir(ekf, path="./foto"):
    for element in os.listdir(path):
        if ekf.lower() in element.lower():
            return element
    return None

if __name__ == "__main__":

    DIR = "./zawieszki/"
    COUNTRIES = "./countries/"

    country = {'pol': 'Poland'}

    rl = read_list()
    for row in rl:
        player = row.split(",")

        country = player[0]
        cou = country[:3].lower()
        fname = player[1]
        lname = player[2]
        dan = player[3]
        role = player[4]
        ekf = player[5]
        pic = player[6]

        fn = fname.lower()
        ln = lname.lower()
        fname = "{}_{}_{}".format(cou, ln, fn)   
        fname_tex = fname + ".tex"
        
        write_preamble(fname_tex)
        photo = None if ekf == "NA" else is_in_foto_dir(ekf)
        write_player(player, fname_tex, photo)
        write_country(player, fname_tex, country) #[player[0]])
        write_role(player, fname_tex)
        write_footer(fname_tex)

        subprocess.call(["ls", fname])
        subprocess.call(["xelatex", fname_tex])
        subprocess.call(["rm", fname_tex, fname + ".log", fname + ".aux"])
        subprocess.call(["mv", fname + ".pdf", DIR])
