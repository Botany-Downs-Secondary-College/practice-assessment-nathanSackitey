class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question_prompts = [
     "1. What is the safest way to drive up to intersections? \n(a) Look to the right \n(b) Look to the left \n(c) Look behind you \n(d) All of the above", '\n'
     
     "2. If you have to drive at a slow speed that may hold up other vehicles, what should you do? \n(a) Drive at night when there's less traffic \n(b) Keep to the left and let others pass where possible \n(c) Nothing - drive as normal as it's other drivers' responsibility to overtake you safely \n(d) Keep as close as you can to the centre of the road", '\n'
     
     "3. Who is responsible for making a child under 14 years use a seat belt or a safety seat in a vehicle? \n(a) The child's parents \n(b) The driver of the vehicle \n(c) The owner of the vehicle \n(d) The child", '\n'
     
     "4. What is the maximum distance a load may overhang your vehicle behind the rear axle? \n(a) 4 Metres \n(b) 5 Metres \n(c) 6 Metres \n(d) 7 Metres", '\n'
     
     "5. You must NOT park on the right-hand side of the road, except when: \n(a) In the countryside \n(b) Deliviering packages \n(c) Picking up passengers \n(d) In a one way street", '\n'
     
     "6. You are driving in a 100 km/h speed area and you see an Accident sign. What speed must you slow down to? \n(a) 50km/h \n(b) 30km/h \n(c) 40km/h \n(d) 20km/h", '\n'

questions = [
     Question(question_prompts[0], "d"),
     Question(question_prompts[1], "b"),
     Question(question_prompts[2], "b"),
     Question(question_prompts[3], "a"),
     Question(question_prompts[4], "d"),
     Question(question_prompts[5], "d")
]

def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
               print("Correct")
          else:
               print("Unlucky, the correct answer is \"{}\".".format(question.answer))
     print("you got", score, "out of", len(questions))


run_quiz(questions)