#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
from queue import Queue
from threading import Event, Lock, Thread

forks = [Lock() for _ in range(5)]
tickets = [Event() for _ in range(5)]
results = []
waitq = Queue(maxsize=5)
servant_done = Event()


class Servant:
    def serve(self):
        global waitq
        global servant_done
        while servant_done.is_set() is not True:
            if waitq.empty() is not True:
                philo = waitq.get()
                philo_id = philo._id
                leftfork = forks[philo_id]
                rightfork = forks[(philo_id + 1) % len(forks)]

                # wait until both forks are ready to get.
                while leftfork.locked() is True or rightfork.locked() is True:
                    pass

                # tell the philosopher to get forks.
                print(f'Serve The philosopher {philo_id} ...')
                tickets[philo_id].set()
                waitq.task_done()


class Philosopher:
    def __init__(self, id, eattimes=1):
        self._id = id
        self._eattimes = eattimes
        self._ticket = tickets[id]
        self._leftfork = forks[id]
        self._rightfork = forks[(id + 1) % len(forks)]

    def pickLeftFork(self):
        self._leftfork.acquire()
        results.append([self._id, 1, 1])
        #print([self._id, 1, 1])

    def pickRightFork(self):
        self._rightfork.acquire()
        results.append([self._id, 2, 1])
        #print([self._id, 2, 1])

    def eat(self):
        results.append([self._id, 0, 3])
        time.sleep(2)
        print(f'philosopher {self._id} is eating...')
        #print([self._id, 0, 3])

    def putLeftFork(self):
        self._leftfork.release()
        results.append([self._id, 1, 2])
        #print([self._id, 1, 2])

    def putRightFork(self):
        self._rightfork.release()
        results.append([self._id, 2, 1])
        #print([self._id, 2, 2])

    def wantsToEat(self):
        while self._eattimes != 0:
            global waitq
            waitq.put(self)
            print(f'philosopher {self._id} get in the queue')
            self._ticket.wait()
            self.pickLeftFork()
            self.pickRightFork()
            self.eat()
            self.putLeftFork()
            self.putRightFork()
            self._ticket.clear()
            self._eattimes = self._eattimes - 1


def main():
    servant = Servant()
    eattimes = 5
    philosophers = [Philosopher(id, eattimes) for id in range(5)]
    tasks = []
    for philosopher in philosophers:
        task = Thread(target=philosopher.wantsToEat)
        tasks.append(task)

    for task in tasks:
        task.start()

    servant_task = Thread(target=servant.serve)
    servant_task.start()

    for task in tasks:
        task.join()

    # all philosopher have done eating, tell the servant to stop.
    servant_done.set()
    servant_task.join()
    print(results)


if __name__ == '__main__':
    main()
