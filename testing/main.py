from lesson import LessonSource

class MainSource(LessonSource):

    def addition(self):
        return print ('addition' + str(2 + 2))

    def subtraction(self):
        return print ('subtraction' + str(2 + 2))

if __name__ == '__main__':
    main = MainSource()
    main.multiplication()
