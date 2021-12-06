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
