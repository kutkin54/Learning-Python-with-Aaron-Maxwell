class BodyOfText:
    def __init__(self, text):
        if text.strip() == "":
            raise ValueError
        self.text = text

    def num_paragraphs(self):

        return len(self.paragraphs())

    def paragraphs(self):
        if self.text.strip() == "":
            return []
        return self.text.strip().split('\n\n')


class Paragraph:
    def __init__(self, text):
        if text.strip() == "":
            raise ValueError
        self.text = text

    def num_sentences(self):
        return len(self.sentences())

    def sentences(self):
        if self.text.strip() == "":
            return []
        sentences = self.text.strip().split(".")
        if sentences[-1] == "":
            sentences.pop()
        else:
            raise ValueError
        return sentences
# Copyright 2015-2018 Aaron Maxwell. All rights reserved.
