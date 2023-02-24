from random import randint


class MathUtils:
    @staticmethod
    def calc(operand_1, operator, operand_2):
        if operator == '+':
            return operand_1 + operand_2
        elif operator == '-':
            return operand_1 - operand_2
        elif operator == '*':
            return operand_1 * operand_2
        elif operator == '/':
            return operand_1 / operand_2

    @staticmethod
    def int_or_none(string):
        try:
            return int(string)
        except ValueError:
            return None


class QPrompts:
    LEVELS = ['simple operations with numbers 2-9',
              'integral squares of 11-29']

    def __init__(self, level: int, questions_total: int):
        self.level = level
        self.questions_total = questions_total

    @staticmethod
    def ask_level():
        while True:
            print('Which level do you want? Enter a number:')
            for idx, LEVEL in enumerate(QPrompts.LEVELS):
                print(f'{idx + 1} - {LEVEL}')
            level = MathUtils.int_or_none(input())
            if level in (1, 2):
                return level

    def ask_question(self):
        if self.level == 1:
            operator = ['+', '-', '*'][randint(0, 2)]
            operand_1 = randint(2, 9)
            operand_2 = randint(2, 9)
            print(f'{operand_1} {operator} {operand_2}')
            result = MathUtils.calc(operand_1, operator, operand_2)
        elif self.level == 2:
            num = randint(11, 29)
            print(num)
            result = num ** 2
        else:
            raise ValueError('Invalid level')

        while True:
            inputted_result = MathUtils.int_or_none(input())
            if inputted_result is None:
                print('Incorrect format.')
            else:
                return 'Right!' if inputted_result == result else 'Wrong!'

    def ask_questions(self):
        correct_count = 0
        for _ in range(self.questions_total):
            res = self.ask_question()
            if res == 'Right!':
                correct_count += 1
            print(res)
        return correct_count

    def print_result(self, correct_count):
        total = self.questions_total

        print(f'Your mark is {correct_count}/{total}.',
              'Would you like to save the result? Enter yes or no.')

        if input() in ['yes', 'YES', 'y', 'Yes']:
            print('What is your name?')

            level_desc = QPrompts.LEVELS[self.level - 1]
            filename = 'results.txt'
            user_name = input()

            phrase = ' '.join([f'{user_name}: {correct_count}/{total}',
                               f'in level {self.level} ({level_desc}).'])

            with open(filename, 'a') as f:
                f.write(phrase)

            print(f'The results are saved in "{filename}".\n')


def main():
    level = QPrompts.ask_level()
    prompts = QPrompts(level, 5)

    correct_count = prompts.ask_questions()
    prompts.print_result(correct_count)


if __name__ == '__main__':
    main()
