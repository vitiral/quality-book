"""csv loading module.

see: REQ-load

"""
#!/usr/bin/python2
import csv


class Question(object):
    """represents a question and can be asked partof: #SPC-question."""

    def __init__(self, question, answer):
        self.question = question.strip()
        self.answer = answer.strip().lower()

    def __eq__(self, other):
        if not isinstance(other, Question):
            return False
        return self.question == other.question and self.answer == other.answer

    def __neq__(self, other):
        return not self == other


def validate_questions(questions):
    """given a list of questions, validate them according to spec.

    partof: #SPC-load-validate
    """
    # check for duplicates
    all_qs = [q.question for q in questions]
    seen = set()
    duplicates = []
    for question in all_qs:
        if question in seen:
            duplicates.append(question)
        seen.add(question)
    if duplicates:
        raise ValueError("duplicate questions found: {}".format(duplicates))


def load_io(open_file):
    """load questions from a file."""
    reader = csv.reader(open_file)
    questions = []
    for row in reader:
        if len(row) == 0 or (len(row) == 1 and not row[0].strip()):
            # skip if the row contains nothing but whitespace
            continue
        if len(row) != 2:
            raise ValueError("row is invalid length of {}: {}".format(
                len(row), row))
        questions.append(Question(*row))
    return questions


def load_path(path):
    """given a path, load a list of validated questions.

    partof: #SPC-load-format
    """
    with open(path, 'rb') as open_file:
        return load_io(open_file)
