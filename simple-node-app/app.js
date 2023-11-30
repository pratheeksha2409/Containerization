const express = require('express');
const app = express();

const port = 4000;

app.get('/', (req, res) => {
  res.send(`This is another Container called Container 3, Node Server is running on port ${port}`);
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

