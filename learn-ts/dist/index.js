"use strict";
// basic types
let id = 5;
let company = 'Morse';
let isPublished = true;
let x = 'Hello';
let ids = [1, 2, 3, 4, 5];
let arr = [1, true, 'Hello'];
// tuple: order matter
let person = [1, 'Tom', false];
// tuple array
let employee;
employee = [
    [1, 'Jill'],
    [3, 'Jumba']
];
// union: hold more than one type
let pid;
// enum: by default equal to its 'index'
// when init to number, it will shift the next value as well
// when init to string, every enum must be init
var Direction1;
(function (Direction1) {
    Direction1[Direction1["Up"] = 2] = "Up";
    Direction1[Direction1["Down"] = 3] = "Down";
    Direction1[Direction1["Left"] = 4] = "Left";
    Direction1[Direction1["Right"] = 5] = "Right";
})(Direction1 || (Direction1 = {}));
// object
const user = { id: 1, name: 'bob' };
const user2 = { id: 2, name: 'carla' };
// type assertion
let cid = 1;
let customerId = cid; // syntax 1
let customerId2 = cid; // syntax2
// functions
function addNum(x, y) {
    return x + y;
}
function log(message) {
    console.log(message);
}
const user3 = { id: 3, name: 'John' };
const add = (x, y) => x + y;
class Person {
    constructor(id, name) {
        this.id = id;
        this.name = name;
    }
    register() {
        return `${this.name} is now registered`;
    }
}
const mully = new Person(1, 'Thomas');
// classes: children
class Employee extends Person {
    constructor(id, name, position) {
        super(id, name);
        this.position = position;
    }
}
const emp = new Employee(3, 'shawn', 'developer');
// generics: build reusable components
function getArray(items) {
    return new Array().concat(items);
}
// avoid using any, but still flexible
let numArray = getArray([1, 2, 3, 4]);
let strArray = getArray(['a', 'b', 'c', 'd']);
