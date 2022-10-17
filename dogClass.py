class Dog:
      species = 'mammal';
      print('In class Dog is', species);
      print('In class Dog');

      def __init__(self, age, name):
            self.age=age;
            self.name=name;
      def bark(self):
            for i in range (1, self.age):
                  print('bark');

tom=Dog(7, 'Tom');
print(tom.name);
tom.bark();
