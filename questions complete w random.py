import random
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
     
     "7. If you have a learner licence you can carry passengers if your supervisor is in the back seat?\n(a) True \n(b) False", '\n'
        
     "8. A broken yellow line painted close to the edge of the road means you may stop or park your vehicle there at any time?\n(a) True \n(b) False", '\n'
        
     "9. When you have a learner licence you do not have to have it with you when you drive if your supervisor has their licence with them?\n(a) True \n(b) False", '\n'
     
     " 10. What must you do before turning left into a driveway?\n(a) Check the driveway is clear and enter \n(b) Signal for 3 seconds or more and if the driveway is clear enter \n(c) Signal only if there is a vehicle behind you and enter \n(d) Signal only if another vehicle is coming towards you and enter", '\n'
        
     "11. What is the minimum tread depth required for car tyres?\n(a) 0.5mm \n(b) 1.0mm \n(c) 1.5mm \n(d) 2.0mm", '\n'
        
     "12. What is the recommended distance you should allow when driving past a cyclist? \n(a) 0.5 metres \n(b) 1.0 metres \n(c) 1.5 metres \n(d) 2.0 metres", '\n'
        
     "13. If you can do so safely, you may pass on the left at an intersection if:\n(a) You have the headlights of your vehicle turned on \n(b) The vehicle in front is signalling a right turn \n(c) The vehicle in front is signalling a left turn \n(d) The vehicle in front is going faster than the speed limit",'\n'

     "14. Can you stop on a bus stop in a private motor vehicle? \n(a) When dropping off passengers \n(b) Only if it is for less than 5 minutes \n(c) Only between midnight and 6am \n(d) No ", '\n'
     
     "15. You should check that there is space for your vehicle on the other side of the crossing before going over a railway level crossing.\n(a) True \n(b) False", '\n'
     
     "16. To help you from being blinded by the headlights of an oncoming vehicle, what should you do?\n(a) Turn the headlights of your vehicle onto high beam \n(b) Look to the right-hand side of the road \n(c) Look at the centre of the road \n(d) Look to the left-hand side of the road ", '\n'
     
     "17. When must you turn your vehicle headlights on? \n(a) 15 minutes after sunset until 15 minutes before sunrise \n(b) 30 minutes after sunset until 30 minutes before sunrise \n(c) 45 minutes after sunset until 45 minutes before sunrise  \n(d) 1 hour after sunset until 1 hour before sunrise", '\n'
     
     "18. What should you do if the vehicle behind you starts to pass you?\n(a)Move over to the right so that they cannot pass \n(b)Speed up so that they will not need to pass \n(c)Signal for them to stay behind you because you think they are going too fast \n(d) Move as far to the left side of the road as is safe and do not speed up", '\n'
     
     "19. If anybody is hurt in a crash, the driver must tell a police officer as soon as possible but within:\n(a) 24 hours \n(b) 36 hours \n(c) 48 hours \n(d) 60 hours", '\n'

     "20. A police officer can impound your car on the spot if you are caught driving while disqualified.\n(a) True \n(b) False",     
]

questions = [
     Question(question_prompts[0], "d"),
     Question(question_prompts[1], "b"),
     Question(question_prompts[2], "b"),
     Question(question_prompts[3], "a"),
     Question(question_prompts[4], "d"),
     Question(question_prompts[5], "d"),
     Question(question_prompts[6], "b"),
     Question(question_prompts[7], "b"),
     Question(question_prompts[8], "b"),
     Question(question_prompts[9], "b"),
     Question(question_prompts[10], "c"),
     Question(question_prompts[11], "c"),
     Question(question_prompts[12], "b"),
     Question(question_prompts[13], "d"),
     Question(question_prompts[14], "a"),
     Question(question_prompts[15], "d"),
     Question(question_prompts[16], "b"),
     Question(question_prompts[17], "d"),
     Question(question_prompts[18], "a"),
     Question(question_prompts[19], "a")
]     
random.shuffle(questions)

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