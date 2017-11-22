class FormField(object):
    def __init__(self, title, help_text=None):
        self.title = title
        self.help_text = help_text
        self.answer = None

    def submit_answer(self, answer):
        self.answer = answer

    def get_answer(self):
        return self.answer

    def is_valid(self):
        if self.get_answer() == None:
            raise ValueError


class TextField(FormField):
    def is_valid(self):
        super().is_valid()
        return self.get_answer() != ""


class EmailField(FormField):
    def is_valid(self):
        super().is_valid()
        return "@" in self.get_answer()


class URLField(FormField):
    def is_valid(self):
        super().is_valid()
        return "http" in self.get_answer()


class MultipleChoiceField(FormField):
    def __init__(self, title, options, help_text=None):
        self.title = title
        self.options = options
        self.help_text = help_text
        self.answer = None

    def is_valid(self):
        super().is_valid()
        return self.get_answer() in self.options


text_field = TextField("hello world")
text_field.submit_answer("hello to you stranger")
text_field.is_valid()
