# Linked List

This is a class that will create Linked Lists in Python

## Features

* Creates a class for a ```Node``` which is aware of the value as ```val``` and next as ```_next```

* Ensure that you have a ```__str__``` method defined to return the value of the next node when printed

* Create a Class for a ```LinkedList``` which creates an empty Linked List when instantiated.
* This class should be aware of a default ```None``` value assigned to ```head``` when the list is created.
* This class should be aware of the ```len``` of the list, which represents the count of Nodes in the list at any time
* This class should have the ability to accept an iterable as an argument when instantiated, such as ```[1, 2, 3, 4]```, and creates a new Node in the list for each value in the iterable.
* Define any further magic methods such as ```len``` and ```str``` to support user functionality and informative responses.
* Define a method called ```insert``` which takes any value as an argument and adds that value to the ```head``` of the list with an O(1) Time performance.
* Define a method called ```includes``` which takes any value as an argument and returns ```True``` or ```False``` depending on whether that value exists as a Node value within the list.

## New Features Added 3-December Which Extend the LL Class

* ```.append(value)``` which adds a new node with the given value to the end of the list
* ```.insertBefore(value, newVal)``` which add a new node with the given newValue immediately before the first value node
* ```.insertAfter(value, newVal)``` which add a new node with the given newValue immediately after the first value node

## Testing

All testing is available via Pytest
