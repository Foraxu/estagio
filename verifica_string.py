
class StringCounter:
    def __init__(self) -> None:
        
        self.string = input("Digite uma palavra:")
        self.a_counter = 0
        self.A_counter = 0
        self.verify_string()
        self.print_result()

    def verify_string(self):
        for letter in self.string:
            if letter == 'a':
                self.a_counter += 1
            elif letter == "A":
                self.A_counter += 1
    
    def print_result(self):
        if self.a_counter != 0 or self.A_counter != 0:
            print(f"Na palavra {self.string} há {self.a_counter} letras 'a' e {self.A_counter} letras 'A'.")

        else:
            print(f"Não há nenhuma letra 'a' na palavra {self.string}. Nem maiúsculas ou minúsculas.")

string_counter = StringCounter()