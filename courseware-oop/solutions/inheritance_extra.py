'''

Imagine you are writing some code to control virtual machines running
on the cloud. Create several classes for the abstractions in your
program:

>>> web1 = WebServer('www1.example.com')
>>> web2 = WebServer('www2.example.com')
>>> web3 = WebServer('www3.example.com')

>>> db1 = DatabaseServer('db1.example.com')
>>> db2 = DatabaseServer('db2.example.com')

>>> lb = LoadBalancer('lb.example.com')

>>> ml1 = MachineLearningNode('ml1.example.com')
>>> ml2 = MachineLearningNode('ml2.example.com')
>>> ml3 = MachineLearningNode('ml3.example.com')
>>> ml4 = MachineLearningNode('ml4.example.com')

>>> web1.start()
>>> web2.start()
>>> db1.start()
>>> ml2.start()
>>> web2.stop()
>>> db2.stop()

>>> web1.is_running()
True
>>> web2.is_running()
False
>>> db1.is_running()
True
>>> db2.is_running()
False
>>> ml2.is_running()
True

Make each of them subclass a base called Server. Put as much code
into this base class as you can:

>>> isinstance(web1, Server)
True
>>> isinstance(db1, Server)
True
>>> isinstance(ml1, Server)
True

For example, the is_running(), start() and stop() methods:

>>> hasattr(Server, 'is_running')
True
>>> hasattr(Server, 'start')
True
>>> hasattr(Server, 'stop')
True

(hasattr() returns True if the class has that method defined, else it
returns False. It works on regular objects, too.)

Since we have a lot of machines to manage, let's create some
abtractions to manage groups of them.

>>> webapp_fleet = WebAppFleet([
...     web1, web2, web3,
...     db1, db2, lb])
>>> small_deep_fleet = DeepLearningFleet([ml1, ml2, lb])
>>> big_deep_fleet = DeepLearningFleet([
...     ml1, ml2, ml3, ml4, lb])

As before, these will share a common base: a class called Fleet. Fleet
objects have methods that tell you which machines are currently
running, and also let you start or stop all machines in the fleet.

>>> webapp_fleet.running()
['www1.example.com', 'db1.example.com']

>>> webapp_fleet.stop_all()
>>> webapp_fleet.running()
[]
>>> webapp_fleet.start_all()
>>> webapp_fleet.running()
['www1.example.com', 'www2.example.com', 'www3.example.com', 'db1.example.com', 'db2.example.com', 'lb.example.com']


>>> small_deep_fleet.running()
['ml2.example.com', 'lb.example.com']
>>> big_deep_fleet.running()
['ml2.example.com', 'lb.example.com']
>>> big_deep_fleet.start_all()
>>> big_deep_fleet.running()
['ml1.example.com', 'ml2.example.com', 'ml3.example.com', 'ml4.example.com', 'lb.example.com']

And of course, put as many of these in the Fleet class as you can, so
they can all be used by the subclasses.

>>> hasattr(Fleet, 'running')
True
>>> hasattr(Fleet, 'start_all')
True
>>> hasattr(Fleet, 'stop_all')
True

Often, your subclasses will have their own specialized methods, not
shared by the base class:

>>> webapp_fleet.webservers()
['www1.example.com', 'www2.example.com', 'www3.example.com']

>>> big_deep_fleet.calculating_nodes()
4
>>> small_deep_fleet.calculating_nodes()
2

'''

# Write your code here:

class Server:
    runs_http_process = False
    is_calculating_server = False
    def __init__(self, domain):
        self.domain = domain
        self.state = 'stopped'
    def stop(self):
        self.state = 'stopped'
    def start(self):
        self.state = 'running'
    def is_running(self):
        return self.state == 'running'
    def report(self):
        return self.report_for('server')
    def report_for(self, description):
        return description + ' is ' + self.state

class WebServer(Server):
    runs_http_process = True
    def report(self):
        return self.report_for('web server')

class DatabaseServer(Server):
    def report(self):
        return self.report_for('DB server')

class LoadBalancer(Server):
    def report(self):
        return self.report_for('LB server')

class MachineLearningNode(Server):
    is_calculating_server = True
    def report(self):
        return self.report_for('ML server')

class Fleet:
    def __init__(self, servers):
        self.servers = servers
    def stop_all(self):
        for server in self.servers:
            server.stop()
    def start_all(self):
        for server in self.servers:
            server.start()
    def running(self):
        return [
            server.domain for server in self.servers
            if server.is_running()
            ]

class WebAppFleet(Fleet):
    def webservers(self):
        webservers = []
        for server in self.servers:
            if server.runs_http_process:
                webservers.append(server.domain)
        return webservers
        # Another way to do it:
        return [
            server.domain for server in self.servers
            if server.runs_http_process
            ]

class DeepLearningFleet(Fleet):
    def calculating_nodes(self):
        return len([
            server.domain for server in self.servers
            if server.is_calculating_server
            ])

# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# Copyright 2015-2018 Aaron Maxwell. All rights reserved.
