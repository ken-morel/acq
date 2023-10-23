"""
provide classes for displaying questions
"""#-------------------------------------------------------------------------------
# Name:        question
# Purpose:     provides required classes for displaying questions
#
# Author:      ama
#
# Created:     21/10/2023
# Copyright:   (c) ama 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import base64
import tempfile
from ttkbootstrap import Label, Frame, Radiobutton, Window as Tk
from tkinter import StringVar
from PIL.ImageTk import PhotoImage
class Question(Frame):
    """class Question(Frame):
    subclass of frame to display a question
    """
    opts:dict
    question:StringVar
    answer:str
    value:StringVar
    style:str = ""
    caption:str
    def __init__(self, root:Tk, question:str, options:list[str], answer:chr, caption:bytes=None):
        """def __init__(self, root:Tk, question:str, options:list[str], answer:chr):
        initializes question objct
        """
        assert len(options) == 4, f"in {r:choices}, {len(choices)} options instead of 4"
        super(Question, self).__init__(root, style=self.style)
        self.question = StringVar(value=question)
        self.answer = answer
        self.options = options
        self.caption = caption
        print(self.question.get())
        self.value = val = StringVar()

        if caption:
            self.caption_ = tempfile.NamedTemporaryFile()
            self.caption.write(base64.b64decode(caption))
            self._caption = PhotoImage(file=self.caption_.name)
            Label(self, text=question, image=self._caption).grid(column=1, row=1)
        else:
            Label(self, text=question).grid(column=1, row=1)

        q_frm = Frame(self)
        q_frm.grid(column=2, row=1)
        #a
        Radiobutton(
            q_frm,
            text=options[0],
            variable=val,
            value="a"
        ).grid(column=1, row=1, sticky="w")
        #b
        Radiobutton(
            q_frm,
            text=options[1],
            variable=val,
            value="b"
        ).grid(column=1, row=2, sticky="w")
        #c
        Radiobutton(
            q_frm,
            text=options[2],
            variable=val,
            value="c"
        ).grid(column=1, row=3, sticky="w")
        #d
        Radiobutton(
            q_frm,
            text=options[3],
            variable=val,
            value="d"
        ).grid(column=1, row=4, sticky="w")
    def correct(self) -> bool:
       """def correct(self) -> bool:
       checks if the current selected value is correct
       """
       return self.value.get() == self.answer

class QuestionFrame(Frame):
    """class QuestionFrame(Frame):
    a tkinter.ttk.Frame subclass for holding multiple question objects
    """
    data:dict
    def __init__(self, root, data):
       """def __init__(self, root:Tk, questions:list[dict[str, str|chr]]):
       initializes the question group
       """
       super(QuestionFrame, self).__init__(root)
       self.data = data

       for y, question in enumerate(data):
           Question(self, **question).grid(row=y+1, column=1)

class Paper(Frame):
    """class Paper(Frame):
    creates a paper object
    """
    number:int
    questions:QuestionFrame
    year:int
    subject:str
    exam:str
    data:dict
    def __init__(self, subject, data:dict):
        self.data = data
        super().__init__(subject)

        subject.add(self, sticky="nsew", text=f"{data['subject']} paper {data['paper']}")
        self.questions = QuestionFrame(self, data["questions"])
        self.questions.grid()
