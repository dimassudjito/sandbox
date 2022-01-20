const { TestScheduler } = require('@jest/core')
const functions = require('./functions')

//basic
test('Adds 2+2 to equal 4', () => {
    expect(functions.add(2, 2)).toBe(4)
})
test('Adds 2+2 to NOT equal 5', () => {
    expect(functions.add(2, 2)).not.toBe(5)
})

// boolean
test('Should be null', () => {
    expect(functions.isNull()).toBeNull()
})
test('Should be falsy', () => {
    expect(functions.checkValue(undefined)).toBeFalsy()
})

// toEqual
test('User should be Brad Traversy object', () => {
    expect(functions.createUser()).toEqual({firstName: 'Brad', lastName: 'Traversy'})
})

// less/greater than
test('Should be under 1600', () => {
    const load1 = 800
    const load2 = 700
    expect(load1 + load2).toBeGreaterThan(800)
})

// regex
test('There is no I in team', () => {
    expect('team').not.toMatch(/I/)
})

// Arrays
test('Admin should be in username', () => {
    usernames = ['john', 'karen', 'admin']
    expect(usernames).toContain('admin')
})

// async API data (Promise)
test('user fetch name should be Leanne Graham', () => {
    expect.assertions(1)
    return functions.fetchUser().then(data => {
        expect(data.name).toEqual('Leanne Graham')
    })
})

// async API data (Async and await)
test('user fetch name should be Leanne Graham', async () => {
    expect.assertions(1)
    const data = await functions.fetchUser();
    expect(data.name).toEqual('Leanne Graham')
})

