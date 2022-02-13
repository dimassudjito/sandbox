import express from 'express'
import cors from 'cors'

const app = express()

app.use(
  cors({
    origin: 'http://localhost:3000'
  })
)

app.use(express.json())

console.log('listening to port 8000')
app.listen(8000)
