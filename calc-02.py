# Token types
#

INTEGER, PLUS, MINUS, MULTIPLY, DIVIDE, EOF = 'INTEGER', 'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'EOF'


class Token(object):
    def __init__(self, type, value):
        # token type: INTEGER, PLUS, or EOF
        self.type = type
        # token value: 0, 1, 2. 3, 4, 5, 6, 7, 8, 9, '+', or None
        self.value = value

    def __str__(self):
        """String representation of the class instance.
        Examples:
            Token(INTEGER, 3)
            Token(PLUS '+')
        """
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()

class Interpreter(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_token = None
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception('Error parsing input')

    def advance(self):
        self.pos += 1;
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespaces (self):
        while self.current_char!=None and self.current_char.isspace():
            self.advance()
        
    def integer(self):
        result = ''
        while self.current_char!=None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)    

    def get_next_token(self):
        
        while self.current_char != None:    

            if self.current_char.isspace():
                self.skip_whitespaces()
                # continue

            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())

            if self.current_char == '+':
                self.advance()
                return Token(PLUS, '+')

            if self.current_char == '-':
                self.advance()
                return Token(MINUS, '-')
            
            if self.current_char == '*':
                self.advance()
                return Token(MULTIPLY, '*')

            if self.current_char == '/':
                self.advance()
                return Token(DIVIDE, '/')

            self.error()

        return Token(EOF, None)

    def eat(self, token_type):        
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def new_item(self):
        item = self.current_token
        self.eat(INTEGER)
        return item.value

    def expr(self):
        self.current_token = self.get_next_token()

        result = self.new_item()
        while self.current_token.type is (PLUS, MINUS, MULTIPLY, DIVIDE):
            op = self.current_token    
            if op.type == PLUS:
                self.eat(PLUS)
                result += self.new_item()
            elif op.type == MINUS:
                self.eat(MINUS)
                result -= self.new_item()
            elif op.type == MULTIPLY:
                self.eat(MULTIPLY)
                result *= self.new_item()
            elif op.type == DIVIDE:
                self.eat(DIVIDE)
                result /= self.new_item()

        return result

def main():
    while True:
        try:            
            text = input('calc> ')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)

if __name__ == '__main__':
    main()
