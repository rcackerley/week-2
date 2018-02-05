class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
        self.num_unique_people_greeted = {}
    
    def __repr__(self):
        return '%s %s %s' % (self.name, self.email, self.phone)

    def greet(self, other_person):
        print 'Hello %s, I am %s!' % (other_person.name, self.name)
        self.greeting_count += 1
        if other_person.name not in self.num_unique_people_greeted:
            self.num_unique_people_greeted[other_person.name] = 1
    
    def print_contact_info(self):
        print '%s\'s email: %s, %s\'s phone number: %s' % (self.name, self.email, self.name, self.phone)
    
    def add_friend(self, other_person):
        self.friends.append(other_person)
    def num_friends(self):
        print len(self.friends)
        


sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')
robby = Person('Robby', 'robbby@aol.com', '125-586-3456')

print sonny.greet(jordan)
print sonny.greet(jordan)
print jordan.greet(sonny)
print sonny.greet(robby)

print '%s, %s' % (sonny.email, sonny.phone)
print '%s, %s' % (jordan.email, jordan.phone)

class Vehicle(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def print_info(self):
        print self.make, self.model, self.year

car = Vehicle('Nissan', 'Leaf', 2015)
# print car.make
car.print_info()
sonny.print_contact_info()
jordan.add_friend(sonny)
jordan.num_friends()

print sonny.greeting_count
print '%r' % sonny

print sonny.num_unique_people_greeted