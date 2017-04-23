#!/usr/bin/env python
# encoding: utf-8
import randomGenerator
import math

# Classe para geracao de numeros aleatorios segundos varias distribuicoes
# Apenas a distribuicao exponencial negativa esta definida

# Gera um numero segundo uma distribuicao exponencial negativa de media m


def exponencial(media):
    return -media * math.log(randomGenerator.rand(10))

