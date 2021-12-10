## Python and OOP:
Python supports different programming paradigms (approaches). OOP is one of the most popular approaches based on object 
usage.

An object has two characteristics:
* Attributes
* Behavior

`Object` is simply a collection of data (variables) and methods (functions) that act on those data.

## DRY:
DRY (Don't Repeat Yourself) principle, multiple functions often work with same data and OOP allows, to avoid repetition
from that side.

## OOP Principles:
* `Inheritance`: A process of using details from a new class without modifying existing class.
* `Encapsulation`: Hiding the private details of a class from other objects.
* `Polymorphism`: A concept of using common operation in different ways for different data input.
* `Abstraction`: Its main goal is to handle complexity by hiding unnecessary details from the user. That enables the user
to implement more complex logic on top of the provided abstraction without understanding or even thinking about all the 
hidden complexity.

## Class:
* A class is a blueprint for the object.
* Class is just template which will be base for creating some object.
* Class can be created with class keyword followed by class name and colon for it's body
* First line of class body is usually docstring (has a brief description about the class)

## Object:
* Object is instance of a class
* To create an object, we usually need class name.

## Methods:
* Methods are functions defined inside the body of a class, they are used to define the behaviors of an object.
* Any object method has `self` as first parameter.

## Constructor:
* __ new __ method is used to construct new object.
* We should use it if we need to control the object creation somehow.
* Constructor is method that is called while object is instantiate.

## Initializer:
* Initializer is called while object is initialize.
* Initializer has the following name: __ init __

## Object Attributes (Properties):
* Object attribute is component of its value.
* Object attributes are created whenever value is assigned to them inside methods with self.
* To access attributes and methods of the object we can use dot operator.

## self:
* Self is reference to current object.
* If some object calls a method that self is that object.

## Deleting Attributes and Objects:
* Any attribute of an object can be deleted anytime, using `del` statement.
* We can even delete the object identifier, using the `del` statement.

## Encapsulation:
Using OOP in Python, we can restrict access to methods and variables. This prevents data from direct modification which 
is called encapsulation. In Python, we denote private attributes using underscore as prefix i.e. single '_' or double '__'.

We can't change it from outside class because Python treats the __engine as private attributes.

## Polymorphism:
Polymorphism is an ability in OOP to use common interface for multiple from data types.

## class and instance attributes:
* Instance attributes are owned by the specific instances of a class. This means for two different instances the instance
attributes are usually different.
* Class (static) attributes are attributes which are owned by the class itself. They will be shared by all the instances 
of the class. Therefore, they have the same value for every instance. We define class attributes outside, of all the methods
usually they are placed at the top, right below the class header.
* If you want to change a class attribute, you have to do it with the notation ClassName.AttributeName. Otherwise, you 
will create a new instance variable.

## Inheritance: 
* Inheritance refers to defining a new class with little or no modification to an existing class.
* The new class is called derived (child) class and the one from which it inherits is called the base (parent) class.
* Derived class inherits features from the base class, adding a new features to it. This results into re-usability of code.
* The idea of class inheritance is based on the fact that some classes have much in common with other classes, but have
some extra features.
* So to avoid code repetition and to provide some relationship mechanism for these classes inheritance comes into.

## Overriding Methods:
We can change the inherited instance methods behavior (overriding). To override method we should just declare method with
the signature same as in parent class. When this happens, the method in the child class overrides that in the base class.

## isinstance(), issubclass():
* `isinstance(obj, type)` checks if obj is instance of Type. For example isinstance(bmw, Car)
* `issubclass(Type1, Type2)` checks if Type1 is subclass of Type2. For example issubclass(BMW, Car)

## Private, Public, Protected:
Python doesn't have any mechanisms, that would effectively restrict you from accessing a variable or calling a member
method. All of this is a matter of culture and convention.

`Public`: All member variables and methods are public by default in python.
`Private`: By declaring your data member private you mean, that nobody shoud be able to access it from outside the class (convention = __)
`Protected`: Protected member is accessible only from within the class, and it's subclasses (convention = _)

## Multiple Inheritance:
* Class can be derived from more than one base classes in Python. This is called multiple inheritance.
* In multiple inheritance, the features of all the base classes are inherited into the derived class.

## Multilevel Inheritance:
* We can also inherit from a derived class. This is called multilevel inheritance. It can be of any depth in Python.
* In multilevel inheritance, features of the base class and the derived class is inherited into the new derived class.

## Object Class:
* All the Python classes at the end inherit from object class
* Either built-in or user-defines, are derived classes and all objects are instances of object class.

## Class Attributes:
Variable declared inside the class definition, but not inside a method are class (static) variable (attributes)

## Class Method and Static Method:
* `classmethod`: A method that receives the class as an implicit argument instead of the instance. (recommended).
* `staticmethod`: A method that does not receive any implicit argument as a first argument.
* static and class methods are easily accomplished using the built-in decorators.

## Getters and Setters:
Solution to add constraint to attribute value can be to hide the attribute (make it private) and define new getter and
setter interfaces to manipulate it. This solution is not pythonic as it requires redesign (at least making attribute private)
or writing much more code.

## Property Function:
property() is a function that defines the functions for getting and setting some attribute. Even if we use private getter
and setter function still better with decorators.

## MRO:
MRO is a concept used in inheritance. It is the order in which a method is searched for in a classes hierarchy and is
especially useful in Python because Python supports multiple inheritance.

MRO of a class can be viewed as the __ mro __ attribute or mro() method. 

## Exceptions:
Exception (Exceptional Situation), an exception is an event, which occurs during the execution of a program, that disrupts
the normal flow of the program's instructions. When writing a program, we more often than not will encounter errors. 
There is number of built-in Exception types.

* We can handle Exceptions using try statement.
* We can have optional finally clause that will execute a code either exception is generated or not.
* Some exceptions are raised automatically, but we can also raise them manually. (raise KeyboardInterrupt)