#!/usr/bin/python


class Hola:

    def parse(self, request, rest):

        return None

    def process(self, parsedRequest):

        return("200 OK", "<html><body><h1>Hola</html></body></h1>")


class Adios:

    def parse(self, request, rest):

        return None

    def process(self, parsedRequest):

        return("200 OK", "<html><body><h1>Adios</html></body></h1>")


if __name__ == "__main__":
    serv = Sumador("localhost", 1234)
