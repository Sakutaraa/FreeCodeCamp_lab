def arithmetic_arranger(problems, show_answers=False):
      if len(problems) > 5:
          return "Error: Too many problems."

      operators = []
      numbers = []

      for problem in problems:
          num1, operator, num2 = problem.split()
          if operator not in ['+', '-']:
              return "Error: Operator must be '+' or '-'."
          if not (num1.isdigit() and num2.isdigit()):
              return "Error: Numbers must only contain digits."
          if len(num1) > 4 or len(num2) > 4:
              return "Error: Numbers cannot be more than four digits."

          operators.append(operator)
          numbers.extend([num1, num2])

      top_row = ''
      bottom_row = ''
      dashes = ''
      answers = []

      for i in range(0, len(numbers), 2):
          num1, num2, operator = numbers[i], numbers[i + 1], operators[i // 2]
          width = max(len(num1), len(num2)) + 2
          top_row += num1.rjust(width) + '    '
          bottom_row += operator + num2.rjust(width - 1) + '    '
          dashes += '-' * width + '    '
          if show_answers:
              result = int(num1) + int(num2) if operator == '+' else int(num1) - int(num2)
              answers.append(str(result).rjust(width))

      top_row = top_row.rstrip()
      bottom_row = bottom_row.rstrip()
      dashes = dashes.rstrip()
      answer_row = '    '.join(answers) if show_answers else ''

      return '\n'.join([top_row, bottom_row, dashes, answer_row]).rstrip()
