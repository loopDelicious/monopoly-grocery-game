# See if your grocery monopoly piece is a rare or semi-rare piece.

rare_pieces = """
$613C*
$618H
?622D*
?625G
A502C
A504E*
B505A*
B506B
C513D
C514E*
D515A
D517C*
E524D*
E525E
F527B*
F528C
G531A
H538D
I541C
J544B
K549C
L551A
M556B
N562D
O565C
P568B
Q573C
R575A
S579A
T585C
U590D
V592B
W597C
X602D
Y603A
Z608B
"""

print "Enter a 3-digit code from your game piece."
found = False
while found == False:
    searching = raw_input("> ")
    for line in rare_pieces.splitlines():
        line = line.rstrip()
        if searching in line:
            found = True
            print line + "is a rare piece!"




