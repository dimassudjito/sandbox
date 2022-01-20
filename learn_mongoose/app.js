const express = require('express')
const mongoose = require('mongoose')
const bodyParser = require('body-parser')
require('dotenv/config')

const app = express()

/* MIDDLEWARE */
app.use(bodyParser.json())

/* ROUTES */
const postsRouter = require('./routes/posts')
app.use('/posts', postsRouter)

app.get('/', (req, res) => {
  res.send('we are on home')
})

/* CONNECT TO DB */
mongoose.connect(
  process.env.DB_CONNECTION,
  { useNewUrlParser: true, useUnifiedTopology: true },
  () => {
    console.log('connected to DB')
  }
)

/* SERVER */
app.listen(3000)
