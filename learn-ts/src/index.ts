// basic types
let id: number = 5
let company: string = 'Morse'
let isPublished: boolean = true
let x: any = 'Hello'

let ids: number[] = [1, 2, 3, 4, 5]
let arr: any[] = [1, true, 'Hello']

// tuple: order matter
let person: [number, string, boolean] = [1, 'Tom', false]
// tuple array
let employee: [number, string][]
employee = [
  [1, 'Jill'],
  [3, 'Jumba']
]

// union: hold more than one type
let pid: string | number

// enum: by default equal to its 'index'
// when init to number, it will shift the next value as well
// when init to string, every enum must be init
enum Direction1 {
  Up = 2,
  Down,
  Left,
  Right
}

// object
const user: { id: number; name: string } = { id: 1, name: 'bob' }
// object: cleaner with type
type User = {
  id: number
  name: string
}
const user2: User = { id: 2, name: 'carla' }

// type assertion
let cid: any = 1
let customerId = <number>cid // syntax 1
let customerId2 = cid as number // syntax2

// functions
function addNum(x: number, y: number): number {
  return x + y
}
function log(message: string | number): void {
  console.log(message)
}

// inteface
interface UserInterface {
  readonly id: number
  name: string
  age?: number // optional
}
const user3: UserInterface = { id: 3, name: 'John' }
interface MathFunc {
  (x: number, y: number): number
}
const add: MathFunc = (x: number, y: number): number => x + y

// classes: with interface
interface PersonInterface {
  id: number
  name: string
  register(): string
}
class Person implements PersonInterface {
  public id: number
  public name: string

  public constructor(id: number, name: string) {
    this.id = id
    this.name = name
  }

  register() {
    return `${this.name} is now registered`
  }
}
const mully = new Person(1, 'Thomas')
// classes: children
class Employee extends Person {
  position: string

  constructor(id: number, name: string, position: string) {
    super(id, name)
    this.position = position
  }
}
const emp = new Employee(3, 'shawn', 'developer')

// generics: build reusable components
function getArray<T>(items: T[]): T[] {
  return new Array().concat(items)
}
// avoid using any, but still flexible
let numArray = getArray<number>([1, 2, 3, 4])
let strArray = getArray<string>(['a', 'b', 'c', 'd'])
