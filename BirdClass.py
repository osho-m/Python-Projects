class Bird:
      species="birds";

      def __init__(self, name, age):
            self.name=name;
            self.age=age;
            print(self.name, "is a ", self.species, "whose age is", self.age);


# Child class (inherits from Bird class)
class Parrot(Bird):
	color="green"
	def run(self, speed):
        		return "{} runs{} " .format( self.name, speed)
poki=Parrot('Poki', 7);
print(poki.color);
print(poki.run('first'));
