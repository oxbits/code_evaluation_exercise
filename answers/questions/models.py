from django.db import models


class QuestionSet(models.Model):

    set_name = models.CharField(
        max_length=256, blank=True, null=True, default='', 
    )

    def __str__(self):
        return self.set_name


class Question(models.Model):

    text = models.TextField(
        blank=True, null=True, default='', 
    )

    token = models.CharField(
        max_length=256, blank=True, null=True, default='', 
    )

    question_set = models.ForeignKey(
        QuestionSet, on_delete=models.CASCADE, blank=True, null=True, 
        related_name='set_question', 
    )

    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    def __str__(self):
        return self.question_set.set_name + ': ' + self.token


class Answer(models.Model):

    YES = 'Y'
    NO = 'N'
    YES_OR_NO = (
        (YES, 'yes'),
        (NO, 'no'),
    )
    
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, blank=True, null=True, 
        related_name='question_answer', 
    )

    text = models.CharField(
      max_length=1,choices=YES_OR_NO,blank=True, null=True, 
    )

    def __str__(self):
        return (
            self.question.token + 
            ' | ' + 
            self.text + 
            ' | answer: ' + 
            str(self.id)
        )


class Image(models.Model):
    
    file = models.ImageField(
        blank=True, null=True, 
    )
    
    answer = models.ForeignKey(
        Answer, on_delete=models.CASCADE, blank=True, null=True, 
        related_name='answer_image', 
    )

    def __str__(self):
        return str(
            self.answer.question.question_set.set_name + 
            ' | ' + 
            self.answer.question.token + 
            ' | answer: ' + str(self.answer.id) + 
            ' | image: ' + str(self.id)
            )

