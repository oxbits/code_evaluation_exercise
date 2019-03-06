from django.test import TestCase
from .models import (
    QuestionSet,
    Question,
    Answer,
    Image,
)

# Create your tests here.

class QuestionAnswerTestCase(TestCase):
    def setUp(self):
        
        question_set = QuestionSet.objects.create(
            set_name='test set',
        )

        question = Question.objects.create(
            text='test question',
            token='test token',
            question_set=question_set,
            order=0,
        )

        answer = Answer.objects.create(
            text='Y',
            question=question,
        )


    def test_question_set(self):
        question_set = QuestionSet.objects.get(set_name='test set')
        self.assertEqual(question_set.set_name, 'test set')
        

    def test_question(self):
        question_set = QuestionSet.objects.get(set_name='test set')
        question = Question.objects.get(text='test question')
        self.assertEqual(question.text, 'test question')
        self.assertEqual(question.token, 'test token')
        self.assertEqual(question.question_set, question_set)
        self.assertEqual(question.order, 0)
        

    def test_answer(self):
        question = Question.objects.get(text='test question')
        answer = Answer.objects.all()[0]
        self.assertEqual(answer.text, 'Y')
        self.assertEqual(answer.question, question)
        

