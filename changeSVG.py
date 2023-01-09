import re

# The list of colors to use
colours = ['#ff453a', '#ff453a', '#fa493a', '#f44c3b', '#ef503b', '#ea543c', '#e5583c', '#df5b3d', '#da5f3d', '#d5633d', '#d0673e', '#ca6a3e', '#c56e3f', '#c0723f', '#bb7640', '#b57940', '#b07d41', '#ab8141', '#a68541', '#a08842', '#9b8c42', '#969043', '#919443', '#8b9744', '#869b44', '#819f44', '#7ca345', '#76a645', '#71aa46', '#6cae46', '#67b247', '#61b547', '#5cb948', '#57bd48', '#52c148', '#4cc449', '#47c849', '#42cc4a', '#3dd04a', '#37d34b', '#32d74b', '#32d74b']



# Open the file "0.svg" and read its contents into a variable



# Replace all occurrences of fill="#ff453a" with the correct color from the list



i = 0
for colour in colours:
    with open("./static/assets/images/mint-round/0.svg", "r") as f:
        svg_contents = f.read()

    matches = re.findall(r"#[a-fA-F0-9]{6}", svg_contents)
    for match in matches:
        svg_contents = svg_contents.replace(match, colour)
        print(matches , colour )
    with open(f"{i}.svg", "w") as f:
        f.write(svg_contents)
    i = i+1


