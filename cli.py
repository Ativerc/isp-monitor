from prompt_toolkit import HTML
from prompt_toolkit import print_formatted_text 
from prompt_toolkit.styles import Style
from prompt_toolkit.formatted_text import FormattedText

print_formatted_text('Hello World!')
print_formatted_text(HTML('<b>This is bold</b>'))
print_formatted_text(HTML('<u>This is underlined</u>'))


# Colors from the ANSI palette.
print_formatted_text(HTML('<ansired>This is red</ansired>'))
print_formatted_text(HTML('<ansigreen>This is green</ansigreen>'))

# Named colors (256 color palette, or true color, depending on the output).
print_formatted_text(HTML('<skyblue>This is sky blue</skyblue>'))
print_formatted_text(HTML('<seagreen>This is sea green</seagreen>'))
print_formatted_text(HTML('<violet>This is violet</violet>'))


# Colors from the ANSI palette.
print_formatted_text(HTML('<aaa fg="ansiwhite" bg="ansigreen">White on green</aaa>'))

style = Style.from_dict({
    'aaa': '#ff0066',
    'bbb': '#44ff00 italic',
})

print_formatted_text(HTML('<aaa>Hello</aaa> <bbb>world</bbb>!'), style=style)


text = FormattedText([
    ('#ff0066', 'FormattedText Hello'),
    ('', ' '),
    ('#44ff00 italic', 'World'),
])

print_formatted_text(text)