import requests
from flask import Flask, render_template, request
import math

def calcular():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operacao = request.form['operacao']

    if operacao == '+':
        resultado = num1 + num2
        etapas = f'{num1} + {num2} = {resultado}'
    elif operacao == '-':
        resultado = num1 - num2
        etapas = f'{num1} - {num2} = {resultado}'
    elif operacao == '*':
        resultado = num1 * num2
        etapas = f'{num1} * {num2} = {resultado}'
    elif operacao == '/':
        if num2 != 0:
            resultado = num1 / num2
            etapas = f'{num1} / {num2} = {resultado}'
        else:
            resultado = 'Erro'
            etapas = 'Não é possvel dividir por 0.'
    
    else:
        resultado = 'Operação inválida'
        etapas = 'A operação selecionada é inválida.'

    return render_template('calculadora.html', etapas=etapas, resultados=resultado)
