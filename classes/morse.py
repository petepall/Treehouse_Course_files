class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern

    def __iter__(self):
        yield from self.pattern

    def __str__(self):
        output = []
        for blip in self:
            if blip == '.':
                output.append('dot')
            else:
                output.append('dash')
        return '-'.join(output)

    @classmethod
    def from_string(cls, message_text):
        output = []
        message_words = message_text.split('-')
        for word in message_words:
            if word.lower() == 'dot':
                output.append('.')
            else:
                output.append('_')
        return cls(output)


class S(Letter):
    def __init__(self):
        pattern = ['.', '.', '.']
        super().__init__(pattern)


print(Letter.from_string("dash-dot"))
