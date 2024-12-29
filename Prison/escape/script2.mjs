function readFileContent(callback) {
  let data = '';

  process.stdin.on('data', chunk => {
    data += chunk;
  });

  process.stdin.on('end', () => {
    callback(data);
  });
}

// Utilisation de la fonction
readFileContent(content => {
  console.log(content);
});
