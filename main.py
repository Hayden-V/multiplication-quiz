import time

import pyinputplus
import pyinputplus as pyip

print('Beginning multiplication quiz. There are ten questions to the quiz. You will have three tries to answer '
      'each question. If you do not make an attempt in eight seconds, the questions will be marked as incorrect.')
correct = 0
incorrect = 0

for i in range(0, 10):
    for q in range(1, 5):
        if q == 4:
            incorrect += 1
            break
        print("What is", i, "x", i, "?")
        try:
            if pyip.inputNum(timeout=8) == i * i:
                correct += 1
                print("Correct!")
                time.sleep(1)
                break
            else:
                incorrect += 1
                if 3 - q == 1:
                    print("Incorrect, you have 1 try left")
                elif 3 - q == 0:
                    print("Incorrect, you have no more attempts for this problem")
                else:
                    print("Incorrect, you have", 3 - q, "tries left.")
        except pyinputplus.TimeoutException:
            incorrect += 1
            if 3 - q == 1:
                print("Incorrect, you were too slow. You have 1 try left")
            elif 3 - q == 0:
                print("Incorrect, you were too slow. You have no more attempts for this problem")
            else:
                print("Incorrect, you were too slow. You have", 3 - q, "tries left.")

print("The quiz is over. You answered", correct, "out of 10 questions correctly.")