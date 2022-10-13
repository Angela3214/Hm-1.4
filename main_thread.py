import threading

cv = threading.Condition()
current_value = 1

def thread_function(i, n): # Лучше называть переменные в соответствии с их значениями (речь про n). Например,
    #def thread_function(result, iteration_count):
    global cv
    global current_value

    for j in range(n): # Тогда здесь for iteration in range(iteration_count):
        with cv:
            cv.wait_for(lambda: current_value == i) #cv.wait_for(lambda: current_value == result)
            print(i, end='') #print(result, end='')
            current_value = 1 + current_value % 3
            cv.notify_all()

n = int(input()) # iteration_count = int(input()). Лучше использовать функции (то есть засунуть это в функцию main и
#добавить ниже if __name__ == "__main__": main()

threads = [
    threading.Thread(target=thread_function, args=(1, n)), #Аналогично заменить n на, например, iteration_count
    threading.Thread(target=thread_function, args=(2, n)),
    threading.Thread(target=thread_function, args=(3, n)),
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()