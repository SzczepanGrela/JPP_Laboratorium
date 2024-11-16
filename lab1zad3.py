# wersja proceduralna

# def optimizeTaskProcedural(tasks):
#     # sortowanie zadan malejaco wedlug wartosci nagroda/czas
#     tasks.sort(key=lambda x: -x['reward']/ x['time'])
#
#     total_reward = 0
#     total_time = 0
#     total_order = []
#
#
#     for task in tasks:
#         total_order.append(task)
#         total_time += task['time']
#         total_reward += task['reward']
#
#
#     return total_reward, total_order
#
#
# tasks = [
#     {'time': 3, 'reward': 10},
#     {'time': 2, 'reward': 5},
#     {'time': 1, 'reward': 8},
#     {'time': 4, 'reward': 7}
#
# ]
#
# print(optimizeTaskProcedural(tasks))



# wersja 2 - map sorted

def optimizeTaskProcedural(tasks):
    # sortowanie zadan malejaco wedlug wartosci nagroda/czas
    key_func = lambda task: -task['reward'] / task['time']

    sorted_tasks = sorted(tasks, key=key_func)

    total_reward = sum(map(lambda task : task['reward'], sorted_tasks))

    return total_reward, sorted_tasks 

tasks = [
    {'time': 3, 'reward': 10},
    {'time': 2, 'reward': 5},
    {'time': 1, 'reward': 8},
    {'time': 4, 'reward': 7}

]

print(optimizeTaskProcedural(tasks))