import { createConnection } from 'typeorm'
import { Product } from '../src/entity/product'
import faker from 'faker'

createConnection().then(async (connection) => {
  const productRepositiory = connection.getMongoRepository(Product)

  for (let i = 0; i < 50; i++) {
    await productRepositiory.save({
      title: faker.lorem.words(2),
      description: faker.lorem.sentences(10),
      price: faker.datatype.number(100),
      images: faker.image.imageUrl()
    })
  }

  process.exit()
})
