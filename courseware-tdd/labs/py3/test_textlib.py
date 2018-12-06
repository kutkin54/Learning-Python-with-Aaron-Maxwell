import unittest
from textlib import BodyOfText, Paragraph


class TestBodyOfText(unittest.TestCase):

    def test_single_paragraph(self):
        bodyOfText = BodyOfText("Hello girls")
        self.assertEqual(1, bodyOfText.num_paragraphs())

    def test_several_paragarphs(self):

        text = """This is a rather short story. It has three paragraphs.

        Once upon a time, a brave princess went on a dangerous journey. She
        had many adventures, and recruited other heros to her important and
        noble cause.

        She prevailed, saving the day, and made it home. Yay!"""
        bodyOfText = BodyOfText(text)
        self.assertEqual(3, bodyOfText.num_paragraphs())

    def test_empty_story(self):
        with self.assertRaises(ValueError):
            BodyOfText("")


class TestParagraph(unittest.TestCase):
    def test_empty_paragraph(self):
        with self.assertRaises(ValueError):
            Paragraph("")

    def test_single_sentence(self):
        paragraph = Paragraph("This is one sentence.")
        self.assertEqual(1, paragraph.num_sentences())

    def test_several_sentences(self):
        text = """Once upon a time, a brave princess went on a dangerous journey. She
        had many adventures, and recruited other heros to her important and
        noble cause."""
        paragraph = Paragraph(text)
        self.assertEqual(2, paragraph.num_sentences())
        # Copyright 2015-2018 Aaron Maxwell. All rights reserved
