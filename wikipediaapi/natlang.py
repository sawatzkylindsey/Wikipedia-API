import html.parser


class HtmlParser(html.parser.HTMLParser):
    def __init__(self, *args, **kwargs):
        super(HtmlParser, self).__init__(*args, **kwargs)
        self.parts = []
        self.include_stack = [True]

    def handle_starttag(self, tag, attrs):
        if tag.lower() == "math":
            self.include_stack.append(False)
        else:
            # Continue on with the parent level's include flag
            self.include_stack.append(self.include_stack[-1])

    def handle_endtag(self, tag):
        self.include_stack.pop()

    def handle_startendtag(self, attrs):
        pass

    def handle_data(self, data):
        if self.include_stack[-1]:
            self.parts.append(data)

    def get_text(self):
        return "".join(self.parts)

