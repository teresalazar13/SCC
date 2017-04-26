#!/usr/bin/env python
# encoding: utf-8
from randomGenerator import *
import math


# Classe para geracao de numeros aleatorios segundos varias distribuicoes
class Aleatorio:

    # Gera um numero segundo uma distribuicao exponencial negativa de media m
    @staticmethod
    def exponencial(media, s):
        return (-media) * math.log(RandomGenerator.rand(s))

    # Gera um numero segundo uma distribuicao normal
    @staticmethod
    def normal(m, d, rand_stream):
        y = [0, 0]
        x = [0, 0]
        while True:
            while True:
                v1 = 2 * RandomGenerator.rand(rand_stream) - 1
                v2 = 2 * RandomGenerator.rand(rand_stream) - 1
                w = math.pow(v1, 2) + math.pow(v2, 2)
                if w > 1:
                    break
                y[0] = v1 * math.pow(((-2 * math.log(w)) / w), 0.5)
                y[1] = v2 * math.pow(((-2 * math.log(w)) / w), 0.5)
            if y[0] < -1 or y[1] < -1 or y[0] > 1 or y[1] > 1:
                break
        x[0] = m + y[0] * d
        x[1] = m + y[1] * d
        # print("x1 = ", x[0], "x2 = ", x[1])
        return x
