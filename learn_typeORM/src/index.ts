import express from 'express'
import cors from 'cors'
import { createConnection } from 'typeorm'
import { Product } from './entity/product'

createConnection().then((connection) => {
  const productRepositiory = connection.getMongoRepository(Product)
  const app = express()

  app.use(
    cors({
      origin: 'http://localhost:3000'
    })
  )

  app.use(express.json())

  console.log('listening to port 8000')
  app.listen(8000)
})
