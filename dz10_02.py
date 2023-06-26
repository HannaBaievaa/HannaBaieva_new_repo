def list_unique_check():
    try:
        my_list = [int(item) for item in input("Введіть список чисел через кому: ").split(sep=',')]
        if len(my_list) == len(set(my_list)):
            print("Всі елементи списку унікальні")
        else:
            print("Не всі елементи із списку є унікальними")
    except ValueError:
        print("Введені не числа", file=sys.stderr)
    except Exception as ex:
        print(ex, "Невідома помилка", file=sys.stderr)


list_unique_check()