#!/usr/bin/python

import random


class Sumador:

    def parse(self, request, rest):

        try:
            numero = int(rest.split('/')[1])
        except ValueError:
            return None
        return numero

    def process(self, parsedRequest):

        try:
            print self.guardado
        except AttributeError:
            self.guardado = 0

        if not parsedRequest:
            return("400 Bad Request", "Go away!")

        if self.guardado:
            resultado = self.guardado + parsedRequest
            self.guardado = 0
        else:
            resultado = "Dame otro numero"
            self.guardado = parsedRequest

        htmlAnswer = '<html><body>' + str(resultado) + '</body></html>'
        return("200 OK", htmlAnswer)
