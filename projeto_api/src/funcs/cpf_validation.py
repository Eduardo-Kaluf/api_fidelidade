from constantes import FIRST_DIGIT_POSITION, SECOND_DIGIT_POSITION, CPF_LENGHT, FIRST_DIGIT_MULTIPLIER, SECOND_DIGIT_MULTIPLIER, MULTIPLIER, DIVIDER

"""
Para o CPF ser considerado válido os seguintes critérios precisam ser verdadeiros:
    - O resto da multiplicação dos primeiros 9 primeiros dígitos por 10 - n (10, 9, 8...), dividido por 11, igual ao primeiro digito depois do "-"
    - O resto da multiplicação dos primeiros 10 primeiros dígitos por 11 - n (11, 10, 9...), dividido por 11, igual ao segundo digito depois do "-"
    - Tamanho total igual a 11
"""


class CPF():
    def __init__(self, cpf):
        self.cpf = cpf
        self._remove_mascara()

    def _remove_mascara(self):
        self.cpf = self.cpf.replace(".", "")
        self.cpf = self.cpf.replace("-", "")

    def _length_verification(self):
        if len(self.cpf) != CPF_LENGHT:
            return 0
        return 1

    def _digit_verification(self, digit_multiplier = int):
        temp = []
        for i, x in zip(self.cpf, list(reversed(range(2, digit_multiplier)))):
            temp.append(int(i) * x)
        return ((sum(temp) * MULTIPLIER) % DIVIDER)

    def cpf_validation(self):
        if not self.cpf.isdigit() or not self._length_verification():
            return 0
        elif (self._digit_verification(FIRST_DIGIT_MULTIPLIER)  != int(self.cpf[FIRST_DIGIT_POSITION]) or 
              self._digit_verification(SECOND_DIGIT_MULTIPLIER) != int(self.cpf[SECOND_DIGIT_POSITION])):
            return 0
        return 1
