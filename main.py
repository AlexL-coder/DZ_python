
from homework_01.main import power_numbers
from homework_01.main import filter_numbers


if __name__ == '__main__':
    #print(power_numbers(2, 6, 5, 20, 100))
    #print(filter_numbers([2, 3, 4, 5, 8],"prime"))
    #filter
    def bread(func):
        def wrapper():
            print('</------\>')
            func()
            print('<\______/>')
        return wrapper

    def ingredients(func):
        def wrapper():
            print ("#помидоры#")
            func()
            print ("~салат~")
        return wrapper


    #sandwich()
    #sandwich = bread(ingredients(sandwich))
    #sandwich()
    @bread
    @ingredients
    def sandwich(food="--ветчина--"):
        print(food)

    #sandwich()

    def decorator_maker():
        print("Я создаю декораторы! Я буду вызван только раз: " + \
        "когда ты попросишь меня создать тебе декоратор.")

        def my_decorator(func):
            print("Я - декоратор! Я буду вызван только раз: в момент декорирования функции.")

            def wrapped():
                print("Я - обёртка вокруг декорируемой функции. "
                      "Я буду вызвана каждый раз когда ты вызываешь декорируемую функцию. "
                      "Я возвращаю результат работы декорируемой функции.")
                return func()

            print("Я возвращаю обёрнутую функцию.")

            return wrapped

        print("Я возвращаю декоратор.")
        return my_decorator


    @decorator_maker()
    def decorated_function():
        print("Я - декорируемая функция.")


    decorated_function()