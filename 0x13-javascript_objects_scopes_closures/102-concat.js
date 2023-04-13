#!/usr/bin/node
const fs = require('fs').promises;

async function concatenateFiles(file1, file2, outputFile) {
  const fArg = await fs.readFile(file1, 'utf-8');
  const sArg = await fs.readFile(file2, 'utf-8');
  await fs.writeFile(outputFile, fArg + sArg);
}

concatenateFiles(process.argv[2], process.argv[3], process.argv[4])
  .then(() => console.log('Files concatenated successfully!'))
  .catch((error) => console.error(`Error concatenating files: ${error.message}`));
