const { readFile, writeFile } = import("./fileManager.cjs");

readFile('Hello World.txt', (err, data) => {
    if (err) {
      console.error('Error reading file:', err);
      return;
    }
  
    const contentToWrite = data || 'Writing to the file';
    writeFile('Bye World.txt', contentToWrite, (writeErr) => {
      if (writeErr) {
        console.error('Error writing file:', writeErr);
        return;
      }
      console.log('Content written to Bye World.txt');
    });
});
  