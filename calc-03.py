
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
