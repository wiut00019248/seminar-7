eng_to_uzb = {
  'one': 'bir',
  'two': 'ikki',
  'three': 'uch',
  'four': 'to\'rt',
  'five': 'besh',
  'six': 'olti',
  'seven': 'yetti',
  'eight': 'sakkiz',
  'nine': 'to\'qqiz',
  'ten': 'o\'n',
}

def eng_to_uzb_translator() -> None:
  for i, j in eng_to_uzb.items():
    print(f"{i}: {j}")

eng_to_uzb_translator()

final_marks = {
  'cs': 99,
  'wf': 98,
  'prog': 95,
  'imob': 98,
  'stats': 96
}

def calc_average(finals: dict) -> float:
  sum = 0
  for i in finals.values():
    sum += i
  return sum / len(finals)

print(calc_average(final_marks))

def input_formatter(user_input: str) -> dict:
  final_marks = {}
  for i in user_input.split(', '):
    subject, mark = i.split(': ')
    final_marks[subject] = mark
  return final_marks

def calc_avg() -> float:
  final_marks = {}
  user_input = input("Enter marks: ")
  final_marks = input_formatter(user_input)
  sum = 0
  for i in final_marks.values():
    sum += int(i)
  return round(sum / len(final_marks), 2)

print(calc_avg())
  


