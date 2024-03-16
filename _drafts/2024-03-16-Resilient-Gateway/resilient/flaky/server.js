const express = require('express');
const app = express();
const port = 8000;

app.get('/flaky', (req, res) => {
  res.send("I'm here.");
});

app.listen(port, () => {
  console.log(`Flaky service listening at http://localhost:${port}`);
});