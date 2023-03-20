# Code for Intelligent Tutors

import random

class IntelligentTutor:
    def present_concept(self, concepts):
        self.concepts = concepts
        self.student_model = {}
        concept = random.choice(self.concepts)
        print("Let's learn about " + concept)
        self.student_model[concept] = {"p": 0.5, "num_attempts": 0, "num_correct": 0}

    def present_question(self, questions, feedback):
        concept = random.choice(list(self.student_model.keys()))
        question = random.choice(questions[concept])
        print(question["text"])
        self.student_model[concept]["num_attempts"] += 1
        answer = input("Enter your answer: ")
        if answer == question["answer"]:
            print(feedback["positive"])
            self.student_model[concept]["num_correct"] += 1
        else:
            print(feedback["negative"])
        self.student_model[concept]["p"] = self.bkt_update(concept)

    def bkt_update(self, concept):
        p_prev = self.student_model[concept]["p"]
        learn_rate = 0.3
        guess_rate = 0.1
        slip_rate = 0.2
        if self.student_model[concept]["num_attempts"] == 0:
            return p_prev
        if self.student_model[concept]["num_correct"] == self.student_model[concept]["num_attempts"]:
            return 1.0
        if self.student_model[concept]["num_correct"] == 0:
            return 0.0
        p = learn_rate * (1 - p_prev) + p_prev
        p = guess_rate * (1 - p_prev) + (1 - slip_rate) * p
        return p

# Example usage
concepts = ["addition", "subtraction", "multiplication", "division"]
questions = {
    "addition": [{"text": "What is 2 + 2?", "answer": "4"}, {"text": "What is 5 + 7?", "answer": "12"}],
    "subtraction": [{"text": "What is 5 - 2?", "answer": "3"}, {"text": "What is 10 - 4?", "answer": "6"}],
    "multiplication": [{"text": "What is 3 x 4?", "answer": "12"}, {"text": "What is 7 x 6?", "answer": "42"}],
    "division": [{"text": "What is 10 / 2?", "answer": "5"}, {"text": "What is 12 / 3?", "answer": "4"}]
}
feedback = {"positive": "Great job!", "negative": "Try again."}
it = IntelligentTutor()

for i in range(10):
    it.present_concept(concepts)
    for j in range(3):
        it.present_question(questions, feedback)









