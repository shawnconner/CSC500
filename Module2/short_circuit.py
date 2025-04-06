true = 0
false = 0


def check(string):
  global true
  print(string)
  true += 1
  return 'this'
  #return True

def false_check(string):
  global false
  false += 1
  print(string)
  return ''
  #return False


if __name__ == '__main__':
    student = True
    teacher = False


    if student or teacher:
        print('Should be at school')
    else:
        print('should not be at school')

    if teacher and student:
        print('Student is the teacher')
    else:
        print('Not a teacher')

    print(false_check('first') or check('second') or check('third') or check('forth') and check('fifth'))
    print(false, true)

    if false_check('blah'):
        print('True')
    else:
        print('False')

    if check('blah'):
        print('True')
    else:
        print('False')


    # true = 0
    # false = 0
    #
    # if false_check('first') and check('second') and check('third') and check('forth') and check('fifth'):
    #     print("Test 1 True")
    # else:
    #     print("Test 1 False")
    #
    #
    # print(false,true)
    #
    # true = 0
    # false = 0
    #
    # if check('first') and check('second') and check('third') and check('forth') and false_check('fifth'):
    #     print("Test 2 True")
    # else:
    #     print("Test 2 False")
    #
    # print(false, true)
    #
    #
    #
