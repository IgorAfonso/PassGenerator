
import math
from random import randrange

def CalculateQuality(lenghtOfPass, extraPercentQuality):

    percent = (lenghtOfPass / 30) * 25 + extraPercentQuality
    qualityFromPassword = ''

    if percent >= 75:
        qualityFromPassword = 'Muito Forte'
    elif percent >= 50 and percent < 75:
        qualityFromPassword = 'Forte'
    elif percent < 50 and percent >= 40:
        qualityFromPassword = 'Média'
    else:
        qualityFromPassword = 'Fraca'

    print(f'A qualidade da senha é: {qualityFromPassword}')


def GeneratePass(lenghtOfPass, upperCaseCheck, numberCheck, symbolCheck):
    counter = 0
    password = ''
    chars = "abcçdefghijklmnopqrstuvwxyz"
    upperCaseChars = "ABCÇDEFGHIJKLMNOPQRSTUVWXYZ"
    numberChars = "1234565789"
    symbolChars = "!#$%&()*+,-./:;<=>?@[]^_{|}"
    extraPercentQuality = 0

    if(upperCaseCheck.upper() != 'N'):
        chars += upperCaseChars
        extraPercentQuality += 15
    
    if(numberCheck.upper() != 'N'):
        chars += numberChars
        extraPercentQuality += 25

    if(symbolCheck.upper() != 'N'):
        chars += symbolChars
        extraPercentQuality += 25

    while counter < lenghtOfPass:
        counter += 1
        randomNumber = math.floor(randrange(0, len(chars)-1))
        password += chars[randomNumber]

    print(password)
    CalculateQuality(lenghtOfPass, extraPercentQuality)


if __name__ == '__main__':
    lenghtOfPass = int(input('Digite a quantidade de caracteres que a senha deve ter: '))
    upperCaseCheck = input('Deseja que a senha contenha letras maiúsculas ?(Y, N): ')
    numberCheck = input('Deseja que a senha contenha números?(Y, N): ')
    symbolCheck = input('Deseja que a senha contenha caracteres especiais? (Y, N): ')
    GeneratePass(lenghtOfPass, upperCaseCheck, numberCheck, symbolCheck)