# we are rebuilding the previous version from scratch by memory, to make sure we understand everything 
PLUS, MINUS, INTEGER, EOF = "PLUS", "MINUS", "INTEGER", "EOF";

class Tokenizer (object) :
# class Token (object) :
    def __init__ (self, type, value) :
        self.type = type;
        self.value = value;

    def create (self) : 
        return 'Token({type}, {value})'.format(
            type = self.type,
            value = repr(self.value)
        );

    def __repr__ (self) :
        return self.create();

# create class (lexer) to recognize blocks divided by space, tokenize and return to main (where they will be printed)
class Print (object) :
    def __init__ (self, text) :
        self.text = text;
        self.position = -1;

    def advance (self) :
        self.position += 1;
        self.current_char = self.text[self.position];

    def get_integer (self) :
        container = '';
        while self.current_char.isdigit() and self.current is not None:
            container += self.current_char;
            self.advance();        
        return int(container);

    def get_next_token (self) :
        while self.current_char is not self.current_char.isspace() :
            if self.current_char.isdigit() :
                return Tokenizer(INTEGER, self.get_integer());


class Pikaciu (object) :
    def __init__ (self, text) :
        self.text = text;

    def attack (self):
        print (self.text);




def main ():
    while True:
        try:
            text = input ("Please enter: ");
        except EOFError:
            break;
        if not text:
            continue;      
    
if __name__ == '__main__':
    main()
